import { SimulationNode } from './types';

/**
 * Groups nodes by sector based on selected filters
 * Nodes can belong to multiple sectors if they have multiple tags
 */
export function groupNodesBySector(
  nodes: SimulationNode[],
  selectedSectors: string[]
): Map<string, SimulationNode[]> {
  const tagGroups = new Map<string, SimulationNode[]>();

  if (selectedSectors.length > 0) {
    // When specific sectors are selected, ONLY show those sectors
    // Nodes appear in sectors they belong to
    nodes.forEach(node => {
      // Get tags that ARE in the selectedSectors
      const matchingTags = node.tags.filter(tag => selectedSectors.includes(tag));

      if (matchingTags.length > 0) {
        // Add node to ALL its matching tag sectors (allowing overlap)
        matchingTags.forEach(tag => {
          if (!tagGroups.has(tag)) {
            tagGroups.set(tag, []);
          }
          tagGroups.get(tag)!.push(node);
        });
      }
    });
  } else {
    // Auto-group by ALL tags (nodes appear in multiple sectors)
    nodes.forEach(node => {
      if (node.tags.length === 0) {
        const sectorName = 'Other';
        if (!tagGroups.has(sectorName)) {
          tagGroups.set(sectorName, []);
        }
        tagGroups.get(sectorName)!.push(node);
      } else {
        // Add node to each of its tag sectors
        node.tags.forEach(tag => {
          if (!tagGroups.has(tag)) {
            tagGroups.set(tag, []);
          }
          tagGroups.get(tag)!.push(node);
        });
      }
    });
  }

  return tagGroups;
}

/**
 * Gets the sector name for a node
 */
export function getNodeSector(node: SimulationNode, selectedSectors: string[]): string {
  if (selectedSectors.length > 0) {
    // Return first matching tag from selectedSectors
    const matchingTags = node.tags.filter(tag => selectedSectors.includes(tag));
    return matchingTags.length > 0 ? matchingTags[0] : 'Other';
  }
  return node.tags[0] || 'Other';
}
