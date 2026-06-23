import assert from 'node:assert/strict';
import { describe, it } from 'vitest';

import {
  buildClusterArtifact,
  buildClusterKey,
  buildFeatureBag,
  buildStructuredFingerprint,
  dedupeLatestByTitleSlug,
  structuralSimilarity,
  type ExtractedFeatures,
} from '../src/submission-ast-cluster-poc.ts';

function baseFeatures(): ExtractedFeatures {
  return {
    parseOk: true,
    syntaxError: null,
    imports: [],
    calledFunctions: [],
    assignedNames: [],
    attributeNames: [],
    forCount: 0,
    whileCount: 0,
    ifCount: 0,
    comprehensionCount: 0,
    maxLoopDepth: 0,
    hasDeque: false,
    hasPopleft: false,
    hasAppendleft: false,
    hasCounter: false,
    hasDefaultdict: false,
    hasHeapq: false,
    hasSet: false,
    hasDict: false,
    hasSortedOrSort: false,
    hasVisited: false,
    hasRecursion: false,
    hasLeftRightPointers: false,
    hasMid: false,
    hasPrefixSignal: false,
    hasDpSignal: false,
    hasUnionFindSignal: false,
    hasTreeSignal: false,
    hasGridSignal: false,
    hasGraphSignal: false,
    hasNeighborSignal: false,
    hasQueueLoopSignal: false,
  };
}

describe('submission AST cluster POC classifier', () => {
  it('produces a neutral frontier fingerprint for queue traversal', () => {
    const result = buildStructuredFingerprint({
      ...baseFeatures(),
      hasDeque: true,
      hasPopleft: true,
      hasVisited: true,
      hasGridSignal: true,
      hasNeighborSignal: true,
      hasQueueLoopSignal: true,
      whileCount: 1,
    });

    assert.deepEqual(result.loops, ['while']);
    assert.deepEqual(result.dataStructures, ['deque', 'graph_state', 'grid', 'set']);
    assert.deepEqual(result.transitionOrder, ['frontier_pop_then_expand']);
    assert.equal(result.answerUpdateTiming, 'on_frontier_hit');
    assert.match(buildClusterKey(result), /transition=frontier_pop_then_expand/);
  });

  it('produces a neutral midpoint fingerprint for boundary narrowing', () => {
    const result = buildStructuredFingerprint({
      ...baseFeatures(),
      hasMid: true,
      whileCount: 1,
    });

    assert.deepEqual(result.ops, ['mid_compute']);
    assert.deepEqual(result.stateVars, ['mid']);
    assert.deepEqual(result.transitionOrder, ['midpoint_then_boundary_narrow']);
    assert.equal(result.answerUpdateTiming, 'after_boundary_update');
  });

  it('keeps only the latest accepted submission per title slug in unique mode', () => {
    const rows = [
      { id: 'new', titleSlug: 'two-sum', status: 'Accepted', content: '', createdAt: new Date('2026-06-22T00:00:00Z'), submissionDetails: null },
      { id: 'older', titleSlug: 'two-sum', status: 'Accepted', content: '', createdAt: new Date('2026-06-21T00:00:00Z'), submissionDetails: null },
      { id: 'other', titleSlug: 'three-sum', status: 'Accepted', content: '', createdAt: new Date('2026-06-20T00:00:00Z'), submissionDetails: null },
      { id: 'missing', titleSlug: null, status: 'Accepted', content: '', createdAt: new Date('2026-06-19T00:00:00Z'), submissionDetails: null },
    ];

    const deduped = dedupeLatestByTitleSlug(rows, 10);

    assert.deepEqual(deduped.map((row) => row.id), ['new', 'other']);
  });

  it('builds weighted feature bags for structure similarity clustering', () => {
    const frontier = buildFeatureBag({
      ...baseFeatures(),
      hasDeque: true,
      hasPopleft: true,
      hasVisited: true,
      hasQueueLoopSignal: true,
      whileCount: 1,
    });
    const similarFrontier = buildFeatureBag({
      ...baseFeatures(),
      hasDeque: true,
      hasPopleft: true,
      hasVisited: true,
      hasQueueLoopSignal: true,
      whileCount: 1,
      hasGridSignal: true,
    });
    const midpoint = buildFeatureBag({
      ...baseFeatures(),
      hasMid: true,
      whileCount: 1,
    });

    assert.equal(frontier['motif:frontier_pop_then_expand'], 3);
    assert.equal(frontier['role:explicit_state_init'], 1);
    assert.ok(structuralSimilarity(frontier, similarFrontier) > structuralSimilarity(frontier, midpoint));
  });

  it('builds a compact JSON artifact grouped by fingerprint cluster', () => {
    const features = { ...baseFeatures(), hasMid: true, whileCount: 1 };
    const fingerprint = buildStructuredFingerprint(features);
    const featureBag = buildFeatureBag(features);
    const artifact = buildClusterArtifact(
      [
        {
          submission: {
            id: 'submission-1',
            titleSlug: 'binary-search',
            status: 'Accepted',
            content: 'def search(): pass',
            createdAt: new Date('2026-06-22T00:00:00Z'),
            submissionDetails: null,
          },
          lang: 'python3',
          features,
          fingerprint,
          featureBag,
          clusterKey: buildClusterKey(fingerprint),
        },
      ],
      { limit: 10, scan: 20, unique: true, threshold: 0.34, json: false },
      '2026-06-22T12:00:00.000Z',
    );

    assert.equal(artifact.generatedAt, '2026-06-22T12:00:00.000Z');
    assert.deepEqual(artifact.summary, { submissionCount: 1, clusterCount: 1 });
    assert.ok(artifact.clusters[0].evidence.some((entry) => entry.feature === 'motif:midpoint_boundary_narrow'));
    assert.equal(artifact.clusters[0].submissions[0].titleSlug, 'binary-search');
    assert.equal('content' in artifact.clusters[0].submissions[0], false);
  });
});
