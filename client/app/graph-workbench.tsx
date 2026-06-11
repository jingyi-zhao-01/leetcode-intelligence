'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { SubmissionGraphView } from './submission-graph';
import { type SubmissionGraph } from '../lib/submission-graph';
import { Button } from './components/ui/button';
import { Input } from './components/ui/input';
import type { TemplateGroupCatalog } from '../lib/template-catalog';

type Props = {
  graph: SubmissionGraph;
  templateCatalog: TemplateGroupCatalog[];
  initialSelectedSlug?: string | null;
};

type GraphClusterDirectory = {
  key: string;
  label: string;
  uniqueQuestionCount: number;
  templateMatchCount: number;
  templates: Array<{
    key: string;
    label: string;
    questionCount: number;
  }>;
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

function buildClusterTree(graph: SubmissionGraph, templateCatalog: TemplateGroupCatalog[]): GraphClusterDirectory[] {
  const groupCounts = new Map<string, { label: string; slugs: Set<string> }>();
  const templateCounts = new Map<string, Set<string>>();

  for (const node of graph.nodes) {
    for (const group of node.templateGroups) {
      const entry = groupCounts.get(group.key) ?? {
        label: group.label,
        slugs: new Set<string>(),
      };
      entry.slugs.add(node.slug);
      groupCounts.set(group.key, entry);
    }

    for (const template of node.templateTags) {
      const entry = templateCounts.get(template.key) ?? new Set<string>();
      entry.add(node.slug);
      templateCounts.set(template.key, entry);
    }
  }

  return templateCatalog
    .map((group) => ({
      key: group.key,
      label: group.label,
      uniqueQuestionCount: groupCounts.get(group.key)?.slugs.size ?? 0,
      templateMatchCount: group.templates.reduce(
        (count, entry) => count + (templateCounts.get(entry.template.key)?.size ?? 0),
        0,
      ),
      templates: group.templates.map((entry) => ({
        key: entry.template.key,
        label: entry.template.label,
        questionCount: templateCounts.get(entry.template.key)?.size ?? 0,
      })),
    }))
    .sort(
      (left, right) =>
        right.uniqueQuestionCount - left.uniqueQuestionCount || left.label.localeCompare(right.label),
    );
}

export function GraphWorkbench({ graph, templateCatalog, initialSelectedSlug }: Props) {
  const [query, setQuery] = useState('');
  const [selectedNodeSlug, setSelectedNodeSlug] = useState<string | null>(initialSelectedSlug?.toLowerCase() ?? null);
  const [selectedTemplateGroupKeys, setSelectedTemplateGroupKeys] = useState<Set<string>>(() => new Set());
  const [selectedTemplateKey, setSelectedTemplateKey] = useState<string | null>(null);
  const [hoveredTemplateGroupKey, setHoveredTemplateGroupKey] = useState<string | null>(null);
  const templateGroupTree = useMemo(() => buildClusterTree(graph, templateCatalog), [graph, templateCatalog]);
  const [expandedTemplateGroupKeys, setExpandedTemplateGroupKeys] = useState<Set<string>>(
    () => new Set(templateCatalog.map((group) => group.key)),
  );
  const [clusterHueByKey, setClusterHueByKey] = useState<Record<string, number>>(() =>
    Object.fromEntries(buildClusterTree(graph, templateCatalog).map((group) => [group.key, defaultClusterHue(group.key)])),
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
    setSelectedTemplateKey(null);
  }

  function updateClusterHue(clusterKey: string, hue: number) {
    setClusterHueByKey((current) => ({
      ...current,
      [clusterKey]: hue,
    }));
  }

  function toggleTemplateGroupExpanded(groupKey: string) {
    setExpandedTemplateGroupKeys((current) => {
      const next = new Set(current);
      if (next.has(groupKey)) {
        next.delete(groupKey);
      } else {
        next.add(groupKey);
      }
      return next;
    });
  }

  function selectTemplateDirectoryEntry(groupKey: string, templateKey: string) {
    setSelectedTemplateKey(templateKey);
    setSelectedTemplateGroupKeys((current) => {
      const next = new Set(current);
      next.add(groupKey);
      return next;
    });
    setExpandedTemplateGroupKeys((current) => new Set(current).add(groupKey));
  }

  return (
    <main className="graph-fullscreen">
      <header className="graph-fullscreen-header">
        <div>
          <p className="eyebrow">Problem Graph</p>
          <h1>Solved question relationships</h1>
        </div>
          <Link href="/submission-history" className="ui-btn ui-btn-outline">
            Back to submission workbench
          </Link>
        </header>

      <section className="graph-workbench-shell">
        <aside className="graph-control-panel">
          <section className="graph-fullscreen-toolbar">
            <Input
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
              <Button type="button" variant="outline" onClick={clearTemplateGroupFilters} disabled={!selectedTemplateGroupKeys.size}>
                Clear template group filters
              </Button>
            </div>
            <div className="graph-cluster-tree" role="list" aria-label="Template group selector">
              {templateGroupTree.map((group) => {
                const isGroupSelected = selectedTemplateGroupKeys.has(group.key);
                const hue = clusterHueByKey[group.key] ?? defaultClusterHue(group.key);
                const isExpanded = expandedTemplateGroupKeys.has(group.key);

                return (
                  <section className="graph-cluster-branch" key={group.key}>
                    <div
                      className={`graph-cluster-row primary ${isGroupSelected ? 'selected' : ''}`}
                      onMouseEnter={() => setHoveredTemplateGroupKey(group.key)}
                      onMouseLeave={() => setHoveredTemplateGroupKey((current) => (current === group.key ? null : current))}
                    >
                      <button
                        type="button"
                        className="graph-cluster-expand"
                        onClick={() => toggleTemplateGroupExpanded(group.key)}
                        aria-expanded={isExpanded}
                        aria-controls={`graph-template-group-${group.key}`}
                      >
                        {isExpanded ? '▾' : '▸'}
                      </button>
                      <label className="graph-cluster-toggle">
                        <input
                          type="checkbox"
                          checked={isGroupSelected}
                          onChange={() => toggleTemplateGroup(group.key)}
                        />
                        <span className="graph-cluster-label-text">{group.label}</span>
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
                    <div className="graph-cluster-stats-row">
                      <small>
                        {group.uniqueQuestionCount} unique problems
                        {group.templateMatchCount > group.uniqueQuestionCount
                          ? ` · ${group.templateMatchCount} template matches`
                          : ''}
                      </small>
                    </div>
                    {isExpanded ? (
                      <div className="graph-template-tree" id={`graph-template-group-${group.key}`}>
                        {group.templates.map((template) => (
                          <button
                            key={`${group.key}:${template.key}`}
                            type="button"
                            className={`graph-template-leaf ${selectedTemplateKey === template.key ? 'selected' : ''}`}
                            onMouseEnter={() => setHoveredTemplateGroupKey(group.key)}
                            onMouseLeave={() =>
                              setHoveredTemplateGroupKey((current) => (current === group.key ? null : current))
                            }
                            onClick={() => selectTemplateDirectoryEntry(group.key, template.key)}
                          >
                            <span className="graph-template-leaf-branch" aria-hidden="true">
                              └
                            </span>
                            <span className="graph-template-leaf-label">{template.label}</span>
                            <small>{template.questionCount} questions</small>
                          </button>
                        ))}
                      </div>
                    ) : null}
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
