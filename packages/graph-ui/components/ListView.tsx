'use client';

import React, { useState, useMemo } from 'react';
import { GraphData, Node } from '@/types/api';

interface ListViewProps {
  data: GraphData;
  onNodeClick: (node: Node) => void;
  selectedSectors?: string[];
}

type SortField = 'title' | 'difficulty' | 'acceptanceRate' | 'freqBar';
type SortOrder = 'asc' | 'desc';

export default function ListView({ data, onNodeClick, selectedSectors = [] }: ListViewProps) {
  const [sortField, setSortField] = useState<SortField>('freqBar');
  const [sortOrder, setSortOrder] = useState<SortOrder>('desc');
  const [searchQuery, setSearchQuery] = useState('');

  // Filter and sort nodes
  const filteredAndSortedNodes = useMemo(() => {
    let filtered = data.nodes;

    // Apply search filter
    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      filtered = filtered.filter(node =>
        node.title.toLowerCase().includes(query) ||
        node.tags.some(tag => tag.toLowerCase().includes(query))
      );
    }

    // Sort nodes
    const sorted = [...filtered].sort((a, b) => {
      let comparison = 0;

      switch (sortField) {
        case 'title':
          comparison = a.title.localeCompare(b.title);
          break;
        case 'difficulty':
          const difficultyOrder = { 'Easy': 1, 'Medium': 2, 'Hard': 3 };
          comparison = difficultyOrder[a.difficulty as keyof typeof difficultyOrder] - 
                      difficultyOrder[b.difficulty as keyof typeof difficultyOrder];
          break;
        case 'acceptanceRate':
          comparison = a.acceptanceRate - b.acceptanceRate;
          break;
        case 'freqBar':
          comparison = (a.freqBar || 0) - (b.freqBar || 0);
          break;
      }

      return sortOrder === 'asc' ? comparison : -comparison;
    });

    return sorted;
  }, [data.nodes, sortField, sortOrder, searchQuery]);

  const handleSort = (field: SortField) => {
    if (sortField === field) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortOrder('desc');
    }
  };

  const getSortIcon = (field: SortField) => {
    if (sortField !== field) return '⇅';
    return sortOrder === 'asc' ? '↑' : '↓';
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'Easy': return 'text-green-400 bg-green-950';
      case 'Medium': return 'text-yellow-400 bg-yellow-950';
      case 'Hard': return 'text-red-400 bg-red-950';
      default: return 'text-gray-400 bg-gray-800';
    }
  };

  return (
    <div className="flex flex-col h-full bg-black">
      {/* Header with search and controls */}
      <div className="p-4 border-b border-gray-800 bg-gray-900">
        <div className="flex items-center gap-4 mb-4">
          <input
            type="text"
            placeholder="Search problems or tags..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="flex-1 px-4 py-3 border border-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white placeholder-gray-400"
          />
          <div className="text-sm text-gray-300 font-medium whitespace-nowrap">
            {filteredAndSortedNodes.length} of {data.nodes.length} problems
          </div>
        </div>

        {selectedSectors.length > 0 && (
          <div className="flex flex-wrap gap-2 items-center">
            <span className="text-sm text-gray-300 font-medium">Filtered by:</span>
            {selectedSectors.map(sector => (
              <span key={sector} className="px-3 py-1 bg-blue-900 text-blue-300 text-sm rounded-md font-medium">
                {sector}
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Table */}
      <div className="flex-1 overflow-auto bg-black">
        <table className="w-full">
          <thead className="bg-gray-900 sticky top-0 z-10 border-b-2 border-gray-700">
            <tr>
              <th className="px-6 py-4 text-left">
                <button
                  onClick={() => handleSort('title')}
                  className="font-semibold text-sm text-gray-200 hover:text-blue-400 flex items-center gap-2 transition-colors"
                >
                  Problem {getSortIcon('title')}
                </button>
              </th>
              <th className="px-6 py-4 text-left w-32">
                <button
                  onClick={() => handleSort('difficulty')}
                  className="font-semibold text-sm text-gray-200 hover:text-blue-400 flex items-center gap-2 transition-colors"
                >
                  Difficulty {getSortIcon('difficulty')}
                </button>
              </th>
              <th className="px-6 py-4 text-left w-32">
                <button
                  onClick={() => handleSort('acceptanceRate')}
                  className="font-semibold text-sm text-gray-200 hover:text-blue-400 flex items-center gap-2 transition-colors"
                >
                  Acceptance {getSortIcon('acceptanceRate')}
                </button>
              </th>
              <th className="px-6 py-4 text-left w-40">
                <button
                  onClick={() => handleSort('freqBar')}
                  className="font-semibold text-sm text-gray-200 hover:text-blue-400 flex items-center gap-2 transition-colors"
                >
                  Frequency {getSortIcon('freqBar')}
                </button>
              </th>
              <th className="px-6 py-4 text-left text-sm font-semibold text-gray-200">Tags</th>
              <th className="px-6 py-4 text-center w-20 text-sm font-semibold text-gray-200">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {filteredAndSortedNodes.map((node) => (
              <tr
                key={node.id}
                onClick={() => onNodeClick(node)}
                className="hover:bg-gray-900 cursor-pointer transition-colors"
              >
                <td className="px-6 py-4">
                  <div className="font-medium text-base text-gray-100">{node.title}</div>
                  <div className="text-sm text-gray-400 mt-1">{node.titleSlug}</div>
                </td>
                <td className="px-6 py-4">
                  <span className={`px-3 py-1.5 rounded-md text-sm font-semibold ${getDifficultyColor(node.difficulty)}`}>
                    {node.difficulty}
                  </span>
                </td>
                <td className="px-6 py-4 text-base text-gray-100 font-medium">
                  {node.acceptanceRate.toFixed(1)}%
                </td>
                <td className="px-6 py-4">
                  <div className="flex items-center gap-3">
                    <div className="flex-1 bg-gray-800 rounded-full h-3 overflow-hidden">
                      <div
                        className="bg-blue-500 h-full rounded-full transition-all"
                        style={{ width: `${(node.freqBar || 0) * 10}%` }}
                      />
                    </div>
                    <span className="text-sm text-gray-300 font-medium w-8 text-right">
                      {node.freqBar || 0}
                    </span>
                  </div>
                </td>
                <td className="px-6 py-4">
                  <div className="flex flex-wrap gap-1.5">
                    {node.tags.slice(0, 3).map(tag => (
                      <span
                        key={tag}
                        className="px-2.5 py-1 bg-gray-800 text-gray-300 text-xs rounded font-medium"
                      >
                        {tag}
                      </span>
                    ))}
                    {node.tags.length > 3 && (
                      <span className="px-2.5 py-1 text-gray-500 text-xs font-medium">
                        +{node.tags.length - 3}
                      </span>
                    )}
                  </div>
                </td>
                <td className="px-6 py-4 text-center">
                  {node.solved ? (
                    <span className="text-green-500 font-bold text-xl">✓</span>
                  ) : (
                    <span className="text-gray-600 text-xl">○</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {filteredAndSortedNodes.length === 0 && (
          <div className="text-center py-16 text-gray-400">
            <div className="text-lg font-medium mb-2">No problems found</div>
            <div className="text-sm">Try adjusting your search or filters</div>
          </div>
        )}
      </div>
    </div>
  );
}
