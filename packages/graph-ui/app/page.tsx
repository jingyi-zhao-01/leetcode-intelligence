'use client';

import React, { useState } from 'react';
import useSWR from 'swr';
import ForceGraph from '@/components/ForceGraph';
import ListView from '@/components/ListView';
import { GraphData, Node, ProblemDetail } from '@/types/api';
import { api } from '@/lib/api';

const fetcher = (url: string) => fetch(url).then(res => res.json());

type ViewMode = 'graph' | 'list';
type TagMode = 'OR' | 'AND';

export default function Home() {
  const [viewMode, setViewMode] = useState<ViewMode>('graph');
  const [tagMode, setTagMode] = useState<TagMode>('OR');
  const [filters, setFilters] = useState({
    solved: false,
    includeTags: [] as string[],
    filterTags: [] as string[],
    limit: 100,
    difficulties: ['Medium'] as string[],
  });
  const [selectedSectors, setSelectedSectors] = useState<string[]>([]);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [sectorsToExpand, setSectorsToExpand] = useState<string[]>([]);
  const [isLeftSidebarCollapsed, setIsLeftSidebarCollapsed] = useState(false);
  const [isRightSidebarCollapsed, setIsRightSidebarCollapsed] = useState(false);
  const [isFilterMenuCollapsed, setIsFilterMenuCollapsed] = useState(false);
  const [tagSearch, setTagSearch] = useState('');
  const [showExplicitOnly, setShowExplicitOnly] = useState(false);
  const [showExplicitRelations, setShowExplicitRelations] = useState(false);
  const [relatedNodes, setRelatedNodes] = useState<Set<number>>(new Set());

  
  // Fetch graph data
  const { data: graphData, error: graphError, isLoading: graphLoading } = useSWR<GraphData>(
    api.graph(filters),
    fetcher
  );

  // Fetch available tags
  const { data: availableTags } = useSWR<string[]>(api.tags(), fetcher);

  // Fetch problem details when node is selected
  const { data: problemDetail } = useSWR<ProblemDetail>(
    selectedNode ? api.problem(selectedNode.titleSlug) : null,
    fetcher
  );

  const handleNodeClick = (node: Node) => {
    console.log('Node clicked:', node.id, 'Auto-select enabled:', showExplicitRelations);
    setSelectedNode(node);
    
    // If auto-select is enabled, find all nodes with explicit relationships
    if (showExplicitRelations && graphData) {
      const related = new Set<number>();
      related.add(node.id);
      
      console.log('Total edges in graph:', graphData.edges.length);
      
      // Find all explicit edges connected to this node
      let explicitCount = 0;
      graphData.edges.forEach(edge => {
        if (edge.type === 'explicit') {
          explicitCount++;
          if (edge.source === node.id) {
            related.add(edge.target);
            console.log('Found explicit edge to target:', edge.target);
          } else if (edge.target === node.id) {
            related.add(edge.source);
            console.log('Found explicit edge from source:', edge.source);
          }
        }
      });
      
      console.log('Total explicit edges in graph:', explicitCount);
      console.log('Total related nodes:', related.size, Array.from(related));
      setRelatedNodes(related);
    } else {
      setRelatedNodes(new Set([node.id]));
    }
  };

  const handleFilterChange = (key: string, value: any) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  };

  // Calculate problem counts per tag
  const sectorCounts = React.useMemo(() => {
    if (!graphData) return new Map<string, number>();
    const counts = new Map<string, number>();
    graphData.nodes.forEach(node => {
      node.tags.forEach(tag => {
        counts.set(tag, (counts.get(tag) || 0) + 1);
      });
    });
    return counts;
  }, [graphData]);

  // Filter graph data to only show selected sectors
  const filteredGraphData = React.useMemo(() => {
    if (!graphData || selectedSectors.length === 0) return graphData;
    
    const filteredNodes = graphData.nodes.filter(node => 
      node.tags.some(tag => selectedSectors.includes(tag))
    );
    
    const nodeIds = new Set(filteredNodes.map(n => n.id));
    let filteredEdges = graphData.edges.filter(edge => 
      nodeIds.has(edge.source) && nodeIds.has(edge.target)
    );

    // If showExplicitOnly is enabled, filter to only explicit relationships
    if (showExplicitOnly) {
      filteredEdges = filteredEdges.filter(edge => edge.isExplicit === true);
    }
    
    return {
      ...graphData,
      nodes: filteredNodes,
      edges: filteredEdges,
      stats: {
        ...graphData.stats,
        totalProblems: filteredNodes.length,
        totalEdges: filteredEdges.length,
      }
    };
  }, [graphData, selectedSectors, showExplicitOnly]);

  return (
    <div className="flex h-screen bg-black">
      {/* Left Sidebar - Filters */}
      {!isLeftSidebarCollapsed && (
        <div className="w-64 p-4 border-r border-gray-800 overflow-y-auto bg-gray-900">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-bold text-gray-100">Filters</h2>
            <button
              onClick={() => setIsLeftSidebarCollapsed(true)}
              className="text-gray-400 hover:text-gray-200 p-1 rounded hover:bg-gray-800"
              title="Collapse sidebar"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
              </svg>
            </button>
          </div>
        
        <div className="mb-4">
          <label className="flex items-center text-gray-300">
            <input
              type="checkbox"
              checked={filters.solved}
              onChange={(e) => handleFilterChange('solved', e.target.checked)}
              className="mr-2" />
            Show Only Solved
          </label>
        </div>

        <div className="mb-4">
          <label className="flex items-center text-gray-300">
            <input
              type="checkbox"
              checked={showExplicitOnly}
              onChange={(e) => setShowExplicitOnly(e.target.checked)}
              className="mr-2"
            />
            Show Explicit Relationships Only
          </label>
        </div>

        <div className="mb-4">
          <label className="flex items-center text-gray-300">
            <input
              type="checkbox"
              checked={showExplicitRelations}
              onChange={(e) => setShowExplicitRelations(e.target.checked)}
              className="mr-2"
            />
            Auto-Select Explicit Relations
          </label>
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium text-gray-300">
            Limit
          </label>
          <input
            type="number"
            value={filters.limit}
            onChange={(e) => handleFilterChange('limit', parseInt(e.target.value))}
            className="w-full p-2 border border-gray-700 rounded bg-gray-800 text-gray-100"
            min="1"
            max="5000"
          />
        </div>

        {availableTags && (
          <div className="mb-4">
            <p className="text-xs text-gray-400">
              Available tags: {availableTags.length}
            </p>
          </div>
        )}

        {graphData && (
          <div className="mt-6 p-3 bg-gray-800 rounded border border-gray-700">
            <h3 className="font-medium mb-2 text-gray-200">Stats</h3>
            <div className="text-sm space-y-1">
              <div className="font-semibold text-blue-400">
                Found: {graphData.stats.totalMatching} problems
              </div>
              <div className="text-gray-400">
                Showing: {graphData.stats.totalProblems} of {graphData.stats.totalMatching}
              </div>
              <div className="text-gray-300">Solved: {graphData.stats.solvedProblems}</div>
              <div className="text-gray-300">Unsolved: {graphData.stats.unsolvedProblems}</div>
              <div className="text-gray-300">Edges: {graphData.stats.totalEdges}</div>
            </div>
          </div>
        )}
      </div>
      )}

      {/* Expand Left Sidebar Button */}
      {isLeftSidebarCollapsed && (
        <div className="flex items-center border-r border-gray-800 bg-gray-900 px-1">
          <button
            onClick={() => setIsLeftSidebarCollapsed(false)}
            className="text-gray-400 hover:text-gray-200 p-2 rounded hover:bg-gray-800"
            title="Expand sidebar"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 5l7 7-7 7M5 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      )}

      {/* Center - Graph */}
      <div className="flex-1 flex flex-col bg-black">
        <div className="border-b border-gray-800 bg-gray-900">
          <div className="p-4 flex items-center justify-between">
            <h1 className="text-2xl font-bold text-gray-100">LeetCode Problem Graph</h1>
            <div className="flex gap-2">
              <button
                onClick={() => setIsFilterMenuCollapsed(!isFilterMenuCollapsed)}
                className="px-3 py-2 rounded-lg font-medium bg-gray-800 text-gray-300 hover:bg-gray-700 transition-colors flex items-center gap-2"
                title={isFilterMenuCollapsed ? 'Show filters' : 'Hide filters'}
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                </svg>
                {isFilterMenuCollapsed ? 'Show' : 'Hide'} Filters
              </button>
            
              
              <button
                onClick={() => setViewMode('graph')}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                  viewMode === 'graph'
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
                }`}
              >
                Graph View
              </button>
              <button
                onClick={() => setViewMode('list')}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                  viewMode === 'list'
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
                }`}
              >
                List View
              </button>
            </div>
          </div>
          
          {/* Tag Filter Controls */}
          {!isFilterMenuCollapsed && (
          <div className="px-4 pb-4 space-y-3">
            {/* Difficulty Filter */}
            <div className="flex items-center gap-3">
              <span className="text-sm text-gray-400 font-medium">Difficulty:</span>
              <div className="flex gap-2">
                {['Easy', 'Medium', 'Hard'].map((difficulty) => (
                  <button
                    key={difficulty}
                    onClick={() => {
                      const isSelected = filters.difficulties.includes(difficulty);
                      const newDifficulties = isSelected
                        ? filters.difficulties.filter(d => d !== difficulty)
                        : [...filters.difficulties, difficulty];
                      handleFilterChange('difficulties', newDifficulties);
                    }}
                    className={`px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${
                      filters.difficulties.includes(difficulty)
                        ? difficulty === 'Easy'
                          ? 'bg-green-700 text-white'
                          : difficulty === 'Medium'
                          ? 'bg-yellow-700 text-white'
                          : 'bg-red-700 text-white'
                        : 'bg-gray-800 text-gray-400 hover:bg-gray-700'
                    }`}
                  >
                    {difficulty}
                  </button>
                ))}
              </div>
            </div>

            {/* Tag Mode Toggle */}
            <div className="flex items-center gap-3">
              <span className="text-sm text-gray-400 font-medium">Filter Mode:</span>
              <div className="flex gap-2">
                <button
                  onClick={() => {
                    setTagMode('OR');
                    handleFilterChange('filterTags', []);
                  }}
                  className={`px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${
                    tagMode === 'OR'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-800 text-gray-400 hover:bg-gray-700'
                  }`}
                >
                  Include Tags (OR)
                </button>
                <button
                  onClick={() => {
                    setTagMode('AND');
                    handleFilterChange('includeTags', []);
                  }}
                  className={`px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${
                    tagMode === 'AND'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-800 text-gray-400 hover:bg-gray-700'
                  }`}
                >
                  Filter Tags (AND)
                </button>
              </div>
            </div>

            {/* Tag Search */}
            <div>
              <input
                type="text"
                placeholder="Search tags..."
                value={tagSearch}
                onChange={(e) => setTagSearch(e.target.value)}
                className="w-full px-3 py-2 bg-gray-800 border border-gray-700 rounded text-gray-300 placeholder-gray-500 focus:outline-none focus:border-blue-500"
              />
            </div>

            {/* Tag Selection */}
            <div className="flex flex-wrap gap-2 max-h-32 overflow-y-auto p-2 bg-gray-800 rounded border border-gray-700">
              {availableTags?.filter(tag => tag.toLowerCase().includes(tagSearch.toLowerCase())).map((tag) => {
                const isSelected = tagMode === 'OR' 
                  ? filters.includeTags.includes(tag)
                  : filters.filterTags.includes(tag);
                const count = sectorCounts.get(tag) || 0;
                
                return (
                  <button
                    key={tag}
                    onClick={() => {
                      if (tagMode === 'OR') {
                        const newTags = isSelected
                          ? filters.includeTags.filter(t => t !== tag)
                          : [...filters.includeTags, tag];
                        handleFilterChange('includeTags', newTags);
                      } else {
                        const newTags = isSelected
                          ? filters.filterTags.filter(t => t !== tag)
                          : [...filters.filterTags, tag];
                        handleFilterChange('filterTags', newTags);
                      }
                    }}
                    className={`px-2.5 py-1 rounded text-xs font-medium transition-colors ${
                      isSelected
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                    }`}
                  >
                    {tag} ({count})
                  </button>
                );
              })}
            </div>

            {/* Active Filters Display */}
            {(filters.includeTags.length > 0 || filters.filterTags.length > 0) && (
              <div className="flex items-center gap-2 text-sm">
                <span className="text-gray-400">Active filters:</span>
                {tagMode === 'OR' && filters.includeTags.length > 0 && (
                  <span className="text-blue-400">
                    {filters.includeTags.length} tag{filters.includeTags.length > 1 ? 's' : ''} (OR)
                  </span>
                )}
                {tagMode === 'AND' && filters.filterTags.length > 0 && (
                  <span className="text-blue-400">
                    {filters.filterTags.length} tag{filters.filterTags.length > 1 ? 's' : ''} (AND)
                  </span>
                )}
                <button
                  onClick={() => {
                    handleFilterChange('includeTags', []);
                    handleFilterChange('filterTags', []);
                  }}
                  className="text-xs text-gray-400 hover:text-gray-200 underline"
                >
                  Clear
                </button>
              </div>
            )}

            {/* Group by Sectors - Only shown when filters are active */}
            {(filters.includeTags.length > 0 || filters.filterTags.length > 0) && (
              <div>
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-sm text-gray-400 font-medium">Group by Sectors:</span>
                  {selectedSectors.length > 0 && (
                    <span className="text-xs text-gray-500">({selectedSectors.length} selected)</span>
                  )}
                </div>
                <div className="flex flex-wrap gap-2 p-2 bg-gray-800 rounded border border-gray-700">
                  {availableTags
                    ?.filter(tag => {
                      const count = sectorCounts.get(tag) || 0;
                      const isInPrimaryFilter = filters.includeTags.includes(tag) || filters.filterTags.includes(tag);
                      return selectedSectors.includes(tag) && count > 0 && !isInPrimaryFilter;
                    })
                    .sort((a, b) => (sectorCounts.get(b) || 0) - (sectorCounts.get(a) || 0))
                    .map((tag) => {
                      const count = sectorCounts.get(tag) || 0;
                      return (
                        <button
                          key={tag}
                          onClick={() => {
                            setSelectedSectors(selectedSectors.filter(t => t !== tag));
                          }}
                          className="px-2.5 py-1 rounded text-xs font-medium transition-colors bg-green-700 text-white hover:bg-green-600 flex items-center gap-1"
                        >
                          {tag} ({count})
                          <span className="text-xs">×</span>
                        </button>
                      );
                    })}
                  {availableTags
                    ?.filter(tag => {
                      const count = sectorCounts.get(tag) || 0;
                      const isInPrimaryFilter = filters.includeTags.includes(tag) || filters.filterTags.includes(tag);
                      return !selectedSectors.includes(tag) && count > 0 && !isInPrimaryFilter;
                    })
                    .sort((a, b) => (sectorCounts.get(b) || 0) - (sectorCounts.get(a) || 0))
                    .map((tag) => {
                      const count = sectorCounts.get(tag) || 0;
                      return (
                        <button
                          key={tag}
                          onClick={() => {
                            setSelectedSectors([...selectedSectors, tag]);
                          }}
                          className="px-2.5 py-1 rounded text-xs font-medium transition-colors bg-gray-700 text-gray-400 hover:bg-gray-600"
                        >
                          {tag} ({count})
                        </button>
                      );
                    })}
                </div>
                <p className="text-xs text-gray-500 mt-1">
                  Select sectors to group and filter graph view. Only selected sectors will be shown.
                </p>
              </div>
            )}
          </div>
          )}
        </div>
        <div className="flex-1">
          {graphLoading && (
            <div className="flex items-center justify-center h-full">
              <p className="text-gray-400">Loading graph...</p>
            </div>
          )}
          {graphError && (
            <div className="flex items-center justify-center h-full">
              <p className="text-red-400">Error loading graph</p>
            </div>
          )}
          {graphData && !graphLoading && (
            <>
              {viewMode === 'graph' && (
                <ForceGraph
                  data={filteredGraphData || graphData}
                  onNodeClick={handleNodeClick}
                  selectedSectors={selectedSectors}
                  sectorsToExpand={sectorsToExpand}
                  onSectorsToExpandChange={setSectorsToExpand}
                  selectedNode={selectedNode}
                  relatedNodes={relatedNodes}
                />
              )}
              {viewMode === 'list' && (
                <ListView
                  data={graphData}
                  onNodeClick={handleNodeClick}
                  selectedSectors={selectedSectors}
                />
              )}
            </>
          )}
        </div>
      </div>

      {/* Right Sidebar - Problem Details */}
      {!isRightSidebarCollapsed && (
        <div className="w-80 p-4 border-l border-gray-800 overflow-y-auto bg-gray-900">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-semibold text-gray-300">Problem Details</h3>
            <button
              onClick={() => setIsRightSidebarCollapsed(true)}
              className="text-gray-400 hover:text-gray-200 p-1 rounded hover:bg-gray-800"
              title="Collapse sidebar"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 5l7 7-7 7M5 5l7 7-7 7" />
              </svg>
            </button>
          </div>
          {selectedNode ? (
          <div>
            <h2 className="text-lg font-bold mb-3 text-gray-100">{selectedNode.title}</h2>
            
            <div className="mb-6">
              <span className={`inline-block px-3 py-1 rounded-md text-sm font-medium ${
                selectedNode.difficulty === 'Easy' ? 'bg-green-950 text-green-400' :
                selectedNode.difficulty === 'Medium' ? 'bg-yellow-950 text-yellow-400' : 'bg-red-950 text-red-400'
              }`}>
                {selectedNode.difficulty}
              </span>
              {selectedNode.solved && (
                <span className="ml-2 inline-block px-3 py-1 rounded-md text-sm font-medium bg-blue-950 text-blue-400">
                  ✓ Solved
                </span>
              )}
            </div>

            <div className="mb-6">
              <p className="text-xs text-gray-400 mb-1">Acceptance Rate</p>
              <p className="text-3xl font-bold text-gray-100">{selectedNode.acceptanceRate}%</p>
            </div>

            <div className="mb-6">
              <p className="text-xs text-gray-400 mb-2">Tags</p>
              <div className="flex flex-wrap gap-2">
                {selectedNode.tags.map(tag => (
                  <span key={tag} className="px-3 py-1.5 bg-gray-800 hover:bg-gray-700 rounded-md text-xs font-medium text-gray-300 transition-colors">
                    {tag}
                  </span>
                ))}
              </div>
            </div>

            {problemDetail && (
              <>
                <div className="mb-6">
                  <p className="text-xs text-gray-400">Submissions: <span className="font-semibold text-gray-200">{problemDetail.totalSubmissions}</span></p>
                </div>

                {problemDetail.submissions.length > 0 && (
                  <div className="mb-4">
                    <p className="text-sm font-medium mb-2 text-gray-200">Recent Submissions</p>
                    <div className="space-y-2 max-h-40 overflow-y-auto">
                      {problemDetail.submissions.slice(0, 5).map(sub => (
                        <div key={sub.id} className="text-xs p-2 bg-gray-800 rounded border border-gray-700">
                          <div className={`font-medium ${
                            sub.status === 'Accepted' ? 'text-green-400' : 'text-red-400'
                          }`}>
                            {sub.status}
                          </div>
                          <div className="text-gray-400">
                            {new Date(sub.createdAt).toLocaleDateString()}
                          </div>
                          {sub.timeSpentMinutes && (
                            <div className="text-gray-400">
                              {sub.timeSpentMinutes} min
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {problemDetail.relatedProblems.length > 0 && (
                  <div>
                    <p className="text-sm font-semibold mb-3 text-gray-200">Related Problems</p>
                    <div className="space-y-2">
                      {problemDetail.relatedProblems.slice(0, 5).map(slug => (
                        <div key={slug} className="text-sm text-blue-400 hover:text-blue-300 hover:underline cursor-pointer transition-colors">
                          {slug}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </>
            )}
          </div>
        ) : (
          <div className="text-center text-gray-500 mt-10">
            <p>Click on a node to see details</p>
          </div>
        )}
      </div>
      )}

      {/* Right Sidebar Expand Button */}
      {isRightSidebarCollapsed && (
        <div className="w-8 bg-gray-900 border-l border-gray-800 flex items-center justify-center">
          <button
            onClick={() => setIsRightSidebarCollapsed(false)}
            className="text-gray-400 hover:text-gray-200 p-2 rounded hover:bg-gray-800"
            title="Expand sidebar"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
            </svg>
          </button>
        </div>
      )}
    </div>
  );
}