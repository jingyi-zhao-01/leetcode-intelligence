'use client';

import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { GraphData, Node } from '@/types/api';
import { renderSector, updateSectorStyle, SectorData } from './Sector';
import { renderExpandedSectorView } from './ExpandedSectorView';

interface ForceGraphProps {
  data: GraphData;
  onNodeClick: (node: Node) => void;
  selectedSectors?: string[];
  sectorsToExpand?: string[];
  onSectorsToExpandChange?: (sectors: string[]) => void;
}

interface SimulationNode extends Node, d3.SimulationNodeDatum {}
interface SimulationLink extends d3.SimulationLinkDatum<SimulationNode> {
  source: SimulationNode | number;
  target: SimulationNode | number;
  type: string;
  sharedTags?: number;
}

export default function ForceGraph({ 
  data, 
  onNodeClick, 
  selectedSectors = [], 
  sectorsToExpand = [],
  onSectorsToExpandChange 
}: ForceGraphProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const simulationRef = useRef<d3.Simulation<SimulationNode, SimulationLink> | null>(null);
  const hoverTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const [selectedSectorsForExpansion, setSelectedSectorsForExpansion] = useState<string[]>([]);
  const sectorElementsRef = useRef<Map<string, { circle: d3.Selection<SVGCircleElement, unknown, null, undefined>; label: d3.Selection<SVGTextElement, unknown, null, undefined> }>>(new Map());
  const zoomBehaviorRef = useRef<d3.ZoomBehavior<SVGSVGElement, unknown> | null>(null);
  const nodeSelectionRef = useRef<d3.Selection<SVGCircleElement, SimulationNode, SVGGElement, unknown> | null>(null);
  const linkSelectionRef = useRef<d3.Selection<SVGLineElement, SimulationLink, SVGGElement, unknown> | null>(null);
  const sectorPositionsRef = useRef<Map<string, { x: number; y: number; radius: number }>>(new Map());
  const tagGroupsRef = useRef<Map<string, SimulationNode[]>>(new Map());
  const expandedViewCleanupRef = useRef<(() => void) | null>(null);
  const containerGroupRef = useRef<d3.Selection<SVGGElement, unknown, null, undefined> | null>(null);

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

    // Store tag groups in ref for access in effects
    tagGroupsRef.current = tagGroups;

    // Calculate sector positions (evenly distributed in a circle)
    const tagArray = Array.from(tagGroups.keys());
    const sectorPositions = new Map<string, { x: number; y: number; radius: number }>();
    sectorPositionsRef.current = sectorPositions;
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

    // Helper to get node's sector
    const getNodeSector = (node: SimulationNode): string => {
      if (selectedSectors.length > 0) {
        const matchingSector = selectedSectors.find(sector => node.tags.includes(sector));
        return matchingSector || 'Other';
      }
      return node.tags[0] || 'Other';
    };

    // Custom force to pull nodes toward their sector center
    const sectorForce = () => {
      nodes.forEach(node => {
        const sectorName = getNodeSector(node);
        const sector = sectorPositions.get(sectorName);
        if (sector && node.x !== undefined && node.y !== undefined) {
          // Reduce pull strength when this sector is being expanded to spread nodes
          const k = (sectorsToExpand.includes(sectorName)) ? 0.05 : 0.3;
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
    containerGroupRef.current = g;

    // Add zoom behavior
    const zoom = d3.zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.1, 10])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      });

    zoomBehaviorRef.current = zoom;
    svg.call(zoom);

    // Click on background to clear selection
    svg.on('click', () => {
      setSelectedSectorsForExpansion([]);
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
        isFocused: selectedSectorsForExpansion.includes(sectorName),
        onFocus: (name) => {
          // Toggle sector selection (max 2 sectors)
          setSelectedSectorsForExpansion(prev => {
            if (prev.includes(name)) {
              return prev.filter(s => s !== name);
            } else if (prev.length >= 2) {
              // Already have 2 sectors selected, replace the first one
              return [prev[1], name];
            } else {
              return [...prev, name];
            }
          });
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

    linkSelectionRef.current = link;

    // Draw nodes
    const node = g.append('g')
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', 8)
      .attr('data-sector', d => getNodeSector(d))
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

    nodeSelectionRef.current = node;

    // Add click handler
    node.on('click', (event, d) => {
      event.stopPropagation();
      onNodeClick(d);
    });

    // Add tooltips
    node.append('title')
      .text(d => `${d.title}\nDifficulty: ${d.difficulty}\nAcceptance: ${d.acceptanceRate}%`);

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
      if (expandedViewCleanupRef.current) {
        expandedViewCleanupRef.current();
      }
    };
  }, [data, onNodeClick, selectedSectors, selectedSectorsForExpansion, sectorsToExpand]);

  // Update sector styles when selected sectors change
  useEffect(() => {
    sectorElementsRef.current.forEach((elements, sectorName) => {
      updateSectorStyle(elements.circle, elements.label, selectedSectorsForExpansion.includes(sectorName));
    });
  }, [selectedSectorsForExpansion]);

  // Handle zoom and filtering when sectors are expanded
  useEffect(() => {
    if (!svgRef.current || !zoomBehaviorRef.current || !nodeSelectionRef.current || !linkSelectionRef.current) return;

    const svg = d3.select(svgRef.current);
    const nodes = nodeSelectionRef.current;
    const links = linkSelectionRef.current;
    const simulation = simulationRef.current;

    if (sectorsToExpand.length > 0) {
      // Clean up any existing expanded view
      if (expandedViewCleanupRef.current) {
        expandedViewCleanupRef.current();
        expandedViewCleanupRef.current = null;
      }

      // Stop the force simulation when showing hierarchical view
      if (simulation) {
        simulation.stop();
      }

      // Collect all nodes and edges from selected sectors
      const allSectorNodes: SimulationNode[] = [];
      const allSectorNodeIds = new Set<number>();
      
      sectorsToExpand.forEach(sectorName => {
        const sectorNodes = tagGroupsRef.current.get(sectorName) || [];
        allSectorNodes.push(...sectorNodes);
        sectorNodes.forEach(n => allSectorNodeIds.add(n.id));
      });
      
      // Get all edges where source is in the selected sectors
      const sectorEdges = data.edges.filter(e => allSectorNodeIds.has(e.source));

      // Calculate the center position for the expanded view
      let centerX = 0;
      let centerY = 0;
      let totalRadius = 0;
      
      sectorsToExpand.forEach(sectorName => {
        const sectorPos = sectorPositionsRef.current.get(sectorName);
        if (sectorPos) {
          centerX += sectorPos.x;
          centerY += sectorPos.y;
          totalRadius = Math.max(totalRadius, sectorPos.radius);
        }
      });
      
      centerX /= sectorsToExpand.length;
      centerY /= sectorsToExpand.length;

      // Expand sector circles
      sectorsToExpand.forEach(sectorName => {
        const focusedSectorElements = sectorElementsRef.current.get(sectorName);
        const sectorPos = sectorPositionsRef.current.get(sectorName);
        if (focusedSectorElements && sectorPos) {
          const expandedRadius = sectorPos.radius * 2;
          focusedSectorElements.circle
            .transition()
            .duration(750)
            .attr('r', expandedRadius);
          focusedSectorElements.label
            .transition()
            .duration(750)
            .attr('y', sectorPos.y - expandedRadius - 10);
        }
      });

      // Calculate zoom transform to center on combined sectors
      const width = svgRef.current.clientWidth;
      const height = svgRef.current.clientHeight;
      const scale = 2.5;
      const translateX = width / 2 - centerX * scale;
      const translateY = height / 2 - centerY * scale;
      const transform = d3.zoomIdentity.translate(translateX, translateY).scale(scale);

      // Zoom to sector with animation
      svg.transition().duration(750).call(
        zoomBehaviorRef.current.transform as any,
        transform
      );

      // Hide original force-directed nodes and edges
      nodes
        .transition()
        .duration(500)
        .attr('opacity', 0)
        .attr('pointer-events', 'none');

      links
        .transition()
        .duration(500)
        .attr('opacity', 0)
        .attr('pointer-events', 'none');

      // Hide/show sector circles and labels
      sectorElementsRef.current.forEach((elements, sectorName) => {
        if (!sectorsToExpand.includes(sectorName)) {
          elements.circle.transition().duration(500).attr('opacity', 0);
          elements.label.transition().duration(500).attr('opacity', 0);
        } else {
          elements.circle.transition().duration(500).attr('opacity', 0.3);
          elements.label.transition().duration(500).attr('opacity', 1);
        }
      });

      // Render hierarchical expanded view after zoom animation
      setTimeout(() => {
        if (containerGroupRef.current) {
          const { cleanup } = renderExpandedSectorView({            nodes: allSectorNodes,
            edges: sectorEdges,
            sectorName: sectorsToExpand.join(' + '),
            sectorPosition: {
              x: centerX,
              y: centerY,
              radius: totalRadius * 2,
            },
            onNodeClick: onNodeClick,
            parentGroup: containerGroupRef.current,
          });
          expandedViewCleanupRef.current = cleanup;
        }
      }, 750);
    } else {
      // Clean up expanded view
      if (expandedViewCleanupRef.current) {
        expandedViewCleanupRef.current();
        expandedViewCleanupRef.current = null;
      }

      // Restart the force simulation
      if (simulation) {
        simulation.alpha(0.3).restart();
      }

      // Reset sector radii to original size
      sectorElementsRef.current.forEach((elements, sectorName) => {
        const sectorPos = sectorPositionsRef.current.get(sectorName);
        if (sectorPos) {
          elements.circle
            .transition()
            .duration(750)
            .attr('r', sectorPos.radius);
          elements.label
            .transition()
            .duration(750)
            .attr('y', sectorPos.y - sectorPos.radius - 10);
        }
      });

      // Reset: show all nodes and edges
      nodes
        .transition()
        .duration(500)
        .attr('opacity', 1)
        .attr('pointer-events', 'all');

      links
        .transition()
        .duration(500)
        .attr('opacity', d => (d as SimulationLink).type === 'explicit' ? 0.8 : 0.2)
        .attr('pointer-events', 'all');

      // Show all sectors
      sectorElementsRef.current.forEach((elements) => {
        elements.circle.transition().duration(500).attr('opacity', 1);
        elements.label.transition().duration(500).attr('opacity', 1);
      });
    }
  }, [sectorsToExpand, data, onNodeClick]);

  return (
    <div className="relative w-full h-full">
      <svg
        ref={svgRef}
        className="w-full h-full border border-gray-300"
        style={{ minHeight: '600px' }}
      />
      
      {/* Expand Button */}
      {selectedSectorsForExpansion.length > 0 && (
        <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2">
          <button
            onClick={() => {
              if (onSectorsToExpandChange) {
                onSectorsToExpandChange([...selectedSectorsForExpansion]);
              }
            }}
            className="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
          >
            Expand {selectedSectorsForExpansion.length} Sector{selectedSectorsForExpansion.length > 1 ? 's' : ''}
          </button>
          <button
            onClick={() => setSelectedSectorsForExpansion([])}
            className="px-6 py-3 bg-gray-600 hover:bg-gray-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
          >
            Clear Selection
          </button>
        </div>
      )}
      
      {/* Close Expanded View Button */}
      {sectorsToExpand.length > 0 && (
        <div className="absolute top-4 right-4">
          <button
            onClick={() => {
              if (onSectorsToExpandChange) {
                onSectorsToExpandChange([]);
              }
              setSelectedSectorsForExpansion([]);
            }}
            className="px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
          >
            Close Expanded View
          </button>
        </div>
      )}
    </div>
  );
}
