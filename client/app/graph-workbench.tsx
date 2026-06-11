'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { SubmissionGraphView } from './submission-graph';
import { buildSubmissionGraph, type SubmissionGraph } from '../lib/submission-graph';
import type { SubmissionRow } from '../lib/data';

type Props = {
  submissions: SubmissionRow[];
  initialSelectedSlug?: string | null;
};

function filterGraph(graph: SubmissionGraph, needle: string) {
  if (!needle) {
    return graph;
  }

  const filteredNodes = graph.nodes.filter((node) => {
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

export function GraphWorkbench({ submissions, initialSelectedSlug }: Props) {
  const [query, setQuery] = useState('');
  const [selectedNodeSlug, setSelectedNodeSlug] = useState<string | null>(initialSelectedSlug?.toLowerCase() ?? null);
  const questionGraph = useMemo(() => buildSubmissionGraph(submissions), [submissions]);
  const filteredGraph = useMemo(() => filterGraph(questionGraph, query.trim().toLowerCase()), [query, questionGraph]);

  const selectedNodeExists = useMemo(() => {
    if (!selectedNodeSlug) {
      return null;
    }

    return filteredGraph.nodes.find((node) => node.slug === selectedNodeSlug) ?? null;
  }, [selectedNodeSlug, filteredGraph]);

  return (
    <main className="graph-fullscreen">
      <header className="graph-fullscreen-header">
        <div>
          <p className="eyebrow">Problem Graph</p>
          <h1>Solved question relationships</h1>
        </div>
        <Link href="/">Back to submission workbench</Link>
      </header>

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
          <span>{selectedNodeExists ? `Selected: ${selectedNodeExists.title}` : 'Select a node to focus'}</span>
        </div>
      </section>

      <section className="graph-fullscreen-canvas">
        <SubmissionGraphView
          graph={filteredGraph}
          selectedNodeSlug={selectedNodeSlug}
          onNodeSelect={setSelectedNodeSlug}
        />
      </section>
    </main>
  );
}
