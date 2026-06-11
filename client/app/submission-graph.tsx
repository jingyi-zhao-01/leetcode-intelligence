'use client';

import { type SubmissionGraph, type SubmissionGraphNode } from '../lib/submission-graph';

function nodeColor(node: SubmissionGraphNode) {
  const difficulty = node.difficulty?.toLowerCase();
  const low = difficulty === 'easy' ? '#2e8c7d' : 'transparent';
  const medium = difficulty === 'medium' ? '#2e638b' : 'transparent';
  const high = difficulty === 'hard' ? '#b24f5d' : 'transparent';
  return difficulty === 'easy'
    ? low
    : difficulty === 'medium'
      ? medium
      : difficulty === 'hard'
        ? high
        : '#3457a6';
}

export function SubmissionGraphView({
  graph,
  selectedNodeSlug,
  onNodeSelect,
}: {
  graph: SubmissionGraph;
  selectedNodeSlug: string | null;
  onNodeSelect: (slug: string) => void;
}) {
  const selectedCount = selectedNodeSlug ? 1 : 0;
  const hasOrphanNodes = graph.nodes.some((node) => node.connectionCount === 0);
  const canvasWidth = 760;
  const canvasHeight = 520;

  return (
    <section className="graph-view">
      <div className="graph-summary">
        <p>
          {graph.nodes.length} problems, {graph.edges.length} edges,{' '}
          {graph.nodes.length > 0 ? graph.nodes.reduce((acc, node) => acc + node.attempts, 0) : 0} total accepted attempts
        </p>
        <p>{selectedCount ? 'One selected question in list' : 'Click a node to focus on a question in this graph'}</p>
      </div>
      {hasOrphanNodes ? <p className="orphan-note">Some problems are isolated because related-problem links were not available.</p> : null}

      <svg
        className="submission-graph"
        viewBox={`0 0 ${canvasWidth} ${canvasHeight}`}
        role="img"
        aria-label="Solved problems relationship graph"
      >
        <g>
          {graph.edges.map((edge) => {
            const source = graph.nodes.find((node) => node.id === edge.source);
            const target = graph.nodes.find((node) => node.id === edge.target);
            if (!source || !target) return null;

            return <line key={edge.id} x1={source.x} y1={source.y} x2={target.x} y2={target.y} className="graph-edge" />;
          })}
        </g>
        <g>
          {graph.nodes.map((node) => {
            const isSelected = selectedNodeSlug === node.slug;
            const classes = ['graph-node', isSelected ? 'selected' : '', selectedCount && !isSelected ? 'dim' : '']
              .filter(Boolean)
              .join(' ');

            return (
              <g
                key={node.id}
                className={classes}
                role="button"
                tabIndex={0}
                onClick={() => onNodeSelect(node.slug)}
                onKeyDown={(event) => {
                  if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    onNodeSelect(node.slug);
                  }
                }}
              >
                <circle cx={node.x} cy={node.y} r={node.connectionCount > 0 ? 20 : 16} fill={nodeColor(node)} className="node-circle" />
                <text x={node.x} y={node.y + 34} className="graph-node-label">
                  {`${node.title.length > 28 ? `${node.title.slice(0, 26)}...` : node.title}`}
                </text>
                <title>
                  {`${node.title} · ${node.slug} · ${node.difficulty ?? 'unknown'} · attempts ${node.attempts}`}
                </title>
                {node.connectionCount === 0 ? (
                  <line x1={node.x - 8} y1={node.y - 8} x2={node.x + 8} y2={node.y + 8} className="graph-node-cross" />
                ) : null}
              </g>
            );
          })}
        </g>
      </svg>
    </section>
  );
}
