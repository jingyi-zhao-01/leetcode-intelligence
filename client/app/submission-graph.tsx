'use client';

import {
  forceCenter,
  forceCollide,
  forceLink,
  forceManyBody,
  forceSimulation,
  forceX,
  forceY,
  type Force,
  type SimulationLinkDatum,
  type SimulationNodeDatum,
} from 'd3-force';
import { useEffect, useMemo, useRef, useState, type CSSProperties, type WheelEvent } from 'react';
import { type SubmissionGraph, type SubmissionGraphNode } from '../lib/submission-graph';

type TemplateCluster = {
  id: string;
  kind: 'template-group';
  key: string;
  label: string;
  nodeIds: string[];
};

type TemplateClusterEnvelope = TemplateCluster & {
  x: number;
  y: number;
  width: number;
  height: number;
  labelX: number;
  labelY: number;
  labelWidth: number;
  labelHeight: number;
};

type LiveGraphNode = SubmissionGraphNode &
  SimulationNodeDatum & {
    x: number;
    y: number;
  };

type LiveGraphLink = SimulationLinkDatum<LiveGraphNode> & {
  id: string;
  source: string | LiveGraphNode;
  target: string | LiveGraphNode;
};

function hashValue(value: string) {
  let hash = 0;
  for (let i = 0; i < value.length; i += 1) {
    hash = (hash * 31 + value.charCodeAt(i)) % 100000;
  }
  return hash;
}

function paletteColor(kind: TemplateCluster['kind'], key: string, hueOverride?: number) {
  const hue = String(hueOverride ?? 290 + (hashValue(key) % 90));
  return {
    stroke: `hsl(${hue} 74% 40% / 0.95)`,
    fill: `hsl(${hue} 78% 60% / 0.06)`,
    text: `hsl(${hue} 75% 28% / 0.95)`,
  };
}

function nodeRadius(node: SubmissionGraphNode) {
  return node.connectionCount > 0 ? 20 : 16;
}

function buildLiveNode(node: SubmissionGraphNode): LiveGraphNode {
  return {
    ...node,
    x: node.x,
    y: node.y,
    vx: 0,
    vy: 0,
  };
}

function createMembershipForce(
  membershipsForNode: (node: LiveGraphNode) => string[],
  strength: number,
): Force<LiveGraphNode, LiveGraphLink> {
  let nodes: LiveGraphNode[] = [];

  const force = ((alpha: number) => {
    const centers = new Map<string, { x: number; y: number; count: number }>();

    for (const node of nodes) {
      for (const membership of membershipsForNode(node)) {
        const center = centers.get(membership) ?? { x: 0, y: 0, count: 0 };
        center.x += node.x;
        center.y += node.y;
        center.count += 1;
        centers.set(membership, center);
      }
    }

    for (const center of centers.values()) {
      if (center.count > 0) {
        center.x /= center.count;
        center.y /= center.count;
      }
    }

    for (const node of nodes) {
      const memberships = membershipsForNode(node);
      if (!memberships.length) {
        continue;
      }

      let targetX = 0;
      let targetY = 0;
      let count = 0;

      for (const membership of memberships) {
        const center = centers.get(membership);
        if (!center || center.count < 2) {
          continue;
        }
        targetX += center.x;
        targetY += center.y;
        count += 1;
      }

      if (!count) {
        continue;
      }

      targetX /= count;
      targetY /= count;
      node.vx = (node.vx ?? 0) + (targetX - node.x) * strength * alpha;
      node.vy = (node.vy ?? 0) + (targetY - node.y) * strength * alpha;
    }
  }) as Force<LiveGraphNode, LiveGraphLink>;

  force.initialize = (forceNodes) => {
    nodes = forceNodes as LiveGraphNode[];
  };

  return force;
}

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
        : '#7f8a9c';
}

export function SubmissionGraphView({
  graph,
  visiblePrimaryClusterKeys,
  clusterHueByKey,
  selectedNodeSlug,
  onNodeSelect,
}: {
  graph: SubmissionGraph;
  visiblePrimaryClusterKeys: Set<string>;
  clusterHueByKey: Record<string, number>;
  selectedNodeSlug: string | null;
  onNodeSelect: (slug: string) => void;
}) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const frameRef = useRef<number | null>(null);
  const [layoutNodes, setLayoutNodes] = useState<LiveGraphNode[]>(() => graph.nodes.map(buildLiveNode));
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const selectedCount = selectedNodeSlug ? 1 : 0;
  const hasOrphanNodes = layoutNodes.some((node) => node.connectionCount === 0);
  const canvasWidth = graph.canvasWidth;
  const canvasHeight = graph.canvasHeight;
  const zoomStep = 1.18;

  const graphCenter = useMemo(
    () => ({
      x: canvasWidth / 2,
      y: canvasHeight / 2,
    }),
    [canvasHeight, canvasWidth],
  );

  useEffect(() => {
    const nodes = graph.nodes.map(buildLiveNode);
    const links: LiveGraphLink[] = graph.edges.map((edge) => ({ ...edge }));
    const nodeById = new Map(nodes.map((node) => [node.id, node]));
    const resolveNode = (value: string | LiveGraphNode) => {
      return typeof value === 'string' ? nodeById.get(value) ?? null : value;
    };

    setLayoutNodes(nodes);

    const simulation = forceSimulation<LiveGraphNode>(nodes)
      .force('charge', forceManyBody().strength(-320))
      .force(
        'link',
        forceLink<LiveGraphNode, LiveGraphLink>(links)
          .id((node) => node.id)
          .distance((edge) => {
            const source = resolveNode(edge.source);
            const target = resolveNode(edge.target);
            if (!source || !target) {
              return 190;
            }
            return 170 + Math.min(source.attempts + target.attempts, 5) * 10;
          })
          .strength(0.24),
      )
      .force('collide', forceCollide<LiveGraphNode>().radius((node) => nodeRadius(node) + 28).strength(0.9))
      .force('center', forceCenter(canvasWidth / 2, canvasHeight / 2))
      .force('x', forceX(canvasWidth / 2).strength(0.018))
      .force('y', forceY(canvasHeight / 2).strength(0.018))
      .force(
        'template-groups',
        createMembershipForce(
          (node) => node.templateGroups.map((group) => `group:${group.key}`),
          0.12,
        ),
      )
      .alpha(0.85)
      .alphaDecay(0.02)
      .velocityDecay(0.32);

    simulation.on('tick', () => {
      if (frameRef.current !== null) {
        return;
      }

      frameRef.current = window.requestAnimationFrame(() => {
        frameRef.current = null;
        setLayoutNodes(nodes.map((node) => ({ ...node })));
      });
    });

    return () => {
      simulation.stop();
      if (frameRef.current !== null) {
        window.cancelAnimationFrame(frameRef.current);
        frameRef.current = null;
      }
    };
  }, [canvasHeight, canvasWidth, graph.edges, graph.nodes]);

  const nodeById = useMemo(() => new Map(layoutNodes.map((node) => [node.id, node])), [layoutNodes]);

  const clusters = useMemo(() => {
    const clusterMap = new Map<string, TemplateCluster>();

    for (const node of layoutNodes) {
      for (const templateGroup of node.templateGroups) {
        if (!visiblePrimaryClusterKeys.has(templateGroup.key)) {
          continue;
        }
        const key = `template-group:${templateGroup.key}`;
        const cluster = clusterMap.get(key);
        if (cluster) {
          cluster.nodeIds.push(node.id);
          continue;
        }
        clusterMap.set(key, {
          id: key,
          kind: 'template-group',
          key: templateGroup.key,
          label: templateGroup.label,
          nodeIds: [node.id],
        });
      }
    }

    const envelopes: TemplateClusterEnvelope[] = [];
    const padding = 20;
    const labelOffsetY = 12;

    for (const cluster of clusterMap.values()) {

      let minX = Number.POSITIVE_INFINITY;
      let minY = Number.POSITIVE_INFINITY;
      let maxX = Number.NEGATIVE_INFINITY;
      let maxY = Number.NEGATIVE_INFINITY;
      let hasNode = false;

      for (const nodeId of cluster.nodeIds) {
        const node = nodeById.get(nodeId);
        if (!node) continue;
        const radius = nodeRadius(node) + 20;
        minX = Math.min(minX, node.x - radius);
        minY = Math.min(minY, node.y - radius);
        maxX = Math.max(maxX, node.x + radius);
        maxY = Math.max(maxY, node.y + radius);
        hasNode = true;
      }

      if (!hasNode) {
        continue;
      }

      envelopes.push({
        ...cluster,
        x: minX - padding,
        y: minY - padding - 14,
        width: maxX - minX + padding * 2,
        height: maxY - minY + padding * 2 + 14,
        labelX: minX - padding + 10,
        labelY: minY - padding - labelOffsetY,
        labelWidth: Math.min(320, Math.max(160, 12 + cluster.label.length * 6)),
        labelHeight: 22,
      });
    }

    return envelopes.sort((left, right) => {
      if (left.nodeIds.length !== right.nodeIds.length) {
        return right.nodeIds.length - left.nodeIds.length;
      }
      return left.label.localeCompare(right.label);
    });
  }, [layoutNodes, nodeById, visiblePrimaryClusterKeys]);

  function applyZoom(nextZoom: number, focalPoint?: { x: number; y: number }) {
    const clampedZoom = Math.min(2.5, Math.max(0.5, nextZoom));
    const focus = focalPoint ?? graphCenter;
    setPan((currentPan) => {
      const graphPointX = (focus.x - currentPan.x) / zoom;
      const graphPointY = (focus.y - currentPan.y) / zoom;
      return {
        x: focus.x - graphPointX * clampedZoom,
        y: focus.y - graphPointY * clampedZoom,
      };
    });
    setZoom(clampedZoom);
  }

  function handleWheel(event: WheelEvent<SVGSVGElement>) {
    event.preventDefault();
    const rect = svgRef.current?.getBoundingClientRect();
    const point = rect
      ? {
          x: event.clientX - rect.left,
          y: event.clientY - rect.top,
        }
      : graphCenter;
    const direction = event.deltaY < 0 ? 1 : -1;
    applyZoom(zoom * (direction > 0 ? zoomStep : 1 / zoomStep), point);
  }

  function resetView() {
    setZoom(1);
    setPan({ x: 0, y: 0 });
  }

  return (
    <section className="graph-view">
      <div className="graph-toolbar">
        <div className="graph-zoom-controls">
          <button type="button" onClick={() => applyZoom(zoom * zoomStep)} aria-label="Zoom in">
            +
          </button>
          <button type="button" onClick={() => applyZoom(zoom / zoomStep)} aria-label="Zoom out">
            -
          </button>
          <button type="button" onClick={resetView} aria-label="Reset zoom">
            Reset
          </button>
        </div>
        <span className="graph-zoom-readout">Zoom {Math.round(zoom * 100)}%</span>
      </div>
      <div className="graph-summary">
        <p>
          {graph.nodes.length} problems, {graph.edges.length} edges,{' '}
          {graph.nodes.length > 0 ? graph.nodes.reduce((acc, node) => acc + node.attempts, 0) : 0} total accepted attempts
        </p>
        <p>{selectedCount ? 'One selected question in list' : 'Click a node to focus on a question in this graph'}</p>
      </div>
      <div className="graph-legend" role="note" aria-label="Node color legend">
        <span className="graph-legend-title">Node colors</span>
        <span className="graph-legend-item">
          <span className="graph-legend-dot node-color-easy" />
          Easy
        </span>
        <span className="graph-legend-item">
          <span className="graph-legend-dot node-color-medium" />
          Medium
        </span>
        <span className="graph-legend-item">
          <span className="graph-legend-dot node-color-hard" />
          Hard
        </span>
        <span className="graph-legend-item">
          <span className="graph-legend-dot node-color-unknown" />
          Unknown
        </span>
        <span className="graph-legend-item">
          <span className="graph-legend-cross">✕</span>
          No related-problem links
        </span>
      </div>
      {hasOrphanNodes ? <p className="orphan-note">Some problems are isolated because related-problem links were not available.</p> : null}

      <div className="graph-canvas-shell">
        <svg
          ref={svgRef}
          className="submission-graph"
          width={canvasWidth}
          height={canvasHeight}
          viewBox={`0 0 ${canvasWidth} ${canvasHeight}`}
          role="img"
          aria-label="Solved problems relationship graph"
          onWheel={handleWheel}
        >
          <g transform={`translate(${pan.x} ${pan.y}) scale(${zoom})`}>
            <g className="graph-cluster-layer">
              {clusters.map((cluster) => {
                const colors = paletteColor(cluster.kind, cluster.key, clusterHueByKey[cluster.key]);
                return (
                  <g key={`cluster-${cluster.id}`} className="graph-cluster-group">
                    <rect
                      x={cluster.x}
                      y={cluster.y}
                      width={cluster.width}
                      height={cluster.height}
                      className={`graph-cluster ${cluster.kind}`}
                      style={
                        {
                          '--cluster-stroke': colors.stroke,
                          '--cluster-fill': colors.fill,
                          '--cluster-text': colors.text,
                        } as CSSProperties
                      }
                    />
                    <g transform={`translate(${cluster.labelX} ${cluster.labelY})`}>
                      <rect
                        x={0}
                        y={0}
                        width={cluster.labelWidth}
                        height={cluster.labelHeight}
                        rx={8}
                        ry={8}
                        className={`graph-cluster-label-bg ${cluster.kind}`}
                        style={
                          {
                            '--cluster-stroke': colors.stroke,
                            '--cluster-fill': colors.fill,
                            '--cluster-text': colors.text,
                          } as CSSProperties
                        }
                      />
                      <text x={10} y={15} className={`graph-cluster-label ${cluster.kind}`}>
                        Template Group: {cluster.label}
                      </text>
                    </g>
                  </g>
                );
              })}
            </g>
            <g>
              {graph.edges.map((edge) => {
                const source = nodeById.get(edge.source);
                const target = nodeById.get(edge.target);
                if (!source || !target) return null;

                return <line key={edge.id} x1={source.x} y1={source.y} x2={target.x} y2={target.y} className="graph-edge" />;
              })}
            </g>
            <g>
              {layoutNodes.map((node) => {
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
                    <circle
                      cx={node.x}
                      cy={node.y}
                      r={node.connectionCount > 0 ? 20 : 16}
                      fill={nodeColor(node)}
                      className="node-circle"
                    />
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
          </g>
        </svg>
      </div>
    </section>
  );
}
