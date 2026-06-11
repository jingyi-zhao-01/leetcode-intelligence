'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { SubmissionGraphView } from './submission-graph';
import { type SubmissionGraph } from '../lib/submission-graph';
import type { SubmissionRow } from '../lib/data';

type Props = {
  submissions: SubmissionRow[];
  graph: SubmissionGraph;
  initialSelectedSlug?: string | null;
};

type GraphClusterTree = {
  key: string;
  label: string;
  questionCount: number;
};

function defaultClusterHue(key: string) {
  let hash = 0;
  for (let index = 0; index < key.length; index += 1) {
    hash = (hash * 31 + key.charCodeAt(index)) % 100000;
  }
  return 290 + (hash % 90);
}

function matchesClusterSelection(
  node: SubmissionGraph['nodes'][number],
  selectedPrimaryKeys: Set<string>,
) {
  const hasPrimaryFilter = selectedPrimaryKeys.size > 0;

  if (!hasPrimaryFilter) {
    return true;
  }

  return node.templateGroups.some((group) => selectedPrimaryKeys.has(group.key));
}

function filterGraph(
  graph: SubmissionGraph,
  needle: string,
  selectedPrimaryKeys: Set<string>,
) {
  const filteredNodes = graph.nodes.filter((node) => {
    if (!matchesClusterSelection(node, selectedPrimaryKeys)) {
      return false;
    }
    const haystack = [node.title, node.slug, node.difficulty].filter(Boolean).join(' ').toLowerCase();
    return haystack.includes(needle);
  });

  const nodeIds = new Set(filteredNodes.map((node) => node.id));
  return {
    ...graph,
    nodes: filteredNodes,
    edges: graph.edges.filter((edge) => nodeIds.has(edge.source) && nodeIds.has(edge.target)),
  };
}

function buildClusterTree(submissions: SubmissionRow[]): GraphClusterTree[] {
  const slugMembers = new Map<string, Map<string, string>>();

  for (const submission of submissions) {
    if (!submission.titleSlug) {
      continue;
    }

    const slug = submission.titleSlug.toLowerCase();
    const membership = slugMembers.get(slug) ?? new Map<string, string>();

    for (const tag of submission.tags) {
      if (tag.dimension !== 'template' || !tag.parentKey) {
        continue;
      }

      membership.set(tag.parentKey, tag.parentLabel ?? tag.parentKey);
    }

    slugMembers.set(slug, membership);
  }

  const primaryCounts = new Map<string, { label: string; slugs: Set<string> }>();

  for (const [slug, membership] of slugMembers.entries()) {
    for (const [primaryKey, primaryLabel] of membership.entries()) {
      const primary = primaryCounts.get(primaryKey) ?? {
        label: primaryLabel,
        slugs: new Set<string>(),
      };
      primary.slugs.add(slug);
      primaryCounts.set(primaryKey, primary);
    }
  }

  return [...primaryCounts.entries()]
    .map(([key, primary]) => ({
      key,
      label: primary.label,
      questionCount: primary.slugs.size,
    }))
    .sort((left, right) => right.questionCount - left.questionCount || left.label.localeCompare(right.label));
}

export function GraphWorkbench({ submissions, graph, initialSelectedSlug }: Props) {
  const [query, setQuery] = useState('');
  const [selectedNodeSlug, setSelectedNodeSlug] = useState<string | null>(initialSelectedSlug?.toLowerCase() ?? null);
  const [selectedPrimaryKeys, setSelectedPrimaryKeys] = useState<Set<string>>(() => new Set());
  const [hoveredPrimaryKey, setHoveredPrimaryKey] = useState<string | null>(null);
  const clusterTree = useMemo(() => buildClusterTree(submissions), [submissions]);
  const [clusterHueByKey, setClusterHueByKey] = useState<Record<string, number>>(() =>
    Object.fromEntries(buildClusterTree(submissions).map((cluster) => [cluster.key, defaultClusterHue(cluster.key)])),
  );
  const filteredGraph = useMemo(
    () => filterGraph(graph, query.trim().toLowerCase(), selectedPrimaryKeys),
    [graph, query, selectedPrimaryKeys],
  );

  const selectedNodeExists = useMemo(() => {
    if (!selectedNodeSlug) {
      return null;
    }

    return filteredGraph.nodes.find((node) => node.slug === selectedNodeSlug) ?? null;
  }, [selectedNodeSlug, filteredGraph]);

  function togglePrimary(primaryKey: string) {
    setSelectedPrimaryKeys((current) => {
      const next = new Set(current);
      if (next.has(primaryKey)) {
        next.delete(primaryKey);
      } else {
        next.add(primaryKey);
      }
      return next;
    });
  }

  function clearClusterFilters() {
    setSelectedPrimaryKeys(new Set());
  }

  function updateClusterHue(clusterKey: string, hue: number) {
    setClusterHueByKey((current) => ({
      ...current,
      [clusterKey]: hue,
    }));
  }

  return (
    <main className="graph-fullscreen">
      <header className="graph-fullscreen-header">
        <div>
          <p className="eyebrow">Problem Graph</p>
          <h1>Solved question relationships</h1>
        </div>
          <Link href="/submission-history">Back to submission workbench</Link>
        </header>

      <section className="graph-workbench-shell">
        <aside className="graph-control-panel">
          <section className="graph-fullscreen-toolbar">
            <input
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Search in graph labels"
              aria-label="Search in graph"
            />
            <div className="graph-selected-meta">
              <span>{filteredGraph.nodes.length} problems</span>
              <span>{filteredGraph.edges.length} edges</span>
              <span>{selectedPrimaryKeys.size} primary filters</span>
              <span>{selectedNodeExists ? `Selected: ${selectedNodeExists.title}` : 'Select a node to focus'}</span>
            </div>
          </section>

          <section className="graph-cluster-filter-panel">
            <div className="graph-cluster-filter-header">
              <div>
                <p className="eyebrow">Cluster selector</p>
                <h2>Primary clusters</h2>
              </div>
              <button type="button" onClick={clearClusterFilters} disabled={!selectedPrimaryKeys.size}>
                Clear cluster filters
              </button>
            </div>
            <div className="graph-cluster-tree" role="list" aria-label="Primary cluster selector">
              {clusterTree.map((primary) => {
                const isPrimarySelected = selectedPrimaryKeys.has(primary.key);
                const hue = clusterHueByKey[primary.key] ?? defaultClusterHue(primary.key);

                return (
                  <section className="graph-cluster-branch" key={primary.key}>
                    <div
                      className={`graph-cluster-row primary ${isPrimarySelected ? 'selected' : ''}`}
                      onMouseEnter={() => setHoveredPrimaryKey(primary.key)}
                      onMouseLeave={() => setHoveredPrimaryKey((current) => (current === primary.key ? null : current))}
                    >
                      <label className="graph-cluster-toggle">
                        <input
                          type="checkbox"
                          checked={isPrimarySelected}
                          onChange={() => togglePrimary(primary.key)}
                        />
                        <span>{primary.label}</span>
                        <small>{primary.questionCount} questions</small>
                      </label>
                      <div className="graph-cluster-hue-control">
                        <span
                          className="graph-cluster-hue-swatch"
                          style={{ background: `hsl(${hue} 78% 52%)` }}
                          aria-hidden="true"
                        />
                        <input
                          type="range"
                          min={0}
                          max={360}
                          value={hue}
                          onChange={(event) => updateClusterHue(primary.key, Number(event.target.value))}
                          aria-label={`Adjust hue for ${primary.label}`}
                        />
                      </div>
                    </div>
                  </section>
                );
              })}
            </div>
          </section>
        </aside>

        <section className="graph-stage-panel">
          <SubmissionGraphView
            graph={filteredGraph}
            visiblePrimaryClusterKeys={selectedPrimaryKeys}
            clusterHueByKey={clusterHueByKey}
            hoveredPrimaryClusterKey={hoveredPrimaryKey}
            selectedNodeSlug={selectedNodeSlug}
            onNodeSelect={setSelectedNodeSlug}
          />
        </section>
      </section>
    </main>
  );
}
