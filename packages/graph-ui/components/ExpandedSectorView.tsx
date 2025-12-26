'use client';

import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { Node, Edge } from '@/types/api';

interface SimulationNode extends Node, d3.SimulationNodeDatum {
  layer?: number;
}

interface SimulationLink extends d3.SimulationLinkDatum<SimulationNode> {
  source: SimulationNode | number;
  target: SimulationNode | number;
  type: string;
}

interface ExpandedSectorViewProps {
  nodes: Node[];
  edges: Edge[];
  sectorName: string;
  sectorPosition: { x: number; y: number; radius: number };
  onNodeClick: (node: Node) => void;
  parentGroup: d3.Selection<SVGGElement, unknown, null, undefined>;
}

/**
 * Creates a topological/hierarchical layout for nodes within a sector
 */
export function renderExpandedSectorView({
  nodes,
  edges,
  sectorName,
  sectorPosition,
  onNodeClick,
  parentGroup,
}: ExpandedSectorViewProps): {
  nodeSelection: d3.Selection<SVGCircleElement, SimulationNode, SVGGElement, unknown>;
  linkSelection: d3.Selection<SVGLineElement, SimulationLink, SVGGElement, unknown>;
  cleanup: () => void;
} {
  // Create a group for this sector's expanded view
  const sectorGroup = parentGroup
    .append('g')
    .attr('class', `expanded-sector-${sectorName}`);

  // Add background panel
  const expandedRadius = sectorPosition.radius * 2;
  sectorGroup
    .append('rect')
    .attr('x', sectorPosition.x - expandedRadius)
    .attr('y', sectorPosition.y - expandedRadius)
    .attr('width', expandedRadius * 2)
    .attr('height', expandedRadius * 2)
    .attr('rx', 12)
    .attr('fill', '#1a1a1a')
    .attr('stroke', '#374151')
    .attr('stroke-width', 2)
    .attr('opacity', 0.95);

  // Build adjacency information
  const nodeMap = new Map<number, SimulationNode>();
  const simNodes: SimulationNode[] = nodes.map(n => {
    const node = { ...n };
    nodeMap.set(n.id, node);
    return node;
  });

  const simLinks: SimulationLink[] = edges
    .filter(e => {
      const sourceNode = nodes.find(n => n.id === e.source);
      const targetNode = nodes.find(n => n.id === e.target);
      return sourceNode && targetNode;
    })
    .map(e => ({
      source: e.source,
      target: e.target,
      type: e.type,
    }));

  // Calculate topological layers for hierarchical layout
  const layers = calculateTopologicalLayers(simNodes, simLinks);
  
  // Assign layers to nodes
  simNodes.forEach(node => {
    node.layer = layers.get(node.id) || 0;
  });

  // Group nodes by their primary sector tag first
  const nodesBySector = new Map<string, SimulationNode[]>();
  simNodes.forEach(node => {
    const primaryTag = node.tags[0] || 'Other';
    if (!nodesBySector.has(primaryTag)) {
      nodesBySector.set(primaryTag, []);
    }
    nodesBySector.get(primaryTag)!.push(node);
  });

  // Position nodes in a hierarchical layout grouped by sector
  const maxLayer = Math.max(...Array.from(layers.values()));
  const layerWidth = (expandedRadius * 2) / Math.max(maxLayer + 1, 1);

  // Calculate sector groups and their vertical positions
  const sectorTags = Array.from(nodesBySector.keys());
  const sectorGroupHeight = expandedRadius * 2 / Math.max(sectorTags.length, 1);
  
  // Position nodes by sector group, then by layer within each sector
  sectorTags.forEach((sectorTag, sectorIndex) => {
    const sectorNodes = nodesBySector.get(sectorTag)!;
    
    // Group nodes by layer within this sector
    const nodesByLayer = new Map<number, SimulationNode[]>();
    sectorNodes.forEach(node => {
      const layer = node.layer || 0;
      if (!nodesByLayer.has(layer)) {
        nodesByLayer.set(layer, []);
      }
      nodesByLayer.get(layer)!.push(node);
    });

    // Calculate vertical space for this sector group
    const sectorCenterY = sectorPosition.y - expandedRadius + sectorGroupHeight * (sectorIndex + 0.5);
    const availableHeight = Math.min(sectorGroupHeight * 0.9, 800); // Limit height per sector
    
    // Position nodes within each layer for this sector
    nodesByLayer.forEach((layerNodes, layer) => {
      const nodeSpacing = Math.max(80, availableHeight / (layerNodes.length + 1)); // Minimum 80px spacing
      
      layerNodes.forEach((node, index) => {
        // Position from left to right for layers, top to bottom for nodes within layer
        const totalHeight = nodeSpacing * (layerNodes.length - 1);
        const startY = sectorCenterY - totalHeight / 2;
        node.x = sectorPosition.x - expandedRadius + layerWidth * (layer + 0.5);
        node.y = startY + nodeSpacing * index;
      });
    });
  });

  // Add sector group labels and separators
  const sectorLabelsGroup = sectorGroup.append('g').attr('class', 'sector-labels');
  sectorTags.forEach((sectorTag, sectorIndex) => {
    const sectorCenterY = sectorPosition.y - expandedRadius + sectorGroupHeight * (sectorIndex + 0.5);
    
    // Add separator line (except for the first one)
    if (sectorIndex > 0) {
      const separatorY = sectorPosition.y - expandedRadius + sectorGroupHeight * sectorIndex;
      sectorLabelsGroup
        .append('line')
        .attr('x1', sectorPosition.x - expandedRadius + 10)
        .attr('y1', separatorY)
        .attr('x2', sectorPosition.x + expandedRadius - 10)
        .attr('y2', separatorY)
        .attr('stroke', '#4b5563')
        .attr('stroke-width', 1.5)
        .attr('stroke-dasharray', '8,4')
        .attr('opacity', 0.4);
    }
    
    // Add sector label with background
    const labelX = sectorPosition.x - expandedRadius + 20;
    const labelY = sectorCenterY - sectorGroupHeight * 0.4;
    
    sectorLabelsGroup
      .append('rect')
      .attr('x', labelX - 8)
      .attr('y', labelY - 16)
      .attr('width', sectorTag.length * 8 + 16)
      .attr('height', 24)
      .attr('rx', 4)
      .attr('fill', '#1e40af')
      .attr('opacity', 0.8);
    
    sectorLabelsGroup
      .append('text')
      .attr('x', labelX)
      .attr('y', labelY)
      .attr('text-anchor', 'start')
      .attr('font-size', '13px')
      .attr('font-weight', '600')
      .attr('fill', '#dbeafe')
      .text(sectorTag);
  });

  // Helper function to check if an edge crosses sector boundaries
  const isCrossSectorEdge = (link: SimulationLink): boolean => {
    const source = typeof link.source === 'number' ? nodeMap.get(link.source) : link.source;
    const target = typeof link.target === 'number' ? nodeMap.get(link.target) : link.target;
    if (!source || !target) return false;
    
    const sourcePrimaryTag = source.tags[0] || 'Other';
    const targetPrimaryTag = target.tags[0] || 'Other';
    return sourcePrimaryTag !== targetPrimaryTag;
  };

  // Draw edges
  const linkGroup = sectorGroup.append('g').attr('class', 'links');
  const linkSelection = linkGroup
    .selectAll('line')
    .data(simLinks)
    .join('line')
    .attr('x1', d => {
      const source = typeof d.source === 'number' ? nodeMap.get(d.source) : d.source;
      return source?.x || 0;
    })
    .attr('y1', d => {
      const source = typeof d.source === 'number' ? nodeMap.get(d.source) : d.source;
      return source?.y || 0;
    })
    .attr('x2', d => {
      const target = typeof d.target === 'number' ? nodeMap.get(d.target) : d.target;
      return target?.x || 0;
    })
    .attr('y2', d => {
      const target = typeof d.target === 'number' ? nodeMap.get(d.target) : d.target;
      return target?.y || 0;
    })
    .attr('stroke', d => {
      // Cross-sector edges get special highlighting
      if (isCrossSectorEdge(d)) {
        return d.type === 'explicit' ? '#a855f7' : '#c084fc'; // Purple for cross-sector
      }
      return d.type === 'explicit' ? '#3b82f6' : '#9ca3af';
    })
    .attr('stroke-width', d => {
      // Cross-sector edges are thicker
      if (isCrossSectorEdge(d)) {
        return d.type === 'explicit' ? 3 : 2;
      }
      return d.type === 'explicit' ? 2 : 1;
    })
    .attr('stroke-opacity', d => {
      // Cross-sector edges are more visible
      if (isCrossSectorEdge(d)) {
        return d.type === 'explicit' ? 0.7 : 0.4;
      }
      return d.type === 'explicit' ? 0.5 : 0.2;
    })
    .attr('stroke-dasharray', d => isCrossSectorEdge(d) ? '5,3' : 'none')
    .attr('marker-end', d => d.type === 'explicit' ? (isCrossSectorEdge(d) ? 'url(#arrowhead-cross)' : 'url(#arrowhead)') : null);

  // Add arrowhead marker definitions
  const defs = sectorGroup.append('defs');
  
  // Regular arrowhead for same-sector edges
  defs.append('marker')
    .attr('id', 'arrowhead')
    .attr('markerWidth', 10)
    .attr('markerHeight', 10)
    .attr('refX', 20)
    .attr('refY', 3)
    .attr('orient', 'auto')
    .append('polygon')
    .attr('points', '0 0, 10 3, 0 6')
    .attr('fill', '#3b82f6');

  // Purple arrowhead for cross-sector edges
  defs.append('marker')
    .attr('id', 'arrowhead-cross')
    .attr('markerWidth', 10)
    .attr('markerHeight', 10)
    .attr('refX', 20)
    .attr('refY', 3)
    .attr('orient', 'auto')
    .append('polygon')
    .attr('points', '0 0, 10 3, 0 6')
    .attr('fill', '#a855f7');

  // Draw nodes
  const nodeGroup = sectorGroup.append('g').attr('class', 'nodes');
  const nodeSelection = nodeGroup
    .selectAll('circle')
    .data(simNodes)
    .join('circle')
    .attr('cx', d => d.x || 0)
    .attr('cy', d => d.y || 0)
    .attr('r', 10)
    .attr('fill', d => {
      if (!d.solved) return '#d1d5db';
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
    .on('click', (event, d) => {
      event.stopPropagation();
      onNodeClick(d);
    });

  // Add node labels
  const labelGroup = sectorGroup.append('g').attr('class', 'labels');
  labelGroup
    .selectAll('text')
    .data(simNodes)
    .join('text')
    .attr('x', d => (d.x || 0) + 15)
    .attr('y', d => (d.y || 0) + 4)
    .attr('text-anchor', 'start')
    .attr('font-size', '10px')
    .attr('fill', '#e5e7eb')
    .attr('font-weight', '400')
    .attr('pointer-events', 'none')
    .style('text-shadow', '1px 1px 2px #000, 0 0 4px #000')
    .text(d => {
      const maxLength = 35;
      return d.title.length > maxLength ? d.title.substring(0, maxLength) + '...' : d.title;
    });

  // Fade in animation
  sectorGroup
    .style('opacity', 0)
    .transition()
    .duration(500)
    .style('opacity', 1);

  return {
    nodeSelection,
    linkSelection,
    cleanup: () => {
      sectorGroup.transition().duration(300).style('opacity', 0).remove();
    },
  };
}

/**
 * Calculate topological layers using BFS from nodes with no incoming edges
 */
function calculateTopologicalLayers(
  nodes: SimulationNode[],
  links: SimulationLink[]
): Map<number, number> {
  const layers = new Map<number, number>();
  const inDegree = new Map<number, number>();
  const outgoing = new Map<number, number[]>();

  // Initialize
  nodes.forEach(node => {
    inDegree.set(node.id, 0);
    outgoing.set(node.id, []);
  });

  // Build graph structure (only explicit edges for topological ordering)
  links.forEach(link => {
    if (link.type === 'explicit') {
      const sourceId = typeof link.source === 'number' ? link.source : link.source.id;
      const targetId = typeof link.target === 'number' ? link.target : link.target.id;
      
      inDegree.set(targetId, (inDegree.get(targetId) || 0) + 1);
      outgoing.get(sourceId)?.push(targetId);
    }
  });

  // BFS to assign layers
  const queue: Array<{ id: number; layer: number }> = [];
  
  // Start with nodes that have no incoming edges
  nodes.forEach(node => {
    if (inDegree.get(node.id) === 0) {
      queue.push({ id: node.id, layer: 0 });
      layers.set(node.id, 0);
    }
  });

  // If no starting nodes (cycle or isolated), start with first node
  if (queue.length === 0 && nodes.length > 0) {
    queue.push({ id: nodes[0].id, layer: 0 });
    layers.set(nodes[0].id, 0);
  }

  while (queue.length > 0) {
    const { id, layer } = queue.shift()!;
    
    outgoing.get(id)?.forEach(targetId => {
      const currentLayer = layers.get(targetId);
      const newLayer = layer + 1;
      
      if (currentLayer === undefined || newLayer > currentLayer) {
        layers.set(targetId, newLayer);
        queue.push({ id: targetId, layer: newLayer });
      }
    });
  }

  // Assign layer 0 to any remaining nodes
  nodes.forEach(node => {
    if (!layers.has(node.id)) {
      layers.set(node.id, 0);
    }
  });

  return layers;
}
