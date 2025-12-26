'use client';

import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { GraphData, Node } from '@/types/api';
import { renderSector, updateSectorStyle, SectorData } from './Sector';
import { renderExpandedSectorView } from './ExpandedSectorView';
import { SimulationNode, SimulationLink, SectorPosition } from './graph/types';
import { groupNodesBySector, getNodeSector } from './graph/sectorUtils';
import { calculateSectorPositions, sectorForceFunction } from './graph/sectorPositions';
import { PrimaryFilterIndicator } from './graph/PrimaryFilterIndicator';
import { ExpansionControls } from './graph/ExpansionControls';
import { CloseExpandedViewButton } from './graph/CloseExpandedViewButton';

interface ForceGraphProps {
  data: GraphData;
  onNodeClick: (node: Node) => void;
  selectedSectors?: string[];
  sectorsToExpand?: string[];
  onSectorsToExpandChange?: (sectors: string[]) => void;
  selectedNode?: Node | null;
  relatedNodes?: Set<number>;
}

export default function ForceGraph({ 
  data, 
  onNodeClick, 
  selectedSectors = [], 
  sectorsToExpand = [],
  onSectorsToExpandChange,
  selectedNode = null,
  relatedNodes = new Set()
}: ForceGraphProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const simulationRef = useRef<d3.Simulation<SimulationNode, SimulationLink> | null>(null);
  const hoverTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const [selectedSectorsForExpansion, setSelectedSectorsForExpansion] = useState<string[]>([]);
  const sectorElementsRef = useRef<Map<string, { circle: d3.Selection<SVGCircleElement, unknown, null, undefined>; label: d3.Selection<SVGTextElement, unknown, null, undefined> }>>(new Map());
  const zoomBehaviorRef = useRef<d3.ZoomBehavior<SVGSVGElement, unknown> | null>(null);
  const nodeSelectionRef = useRef<d3.Selection<SVGCircleElement, SimulationNode, SVGGElement, unknown> | null>(null);
  const linkSelectionRef = useRef<d3.Selection<SVGLineElement, SimulationLink, SVGGElement, unknown> | null>(null);
  const sectorPositionsRef = useRef<Map<string, SectorPosition>>(new Map());
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
    const tagGroups = groupNodesBySector(nodes, selectedSectors);

    // Store tag groups in ref for access in effects
    tagGroupsRef.current = tagGroups;

    // Calculate sector positions (evenly distributed in a circle)
    const sectorPositions = calculateSectorPositions(tagGroups, width, height);
    sectorPositionsRef.current = sectorPositions;

    // Custom force to pull nodes toward their sector center(s)
    // Multi-tag nodes are pulled toward the average of all their sectors
    const sectorForce = () => {
      sectorForceFunction(nodes, sectorPositions, (node) => getNodeSector(node, selectedSectors), sectorsToExpand, selectedSectors);
    };

    // Initialize D3 force simulation with different configurations based on whether sectors are selected
    const simulation = selectedSectors.length > 0
      ? d3.forceSimulation(nodes)
          .force('link', d3.forceLink<SimulationNode, SimulationLink>(links)
            .id(d => d.id)
            .distance(d => (d as SimulationLink).type === 'explicit' ? 80 : 150)
            .strength(d => (d as SimulationLink).type === 'explicit' ? 0.5 : 0.02))
          .force('charge', d3.forceManyBody().strength(-150))
          .force('center', d3.forceCenter(width / 2, height / 2).strength(0.05))
          .force('collide', d3.forceCollide().radius(25))
          .force('sector', sectorForce)
      : d3.forceSimulation(nodes)
          .force('link', d3.forceLink<SimulationNode, SimulationLink>(links)
            .id(d => d.id)
            .distance(d => (d as SimulationLink).type === 'explicit' ? 100 : 200)
            .strength(d => (d as SimulationLink).type === 'explicit' ? 0.8 : 0.01))
          .force('charge', d3.forceManyBody().strength(-200))
          .force('center', d3.forceCenter(width / 2, height / 2).strength(0.1))
          .force('collide', d3.forceCollide().radius(30));

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

    // Draw sectors using the Sector component (only when sectors are selected)
    const sectorGroup = g.append('g').attr('class', 'sectors');
    sectorElementsRef.current.clear();
    
    if (selectedSectors.length > 0) {
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
    }

    // Draw edges (explicit edges first so they appear below tag edges in rendering order)
    const link = g.append('g')
      .selectAll('line')
      .data(links.sort((a, b) => a.type === 'explicit' ? -1 : 1))
      .join('line')
      .attr('stroke', d => d.type === 'explicit' ? '#3b82f6' : '#9ca3af')
      .attr('stroke-width', d => d.type === 'explicit' ? 2 : 0.3)
      .attr('stroke-opacity', d => d.type === 'explicit' ? 0.5 : 0.08)
      .attr('stroke-dasharray', d => d.type === 'explicit' ? '0' : '3,3');

    linkSelectionRef.current = link;

    // Draw nodes
    const node = g.append('g')
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', d => {
        if (selectedNode && d.id === selectedNode.id) return 12;
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return 10;
        return 8;
      })
      .attr('data-sector', d => getNodeSector(d, selectedSectors))
      .attr('fill', d => {
        if (!d.solved) return '#d1d5db';
        // Basic color by difficulty for now (will add acceptance rate gradient later)
        if (d.difficulty === 'Easy') return '#86efac';
        if (d.difficulty === 'Medium') return '#fde047';
        return '#fca5a5';
      })
      .attr('stroke', d => {
        // Highlight selected node with bright cyan border
        if (selectedNode && d.id === selectedNode.id) return '#06b6d4';
        // Highlight related nodes with lighter cyan
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return '#22d3ee';
        if (d.difficulty === 'Easy') return '#22c55e';
        if (d.difficulty === 'Medium') return '#f97316';
        return '#ef4444';
      })
      .attr('stroke-width', d => {
        if (selectedNode && d.id === selectedNode.id) return 4;
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return 3;
        return 2;
      })
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

      // Update sector circle and label positions based on actual node positions (only when sectors are selected)
      if (selectedSectors.length > 0) {
        tagGroups.forEach((sectorNodes, sectorName) => {
          if (sectorNodes.length === 0) return;
          
          // Calculate center of mass for this sector's nodes
          let centerX = 0;
          let centerY = 0;
          sectorNodes.forEach(n => {
            if (n.x !== undefined && n.y !== undefined) {
              centerX += n.x;
              centerY += n.y;
            }
          });
          centerX /= sectorNodes.length;
          centerY /= sectorNodes.length;

          // Update sector elements
          const sectorElements = sectorElementsRef.current.get(sectorName);
          if (sectorElements) {
            const currentRadius = parseFloat(sectorElements.circle.attr('r'));
            sectorElements.circle
              .attr('cx', centerX)
              .attr('cy', centerY);
            sectorElements.label
              .attr('x', centerX)
              .attr('y', centerY - currentRadius - 10);
          }
        });
      }
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

    // Stop simulation after it settles to prevent constant re-computation
    simulation.on('end', () => {
      simulation.stop();
    });

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

  // Update node highlighting when selectedNode changes
  useEffect(() => {
    if (!nodeSelectionRef.current) return;
    
    nodeSelectionRef.current
      .attr('r', (d: SimulationNode) => {
        if (selectedNode && d.id === selectedNode.id) return 12;
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return 10;
        return 8;
      })
      .attr('stroke', (d: SimulationNode) => {
        if (selectedNode && d.id === selectedNode.id) return '#06b6d4';
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return '#22d3ee';
        if (d.difficulty === 'Easy') return '#22c55e';
        if (d.difficulty === 'Medium') return '#f97316';
        return '#ef4444';
      })
      .attr('stroke-width', (d: SimulationNode) => {
        if (selectedNode && d.id === selectedNode.id) return 4;
        if (relatedNodes.has(d.id) && relatedNodes.size > 1) return 3;
        return 2;
      });
  }, [selectedNode, relatedNodes]);

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
      
      <PrimaryFilterIndicator selectedSectors={selectedSectors} />
      
      <ExpansionControls
        selectedSectorsForExpansion={selectedSectorsForExpansion}
        onExpand={() => {
          if (onSectorsToExpandChange) {
            onSectorsToExpandChange([...selectedSectorsForExpansion]);
          }
        }}
        onClearSelection={() => setSelectedSectorsForExpansion([])}
      />
      
      <CloseExpandedViewButton
        sectorsToExpand={sectorsToExpand}
        onClose={() => {
          if (onSectorsToExpandChange) {
            onSectorsToExpandChange([]);
          }
          setSelectedSectorsForExpansion([]);
        }}
      />
    </div>
  );
}
