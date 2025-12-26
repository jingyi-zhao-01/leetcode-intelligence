'use client';

import * as d3 from 'd3';

export interface SectorData {
  name: string;
  x: number;
  y: number;
  radius: number;
  nodeCount: number;
}

interface RenderSectorOptions {
  sector: SectorData;
  isFocused: boolean;
  onFocus: (sectorName: string) => void;
  parent: d3.Selection<SVGGElement, unknown, null, undefined>;
}

/**
 * Renders a sector circle and label in the SVG
 */
export function renderSector({ sector, isFocused, onFocus, parent }: RenderSectorOptions): {
  circle: d3.Selection<SVGCircleElement, unknown, null, undefined>;
  label: d3.Selection<SVGTextElement, unknown, null, undefined>;
} {
  // Draw sector background circle
  const circle = parent
    .append('circle')
    .attr('cx', sector.x)
    .attr('cy', sector.y)
    .attr('r', sector.radius)
    .attr('fill', isFocused ? 'rgba(59, 130, 246, 0.05)' : 'rgba(100, 100, 100, 0.02)')
    .attr('stroke', isFocused ? 'rgba(59, 130, 246, 0.5)' : 'rgba(150, 150, 150, 0.2)')
    .attr('stroke-width', isFocused ? 1.5 : 0.8)
    .attr('stroke-dasharray', isFocused ? '0' : '5,5')
    .style('cursor', 'pointer')
    .on('click', (event) => {
      event.stopPropagation();
      onFocus(sector.name);
    });

  // Draw sector label
  const label = parent
    .append('text')
    .attr('x', sector.x)
    .attr('y', sector.y - sector.radius - 10)
    .attr('text-anchor', 'middle')
    .attr('font-size', isFocused ? '14px' : '12px')
    .attr('font-weight', 'bold')
    .attr('fill', isFocused ? '#3b82f6' : '#666')
    .style('cursor', 'pointer')
    .text(`${sector.name} (${sector.nodeCount})`)
    .on('click', (event) => {
      event.stopPropagation();
      onFocus(sector.name);
    });

  return { circle, label };
}

/**
 * Updates sector styling based on focus state
 */
export function updateSectorStyle(
  circle: d3.Selection<SVGCircleElement, unknown, null, undefined>,
  label: d3.Selection<SVGTextElement, unknown, null, undefined>,
  isFocused: boolean
): void {
  circle
    .attr('fill', isFocused ? 'rgba(59, 130, 246, 0.05)' : 'rgba(100, 100, 100, 0.02)')
    .attr('stroke', isFocused ? 'rgba(59, 130, 246, 0.5)' : 'rgba(150, 150, 150, 0.2)')
    .attr('stroke-width', isFocused ? 1.5 : 0.8)
    .attr('stroke-dasharray', isFocused ? '0' : '5,5');

  label
    .attr('font-size', isFocused ? '14px' : '12px')
    .attr('fill', isFocused ? '#3b82f6' : '#666');
}
