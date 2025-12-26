import * as d3 from 'd3';
import { SimulationNode, SectorPosition } from './types';

/**
 * Calculates evenly distributed positions for sectors in a circle
 * Sectors can overlap to allow shared nodes to be positioned in intersection areas
 */
export function calculateSectorPositions(
  tagGroups: Map<string, SimulationNode[]>,
  width: number,
  height: number
): Map<string, SectorPosition> {
  const sectorPositions = new Map<string, SectorPosition>();
  const centerX = width / 2;
  const centerY = height / 2;
  // Larger base radius for better spacing between sectors
  const baseRadius = Math.min(width, height) * 0.4;

  const tagArray = Array.from(tagGroups.keys());
  const maxNodesInSector = Math.max(...Array.from(tagGroups.values()).map(g => g.length));

  tagArray.forEach((tag, i) => {
    const angle = (i / tagArray.length) * 2 * Math.PI;
    const nodeCount = tagGroups.get(tag)?.length || 0;

    // Smaller sector radius for less overlap
    const densityFactor = Math.sqrt(nodeCount / Math.max(maxNodesInSector, 1));
    const dynamicRadius = Math.max(60, 120 * densityFactor + (nodeCount > 20 ? 40 : 0));

    sectorPositions.set(tag, {
      x: centerX + baseRadius * Math.cos(angle),
      y: centerY + baseRadius * Math.sin(angle),
      radius: dynamicRadius,
    });
  });

  return sectorPositions;
}

/**
 * Creates a custom force that pulls nodes toward their sector center
 */
export function createSectorForce(
  sectorPositions: Map<string, SectorPosition>,
  getNodeSector: (node: SimulationNode) => string,
  sectorsToExpand: string[]
) {
  return () => {
    return (alpha: number) => {
      // This function is called by D3 simulation on each tick
    };
  };
}

/**
 * Creates the sector force function for D3 simulation
 * Multi-tag nodes are pulled toward the average position of all their sectors
 */
export function sectorForceFunction(
  nodes: SimulationNode[],
  sectorPositions: Map<string, SectorPosition>,
  getNodeSector: (node: SimulationNode) => string,
  sectorsToExpand: string[],
  selectedSectors: string[] = []
) {
  nodes.forEach(node => {
    if (node.x === undefined || node.y === undefined) return;

    // Get all sectors this node belongs to
    // If selectedSectors is provided, only consider those sectors
    const relevantTags = selectedSectors.length > 0
      ? node.tags.filter(tag => selectedSectors.includes(tag))
      : node.tags;

    const nodeSectors = relevantTags
      .map(tag => sectorPositions.get(tag))
      .filter(sector => sector !== undefined) as SectorPosition[];

    if (nodeSectors.length === 0) return;

    // Calculate average position of all sectors this node belongs to
    let targetX = 0;
    let targetY = 0;
    nodeSectors.forEach(sector => {
      targetX += sector.x;
      targetY += sector.y;
    });
    targetX /= nodeSectors.length;
    targetY /= nodeSectors.length;

    // Pull node toward the intersection point of its sectors
    const primarySector = getNodeSector(node);
    const k = sectorsToExpand.includes(primarySector) ? 0.03 : 0.2;
    node.vx = (node.vx || 0) + (targetX - node.x) * k;
    node.vy = (node.vy || 0) + (targetY - node.y) * k;
  });
}
