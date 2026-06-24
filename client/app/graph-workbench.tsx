'use client';

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

const GRAPH_GROUP_TONES = ['teal', 'blue', 'amber', 'purple', 'green'] as const;

function defaultClusterHue(key: string) {
  let hash = 0;
  for (let index = 0; index < key.length; index += 1) {
    hash = (hash * 31 + key.charCodeAt(index)) % 100000;
  }
  return 290 + (hash % 90);
}

function matchesClusterSelection(node: SubmissionGraph['nodes'][number], selectedTemplateGroupKeys: Set<string>) {
  const hasTemplateGroupFilter = selectedTemplateGroupKeys.size > 0;

  if (!hasTemplateGroupFilter) {
    return true;
  }

  return node.templateGroups.some((group) => selectedTemplateGroupKeys.has(group.key));
}

function filterGraph(graph: SubmissionGraph, needle: string, selectedTemplateGroupKeys: Set<string>) {
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
  const graphTemplatesByGroup = new Map<
    string,
    Map<
      string,
      {
        label: string;
        slugs: Set<string>;
      }
    >
  >();

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

      if (template.parentKey) {
        const groupTemplates = graphTemplatesByGroup.get(template.parentKey) ?? new Map();
        const groupTemplate = groupTemplates.get(template.key) ?? {
          label: template.label,
          slugs: new Set<string>(),
        };
        groupTemplate.slugs.add(node.slug);
        groupTemplates.set(template.key, groupTemplate);
        graphTemplatesByGroup.set(template.parentKey, groupTemplates);
      }
    }
  }

  const catalogGroupKeys = new Set(templateCatalog.map((group) => group.key));
  const catalogGroups = templateCatalog.map((group) => {
    const templatesByKey = new Map(
      group.templates.map((entry) => [
        entry.template.key,
        {
          key: entry.template.key,
          label: entry.template.label,
          questionCount: templateCounts.get(entry.template.key)?.size ?? 0,
        },
      ]),
    );
    const graphTemplates = graphTemplatesByGroup.get(group.key);

    for (const [templateKey, template] of graphTemplates?.entries() ?? []) {
      if (!templatesByKey.has(templateKey)) {
        templatesByKey.set(templateKey, {
          key: templateKey,
          label: template.label,
          questionCount: template.slugs.size,
        });
      }
    }

    const templates = [...templatesByKey.values()].sort(
      (left, right) => right.questionCount - left.questionCount || left.label.localeCompare(right.label),
    );

    return {
      key: group.key,
      label: group.label,
      uniqueQuestionCount: groupCounts.get(group.key)?.slugs.size ?? 0,
      templateMatchCount: templates.reduce((count, entry) => count + entry.questionCount, 0),
      templates,
    };
  });
  const graphOnlyGroups = [...groupCounts.entries()]
    .filter(([groupKey]) => !catalogGroupKeys.has(groupKey))
    .map(([groupKey, group]) => {
      const templates = [...(graphTemplatesByGroup.get(groupKey)?.entries() ?? [])]
        .map(([templateKey, template]) => ({
          key: templateKey,
          label: template.label,
          questionCount: template.slugs.size,
        }))
        .sort((left, right) => right.questionCount - left.questionCount || left.label.localeCompare(right.label));

      return {
        key: groupKey,
        label: group.label,
        uniqueQuestionCount: group.slugs.size,
        templateMatchCount: templates.reduce((count, entry) => count + entry.questionCount, 0),
        templates,
      };
    });

  return [...catalogGroups, ...graphOnlyGroups].sort(
    (left, right) => right.uniqueQuestionCount - left.uniqueQuestionCount || left.label.localeCompare(right.label),
  );
}

export function GraphWorkbench({ graph, templateCatalog, initialSelectedSlug }: Props) {
  const [query, setQuery] = useState('');
  const [selectedNodeSlug, setSelectedNodeSlug] = useState<string | null>(initialSelectedSlug?.toLowerCase() ?? null);
  const [selectedTemplateGroupKeys, setSelectedTemplateGroupKeys] = useState<Set<string>>(() => new Set());
  const [selectedTemplateKey, setSelectedTemplateKey] = useState<string | null>(null);
  const [hoveredTemplateGroupKey, setHoveredTemplateGroupKey] = useState<string | null>(null);
  const templateGroupTree = useMemo(() => buildClusterTree(graph, templateCatalog), [graph, templateCatalog]);
  const [clusterHueByKey, setClusterHueByKey] = useState<Record<string, number>>(() =>
    Object.fromEntries(
      buildClusterTree(graph, templateCatalog).map((group) => [group.key, defaultClusterHue(group.key)]),
    ),
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

  function selectTemplateDirectoryEntry(groupKey: string, templateKey: string) {
    setSelectedTemplateKey(templateKey);
    setSelectedTemplateGroupKeys((current) => {
      const next = new Set(current);
      next.add(groupKey);
      return next;
    });
  }

  return (
    <main className="graph-fullscreen">
      <header className="graph-page-header">
        <div>
          <p className="eyebrow">Graph Explorer</p>
          <h1>Problem Graph</h1>
          <p>Explore solved-question relationships through the current template taxonomy.</p>
        </div>
        <div className="graph-header-summary">
          <span>{graph.nodes.length} problems</span>
          <span>{graph.edges.length} edges</span>
          <span>{templateGroupTree.length} groups</span>
        </div>
      </header>

      <section className="graph-workbench-shell">
        <aside className="graph-control-panel">
          <section className="graph-fullscreen-toolbar">
            <div className="graph-search-stack">
              <p className="graph-panel-title">Template groups</p>
              <Input
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Filter nodes..."
                aria-label="Search in graph"
              />
            </div>
            <div className="graph-toolbar-summary">
              <span>
                {selectedTemplateGroupKeys.size ? `${selectedTemplateGroupKeys.size} selected` : 'All groups'}
              </span>
              {selectedTemplateGroupKeys.size ? (
                <Button type="button" variant="outline" onClick={clearTemplateGroupFilters}>
                  Clear
                </Button>
              ) : null}
            </div>
          </section>

          <section className="graph-cluster-filter-panel">
            <div className="graph-cluster-tree" role="list" aria-label="Template group selector">
              {templateGroupTree.map((group, groupIndex) => {
                const isGroupSelected = selectedTemplateGroupKeys.has(group.key);
                const tone = GRAPH_GROUP_TONES[groupIndex % GRAPH_GROUP_TONES.length];

                return (
                  <section
                    className={`graph-group-list-section graph-group-list-item-${tone} ${isGroupSelected ? 'selected' : ''}`}
                    key={group.key}
                    onMouseEnter={() => setHoveredTemplateGroupKey(group.key)}
                    onMouseLeave={() =>
                      setHoveredTemplateGroupKey((current) => (current === group.key ? null : current))
                    }
                  >
                    <button
                      type="button"
                      className={`graph-group-list-item ${isGroupSelected ? 'selected' : ''}`}
                      onClick={() => toggleTemplateGroup(group.key)}
                      aria-pressed={isGroupSelected}
                    >
                      <span className="graph-group-list-dot" aria-hidden="true" />
                      <span className="graph-group-list-label">{group.label}</span>
                      <span className="graph-group-list-count">{group.uniqueQuestionCount}</span>
                    </button>
                    {isGroupSelected ? (
                      <div className="graph-template-tree" role="list" aria-label={`${group.label} templates`}>
                        {group.templates.length ? (
                          group.templates.map((template) => (
                            <button
                              key={`${group.key}:${template.key}`}
                              type="button"
                              className={`graph-template-leaf ${selectedTemplateKey === template.key ? 'selected' : ''}`}
                              onClick={() => selectTemplateDirectoryEntry(group.key, template.key)}
                            >
                              <span className="graph-template-leaf-branch" aria-hidden="true">
                                └
                              </span>
                              <span className="graph-template-leaf-label">{template.label}</span>
                              <small>{template.questionCount}</small>
                            </button>
                          ))
                        ) : (
                          <p className="graph-template-empty">No templates in this group yet</p>
                        )}
                      </div>
                    ) : null}
                  </section>
                );
              })}
            </div>
          </section>
        </aside>

        <section className="graph-stage-panel">
          <div className="graph-stage-header">
            <span>{filteredGraph.nodes.length} problems</span>
            <span>{filteredGraph.edges.length} connections</span>
            <span>{selectedNodeExists ? `Focus: ${selectedNodeExists.title}` : 'No focused node'}</span>
          </div>
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
