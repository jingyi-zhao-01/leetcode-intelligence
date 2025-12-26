import * as d3 from 'd3';
import { SimulationNode, SimulationLink, SectorPosition } from './types';
import { sectorForceFunction } from './sectorPositions';
import { getNodeSector } from './sectorUtils';

interface UseSimulationParams {
  nodes: SimulationNode[];
  links: SimulationLink[];
  width: number;
  height: number;
  sectorPositions: Map<string, SectorPosition>;
  selectedSectors: string[];
  sectorsToExpand: string[];
  onTick: () => void;
}

export function createSimulation({
  nodes,
  links,
  width,
  height,
  sectorPositions,
  selectedSectors,
  sectorsToExpand,
  onTick,
}: UseSimulationParams): d3.Simulation<SimulationNode, SimulationLink> {
  // Custom force to pull nodes toward their sector center
  const sectorForce = () => {
    sectorForceFunction(
      nodes,
      sectorPositions,
      (node) => getNodeSector(node, selectedSectors),
      sectorsToExpand
    );
  };

  // Initialize D3 force simulation
  const simulation = d3
    .forceSimulation(nodes)
    .force(
      'link',
      d3
        .forceLink<SimulationNode, SimulationLink>(links)
        .id(d => d.id)
        .distance(d => (d as SimulationLink).type === 'explicit' ? 80 : 150)
        .strength(d => (d as SimulationLink).type === 'explicit' ? 0.5 : 0.02)
    )
    .force('charge', d3.forceManyBody().strength(-150))
    .force('center', d3.forceCenter(width / 2, height / 2).strength(0.05))
    .force('collide', d3.forceCollide().radius(25))
    .force('sector', sectorForce)
    .on('tick', onTick);

  return simulation;
}
