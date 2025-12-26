import * as d3 from 'd3';
import { Node } from '@/types/api';

export interface SimulationNode extends Node, d3.SimulationNodeDatum {}

export interface SimulationLink extends d3.SimulationLinkDatum<SimulationNode> {
  source: SimulationNode | number;
  target: SimulationNode | number;
  type: string;
  sharedTags?: number;
}

export interface SectorPosition {
  x: number;
  y: number;
  radius: number;
}
