'use client';

import {
  forceCenter,
  forceCollide,
  forceLink,
  forceManyBody,
  forceSimulation,
  forceX,
  forceY,
  type SimulationLinkDatum,
  type SimulationNodeDatum,
} from 'd3-force';
import { useEffect, useMemo, useRef, useState, type CSSProperties, type PointerEvent } from 'react';
import { type SubmissionGraph, type SubmissionGraphNode } from '../lib/submission-graph';
import {
  buildPrimaryClusterAnchors,
  createPrimaryClusterForce,
  createSharedTemplateGroupForce,
  buildVisibleTemplateGroupEnvelopes,
} from '../lib/submission-graph-layout';
import { Button } from './components/ui/button';

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

function paletteColor(kind: 'template-group', key: string, hueOverride?: number) {
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
  hoveredPrimaryClusterKey,
  selectedNodeSlug,
  onNodeSelect,
}: {
  graph: SubmissionGraph;
  visiblePrimaryClusterKeys: Set<string>;
  clusterHueByKey: Record<string, number>;
  hoveredPrimaryClusterKey: string | null;
  selectedNodeSlug: string | null;
  onNodeSelect: (slug: string) => void;
}) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const frameRef = useRef<number | null>(null);
  const [layoutNodes, setLayoutNodes] = useState<LiveGraphNode[]>(() => graph.nodes.map(buildLiveNode));
  const [hoveredClusterFromGraph, setHoveredClusterFromGraph] = useState<string | null>(null);
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const [panMode, setPanMode] = useState(false);
  const [isPanning, setIsPanning] = useState(false);
  const dragStateRef = useRef<{
    pointerId: number;
    startClientX: number;
    startClientY: number;
    startPanX: number;
    startPanY: number;
  } | null>(null);
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
    const primaryClusterAnchors = buildPrimaryClusterAnchors(nodes, canvasWidth, canvasHeight);
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
      .force('primary-template-group', createPrimaryClusterForce(primaryClusterAnchors, 0.18))
      .force('shared-template-groups', createSharedTemplateGroupForce(primaryClusterAnchors, 0.1))
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
  const effectiveHoveredPrimaryClusterKey = hoveredClusterFromGraph ?? hoveredPrimaryClusterKey;

  const clusters = useMemo(() => {
    return buildVisibleTemplateGroupEnvelopes(layoutNodes, visiblePrimaryClusterKeys, nodeRadius);
  }, [layoutNodes, visiblePrimaryClusterKeys]);

  const highlightedNodeIds = useMemo(() => {
    if (!effectiveHoveredPrimaryClusterKey) {
      return null;
    }

    return new Set(
      layoutNodes
        .filter((node) => node.templateGroups.some((group) => group.key === effectiveHoveredPrimaryClusterKey))
        .map((node) => node.id),
    );
  }, [effectiveHoveredPrimaryClusterKey, layoutNodes]);

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

  function handleCanvasPointerDown(event: PointerEvent<SVGSVGElement>) {
    if (!panMode) {
      return;
    }

    const target = event.target as Element | null;
    if (target?.closest('.graph-node') || target?.closest('.graph-cluster-group')) {
      return;
    }

    event.preventDefault();
    dragStateRef.current = {
      pointerId: event.pointerId,
      startClientX: event.clientX,
      startClientY: event.clientY,
      startPanX: pan.x,
      startPanY: pan.y,
    };
    setIsPanning(true);
    svgRef.current?.setPointerCapture(event.pointerId);
  }

  function handleCanvasPointerMove(event: PointerEvent<SVGSVGElement>) {
    const dragState = dragStateRef.current;
    if (!dragState || dragState.pointerId !== event.pointerId) {
      return;
    }

    const deltaX = event.clientX - dragState.startClientX;
    const deltaY = event.clientY - dragState.startClientY;
    setPan({
      x: dragState.startPanX + deltaX,
      y: dragState.startPanY + deltaY,
    });
  }

  function stopPanning(pointerId?: number) {
    const activePointerId = pointerId ?? dragStateRef.current?.pointerId;
    if (activePointerId !== undefined) {
      svgRef.current?.releasePointerCapture(activePointerId);
    }
    dragStateRef.current = null;
    setIsPanning(false);
  }

  function resetView() {
    setZoom(1);
    setPan({ x: 0, y: 0 });
  }

  return (
    <section className="graph-view">
      <div className="graph-toolbar">
        <div className="graph-zoom-controls">
          <Button type="button" variant="outline" size="icon" onClick={() => applyZoom(zoom * zoomStep)} aria-label="Zoom in">
            +
          </Button>
          <Button type="button" variant="outline" size="icon" onClick={() => applyZoom(zoom / zoomStep)} aria-label="Zoom out">
            -
          </Button>
          <Button type="button" variant="outline" onClick={resetView} aria-label="Reset zoom">
            Reset
          </Button>
          <Button
            type="button"
            variant="outline"
            onClick={() => setPanMode((current) => !current)}
            className={panMode ? 'active' : ''}
            aria-pressed={panMode}
            aria-label="Toggle pan mode"
          >
            Pan
          </Button>
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
          className={`submission-graph ${panMode ? 'pan-enabled' : ''} ${isPanning ? 'panning' : ''}`.trim()}
          width={canvasWidth}
          height={canvasHeight}
          viewBox={`0 0 ${canvasWidth} ${canvasHeight}`}
          role="img"
          aria-label="Solved problems relationship graph"
          onPointerDown={handleCanvasPointerDown}
          onPointerMove={handleCanvasPointerMove}
          onPointerUp={(event) => stopPanning(event.pointerId)}
          onPointerCancel={(event) => stopPanning(event.pointerId)}
          onPointerLeave={() => {
            if (!dragStateRef.current) {
              return;
            }
            stopPanning();
          }}
        >
          <g transform={`translate(${pan.x} ${pan.y}) scale(${zoom})`}>
            <g className="graph-cluster-layer">
              {clusters.map((cluster) => {
                const colors = paletteColor(cluster.kind, cluster.key, clusterHueByKey[cluster.key]);
                const isClusterHighlighted =
                  !effectiveHoveredPrimaryClusterKey || cluster.key === effectiveHoveredPrimaryClusterKey;
                return (
                  <g
                    key={`cluster-${cluster.id}`}
                    className={`graph-cluster-group ${isClusterHighlighted ? '' : 'dimmed'}`.trim()}
                    onMouseEnter={() => setHoveredClusterFromGraph(cluster.key)}
                    onMouseLeave={() => setHoveredClusterFromGraph((current) => (current === cluster.key ? null : current))}
                  >
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

                 const isHighlightedEdge =
                  !highlightedNodeIds || (highlightedNodeIds.has(source.id) && highlightedNodeIds.has(target.id));

                return (
                  <line
                    key={edge.id}
                    x1={source.x}
                    y1={source.y}
                    x2={target.x}
                    y2={target.y}
                    className={`graph-edge ${isHighlightedEdge ? '' : 'dimmed'}`.trim()}
                  />
                );
              })}
            </g>
            <g>
              {layoutNodes.map((node) => {
                const isSelected = selectedNodeSlug === node.slug;
                const isHighlightedNode = !highlightedNodeIds || highlightedNodeIds.has(node.id);
                const classes = [
                  'graph-node',
                  isSelected ? 'selected' : '',
                  selectedCount && !isSelected ? 'dim' : '',
                  !isHighlightedNode ? 'cluster-dim' : '',
                ]
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
                    <text
                      x={node.x}
                      y={node.y + 34}
                      className={`graph-node-label ${isHighlightedNode ? 'cluster-highlight' : 'cluster-dim'}`.trim()}
                    >
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
