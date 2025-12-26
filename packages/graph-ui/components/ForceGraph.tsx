'use client';

import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { GraphData, Node, Edge } from '@/types/api';
import ProblemHoverCard from './ProblemHoverCard';
import { renderSector, updateSectorStyle, SectorData } from './Sector.tsx';

interface ForceGraphProps {
  data: GraphData;
  onNodeClick: (node: Node) => void;
  selectedSectors?: string[];
}

interface SimulationNode extends Node, d3.SimulationNodeDatum {}
interface SimulationLink extends d3.SimulationLinkDatum<SimulationNode> {
  source: SimulationNode | number;
  target: SimulationNode | number;
  type: string;
  sharedTags?: number;
}

export default function ForceGraph({ data, onNodeClick, selectedSectors = [] }: ForceGraphProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const simulationRef = useRef<d3.Simulation<SimulationNode, SimulationLink> | null>(null);
  const [hoveredNode, setHoveredNode] = useState<{ node: Node; x: number; y: number } | null>(null);
  const hoverTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const [focusedSector, setFocusedSector] = useState<string | null>(null);
  const sectorElementsRef = useRef<Map<string, { circle: d3.Selection<SVGCircleElement, unknown, null, undefined>; label: d3.Selection<SVGTextElement, unknown, null, undefined> }>>(new Map());

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

    // Group nodes by sector
    const tagGroups = new Map<string, SimulationNode[]>();
    
    if (selectedSectors.length > 0) {
      // User-specified sectors: group by first matching sector tag
      nodes.forEach(node => {
        const matchingSector = selectedSectors.find(sector => node.tags.includes(sector));
        const sectorName = matchingSector || 'Other';
        if (!tagGroups.has(sectorName)) {
          tagGroups.set(sectorName, []);
        }
        tagGroups.get(sectorName)!.push(node);
      });
    } else {
      // Auto-group by primary tag (first tag)
      nodes.forEach(node => {
        const primaryTag = node.tags[0] || 'Other';
        if (!tagGroups.has(primaryTag)) {
          tagGroups.set(primaryTag, []);
        }
        tagGroups.get(primaryTag)!.push(node);
      });
    }

    // Calculate sector positions (evenly distributed in a circle)
    const tagArray = Array.from(tagGroups.keys());
    const sectorPositions = new Map<string, { x: number; y: number; radius: number }>();
    const baseRadius = Math.min(width, height) * 0.35;
    const centerX = width / 2;
    const centerY = height / 2;
    
    // Calculate dynamic radius for each sector based on node count
    const maxNodesInSector = Math.max(...Array.from(tagGroups.values()).map(g => g.length));
    
    tagArray.forEach((tag, i) => {
      const angle = (i / tagArray.length) * 2 * Math.PI;
      const nodeCount = tagGroups.get(tag)?.length || 0;
      
      // Dynamic sector radius: scales with sqrt of node count for area-based scaling
      // Min radius = 80, grows based on density
      const densityFactor = Math.sqrt(nodeCount / Math.max(maxNodesInSector, 1));
      const dynamicRadius = Math.max(80, 150 * densityFactor + (nodeCount > 20 ? 50 : 0));
      
      sectorPositions.set(tag, {
        x: centerX + baseRadius * Math.cos(angle),
        y: centerY + baseRadius * Math.sin(angle),
        radius: dynamicRadius,
      });
    });

    // Custom force to pull nodes toward their sector center
    const sectorForce = () => {
      nodes.forEach(node => {
        let sectorName: string;
        if (selectedSectors.length > 0) {
          const matchingSector = selectedSectors.find(sector => node.tags.includes(sector));
          sectorName = matchingSector || 'Other';
        } else {
          sectorName = node.tags[0] || 'Other';
        }
        
        const sector = sectorPositions.get(sectorName);
        if (sector && node.x !== undefined && node.y !== undefined) {
          const k = 0.3; // Strength of the pull
          node.vx = (node.vx || 0) + (sector.x - node.x) * k;
          node.vy = (node.vy || 0) + (sector.y - node.y) * k;
        }
      });
    };

    // Initialize D3 force simulation
    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink<SimulationNode, SimulationLink>(links)
        .id(d => d.id)
        .distance(d => (d as SimulationLink).type === 'explicit' ? 80 : 150)
        .strength(d => (d as SimulationLink).type === 'explicit' ? 0.5 : 0.02))
      .force('charge', d3.forceManyBody().strength(-150))
      .force('center', d3.forceCenter(width / 2, height / 2).strength(0.05))
      .force('collide', d3.forceCollide().radius(25))
      .force('sector', sectorForce);

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

    // Click on background to unfocus sectors
    svg.on('click', () => {
      setFocusedSector(null);
    });

    // Draw sectors using the Sector component
    const sectorGroup = g.append('g').attr('class', 'sectors');
    sectorElementsRef.current.clear();
    
    Array.from(sectorPositions.entries()).forEach(([sectorName, position]) => {
      const sectorData: SectorData = {
        name: sectorName,
        x: position.x,
        y: position.y,
        radius: position.radius,
        nodeCount: tagGroups.get(sectorName)?.length || 0,
      };
      
      const elements = renderSector({
        sector: sectorData,
        isFocused: focusedSector === sectorName,
        onFocus: (name) => {
          setFocusedSector(prev => prev === name ? null : name);
        },
        parent: sectorGroup,
      });
      
      sectorElementsRef.current.set(sectorName, elements);
    });

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
  }, [data, onNodeClick, selectedSectors]);

  // Update sector styles when focused sector changes
  useEffect(() => {
    sectorElementsRef.current.forEach((elements, sectorName) => {
      updateSectorStyle(elements.circle, elements.label, focusedSector === sectorName);
    });
  }, [focusedSector]);

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
