'use client';

import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { GraphData, Node, Edge } from '@/types/api';
import ProblemHoverCard from './ProblemHoverCard';

interface ForceGraphProps {
  data: GraphData;
  onNodeClick: (node: Node) => void;
}

interface SimulationNode extends Node, d3.SimulationNodeDatum {}
interface SimulationLink extends d3.SimulationLinkDatum<SimulationNode> {
  source: SimulationNode | number;
  target: SimulationNode | number;
  type: string;
  sharedTags?: number;
}

export default function ForceGraph({ data, onNodeClick }: ForceGraphProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const simulationRef = useRef<d3.Simulation<SimulationNode, SimulationLink> | null>(null);
  const [hoveredNode, setHoveredNode] = useState<{ node: Node; x: number; y: number } | null>(null);
  const hoverTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (!svgRef.current || !data.nodes.length) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll('*').remove(); // Clear previous render

    const width = svgRef.current.clientWidth;
    const height = svgRef.current.clientHeight;

    // Create simulation nodes and links
    const nodes: SimulationNode[] = data.nodes.map(d => ({ ...d }));
    const links: SimulationLink[] = data.edges.map(d => ({
      source: d.source,
      target: d.target,
      type: d.type,
      sharedTags: d.sharedTags,
    }));

    // Initialize D3 force simulation
    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink<SimulationNode, SimulationLink>(links)
        .id(d => d.id)
        .distance(d => (d as SimulationLink).type === 'explicit' ? 120 : 200)
        .strength(d => (d as SimulationLink).type === 'explicit' ? 0.8 : 0.05))
      .force('charge', d3.forceManyBody().strength(-200))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collide', d3.forceCollide().radius(25));

    simulationRef.current = simulation;

    // TODO: Implement centralizing logic for solved problems

    // Create container group
    const g = svg.append('g');

    // Add zoom behavior
    const zoom = d3.zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.1, 10])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      });

    svg.call(zoom);

    // Draw edges (explicit edges first so they appear below tag edges in rendering order)
    const link = g.append('g')
      .selectAll('line')
      .data(links.sort((a, b) => a.type === 'explicit' ? -1 : 1))
      .join('line')
      .attr('stroke', d => d.type === 'explicit' ? '#3b82f6' : '#9ca3af')
      .attr('stroke-width', d => d.type === 'explicit' ? 3 : 0.5)
      .attr('stroke-opacity', d => d.type === 'explicit' ? 0.8 : 0.2)
      .attr('stroke-dasharray', d => d.type === 'explicit' ? '0' : '3,3');

    // Draw nodes
    const node = g.append('g')
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', 8)
      .attr('fill', d => {
        if (!d.solved) return '#d1d5db';
        // Basic color by difficulty for now (will add acceptance rate gradient later)
        if (d.difficulty === 'Easy') return '#86efac';
        if (d.difficulty === 'Medium') return '#fde047';
        return '#fca5a5';
      })
      .attr('stroke', d => {
        if (d.difficulty === 'Easy') return '#22c55e';
        if (d.difficulty === 'Medium') return '#f97316';
        return '#ef4444';
      })
      .attr('stroke-width', 2)
      .style('cursor', 'pointer')
      .call(d3.drag<SVGCircleElement, SimulationNode>()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended) as any);

    // Add click handler
    node.on('click', (event, d) => {
      event.stopPropagation();
      onNodeClick(d);
    });

    // Add hover handlers
    node.on('mouseenter', (event, d) => {
      // Clear any existing timeout
      if (hoverTimeoutRef.current) {
        clearTimeout(hoverTimeoutRef.current);
      }
      
      // Show hover card after a short delay
      hoverTimeoutRef.current = setTimeout(() => {
        const rect = svgRef.current?.getBoundingClientRect();
        if (rect) {
          setHoveredNode({
            node: d,
            x: rect.left + (d.x || 0),
            y: rect.top + (d.y || 0),
          });
        }
      }, 300); // 300ms delay before showing
    });

    node.on('mouseleave', () => {
      // Clear timeout if mouse leaves before delay completes
      if (hoverTimeoutRef.current) {
        clearTimeout(hoverTimeoutRef.current);
        hoverTimeoutRef.current = null;
      }
    });

    // Add tooltips
    node.append('title')
      .text(d => `${d.title}\\nDifficulty: ${d.difficulty}\\nAcceptance: ${d.acceptanceRate}%`);

    // Update positions on simulation tick
    simulation.on('tick', () => {
      link
        .attr('x1', d => (d.source as SimulationNode).x!)
        .attr('y1', d => (d.source as SimulationNode).y!)
        .attr('x2', d => (d.target as SimulationNode).x!)
        .attr('y2', d => (d.target as SimulationNode).y!);

      node
        .attr('cx', d => d.x!)
        .attr('cy', d => d.y!);
    });

    // Drag functions
    function dragstarted(event: d3.D3DragEvent<SVGCircleElement, SimulationNode, SimulationNode>, d: SimulationNode) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event: d3.D3DragEvent<SVGCircleElement, SimulationNode, SimulationNode>, d: SimulationNode) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event: d3.D3DragEvent<SVGCircleElement, SimulationNode, SimulationNode>, d: SimulationNode) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }

    // Cleanup
    return () => {
      simulation.stop();
      if (hoverTimeoutRef.current) {
        clearTimeout(hoverTimeoutRef.current);
      }
    };
  }, [data, onNodeClick]);

  return (
    <>
      <svg
        ref={svgRef}
        className="w-full h-full border border-gray-300"
        style={{ minHeight: '600px' }}
      />
      
      {/* Hover Card */}
      {/* {hoveredNode && (
        <ProblemHoverCard
          node={hoveredNode.node}
          position={{ x: hoveredNode.x, y: hoveredNode.y }}
          onClose={() => setHoveredNode(null)}
        />
      )} */}
    </>
  );
}
