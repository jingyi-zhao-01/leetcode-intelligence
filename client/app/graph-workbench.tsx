'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { SubmissionGraphView } from './submission-graph';
import { type SubmissionGraph } from '../lib/submission-graph';
import type { GraphSubmissionRow } from '../lib/data';

type Props = {
  submissions: GraphSubmissionRow[];
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
  selectedTemplateGroupKeys: Set<string>,
) {
  const hasTemplateGroupFilter = selectedTemplateGroupKeys.size > 0;

  if (!hasTemplateGroupFilter) {
    return true;
  }

  return node.templateGroups.some((group) => selectedTemplateGroupKeys.has(group.key));
}

function filterGraph(
  graph: SubmissionGraph,
  needle: string,
  selectedTemplateGroupKeys: Set<string>,
) {
  const filteredNodes = graph.nodes.filter((node) => {
    if (!matchesClusterSelection(node, selectedTemplateGroupKeys)) {
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

function buildClusterTree(submissions: GraphSubmissionRow[]): GraphClusterTree[] {
  const slugMembers = new Map<string, Map<string, string>>();

  for (const submission of submissions) {
    if (!submission.titleSlug) {
      continue;
    }

    const slug = submission.titleSlug.toLowerCase();
    const membership = slugMembers.get(slug) ?? new Map<string, string>();

    for (const tag of submission.tags) {
      if (tag.dimension !== 'template' || tag.kind !== 'tag' || !tag.parentKey) {
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
  const [selectedTemplateGroupKeys, setSelectedTemplateGroupKeys] = useState<Set<string>>(() => new Set());
  const [hoveredTemplateGroupKey, setHoveredTemplateGroupKey] = useState<string | null>(null);
  const templateGroupTree = useMemo(() => buildClusterTree(submissions), [submissions]);
  const [clusterHueByKey, setClusterHueByKey] = useState<Record<string, number>>(() =>
    Object.fromEntries(buildClusterTree(submissions).map((group) => [group.key, defaultClusterHue(group.key)])),
  );
  const filteredGraph = useMemo(
    () => filterGraph(graph, query.trim().toLowerCase(), selectedTemplateGroupKeys),
    [graph, query, selectedTemplateGroupKeys],
  );

  const selectedNodeExists = useMemo(() => {
    if (!selectedNodeSlug) {
      return null;
    }

    return filteredGraph.nodes.find((node) => node.slug === selectedNodeSlug) ?? null;
  }, [selectedNodeSlug, filteredGraph]);

  function toggleTemplateGroup(groupKey: string) {
    setSelectedTemplateGroupKeys((current) => {
      const next = new Set(current);
      if (next.has(groupKey)) {
        next.delete(groupKey);
      } else {
        next.add(groupKey);
      }
      return next;
    });
  }

  function clearTemplateGroupFilters() {
    setSelectedTemplateGroupKeys(new Set());
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
              <span>{selectedTemplateGroupKeys.size} template group filters</span>
              <span>{selectedNodeExists ? `Selected: ${selectedNodeExists.title}` : 'Select a node to focus'}</span>
            </div>
          </section>

          <section className="graph-cluster-filter-panel">
            <div className="graph-cluster-filter-header">
              <div>
                <p className="eyebrow">Template Group Selector</p>
                <h2>Template groups</h2>
              </div>
              <button type="button" onClick={clearTemplateGroupFilters} disabled={!selectedTemplateGroupKeys.size}>
                Clear template group filters
              </button>
            </div>
            <div className="graph-cluster-tree" role="list" aria-label="Template group selector">
              {templateGroupTree.map((group) => {
                const isGroupSelected = selectedTemplateGroupKeys.has(group.key);
                const hue = clusterHueByKey[group.key] ?? defaultClusterHue(group.key);

                return (
                  <section className="graph-cluster-branch" key={group.key}>
                    <div
                      className={`graph-cluster-row primary ${isGroupSelected ? 'selected' : ''}`}
                      onMouseEnter={() => setHoveredTemplateGroupKey(group.key)}
                      onMouseLeave={() => setHoveredTemplateGroupKey((current) => (current === group.key ? null : current))}
                    >
                      <label className="graph-cluster-toggle">
                        <input
                          type="checkbox"
                          checked={isGroupSelected}
                          onChange={() => toggleTemplateGroup(group.key)}
                        />
                        <span>{group.label}</span>
                        <small>{group.questionCount} questions</small>
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
                          onChange={(event) => updateClusterHue(group.key, Number(event.target.value))}
                          aria-label={`Adjust hue for ${group.label}`}
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
            visiblePrimaryClusterKeys={selectedTemplateGroupKeys}
            clusterHueByKey={clusterHueByKey}
            hoveredPrimaryClusterKey={hoveredTemplateGroupKey}
            selectedNodeSlug={selectedNodeSlug}
            onNodeSelect={setSelectedNodeSlug}
          />
        </section>
      </section>
    </main>
  );
}
