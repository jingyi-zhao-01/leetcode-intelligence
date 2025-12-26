'use client';

import React, { useState } from 'react';
import useSWR from 'swr';
import ForceGraph from '@/components/ForceGraph';
import { GraphData, Node, ProblemDetail } from '@/types/api';
import { api } from '@/lib/api';

const fetcher = (url: string) => fetch(url).then(res => res.json());

export default function Home() {
  const [filters, setFilters] = useState({
    solved: false,
    includeTags: [] as string[],
    filterTags: [] as string[],
    limit: 100,
    difficulties: [] as string[],
  });
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  
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
    setSelectedNode(node);
  };

  const handleFilterChange = (key: string, value: any) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  };

  return (
    <div className="flex h-screen">
      {/* Left Sidebar - Filters */}
      <div className="w-64 p-4 border-r overflow-y-auto">
        <h2 className="text-xl font-bold mb-4">Filters</h2>
        
        <div className="mb-4">
          <label className="flex items-center">
            <input
              type="checkbox"
              checked={filters.solved}
              onChange={(e) => handleFilterChange('solved', e.target.checked)}
              className="mr-2"
            />
            Show Only Solved
          </label>
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">
            Difficulty
          </label>
          <div className="space-y-2">
            {['Easy', 'Medium', 'Hard'].map((difficulty) => (
              <label key={difficulty} className="flex items-center">
                <input
                  type="checkbox"
                  checked={filters.difficulties.includes(difficulty)}
                  onChange={(e) => {
                    const newDifficulties = e.target.checked
                      ? [...filters.difficulties, difficulty]
                      : filters.difficulties.filter(d => d !== difficulty);
                    handleFilterChange('difficulties', newDifficulties);
                  }}
                  className="mr-2"
                />
                <span className={`
                  ${difficulty === 'Easy' ? 'text-green-600' : ''}
                  ${difficulty === 'Medium' ? 'text-orange-600' : ''}
                  ${difficulty === 'Hard' ? 'text-red-600' : ''}
                `}>
                  {difficulty}
                </span>
              </label>
            ))}
          </div>
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">
            Limit
          </label>
          <input
            type="number"
            value={filters.limit}
            onChange={(e) => handleFilterChange('limit', parseInt(e.target.value))}
            className="w-full p-2 border rounded"
            min="1"
            max="5000"
          />
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">
            Include Tags (OR)
            {filters.includeTags.length > 0 && (
              <span className="ml-2 text-xs text-gray-500">({filters.includeTags.length} selected)</span>
            )}
          </label>
          <div className={`max-h-40 overflow-y-auto space-y-1 border rounded p-2 ${
            filters.filterTags.length > 0 ? 'opacity-50 bg-gray-100' : ''
          }`}>
            {availableTags?.map((tag) => (
              <label key={tag} className="flex items-center text-xs">
                <input
                  type="checkbox"
                  checked={filters.includeTags.includes(tag)}
                  disabled={filters.filterTags.length > 0}
                  onChange={(e) => {
                    const newTags = e.target.checked
                      ? [...filters.includeTags, tag]
                      : filters.includeTags.filter(t => t !== tag);
                    handleFilterChange('includeTags', newTags);
                  }}
                  className="mr-2"
                />
                {tag}
              </label>
            ))}
          </div>
          {filters.filterTags.length > 0 && (
            <p className="text-xs text-orange-600 mt-1">Disabled: Filter Tags (AND) is active</p>
          )}
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">
            Filter Tags (AND)
            {filters.filterTags.length > 0 && (
              <span className="ml-2 text-xs text-gray-500">({filters.filterTags.length} selected)</span>
            )}
          </label>
          <div className={`max-h-40 overflow-y-auto space-y-1 border rounded p-2 ${
            filters.includeTags.length > 0 ? 'opacity-50 bg-gray-100' : ''
          }`}>
            {availableTags?.map((tag) => (
              <label key={tag} className="flex items-center text-xs">
                <input
                  type="checkbox"
                  checked={filters.filterTags.includes(tag)}
                  disabled={filters.includeTags.length > 0}
                  onChange={(e) => {
                    const newTags = e.target.checked
                      ? [...filters.filterTags, tag]
                      : filters.filterTags.filter(t => t !== tag);
                    handleFilterChange('filterTags', newTags);
                  }}
                  className="mr-2"
                />
                {tag}
              </label>
            ))}
          </div>
          {filters.includeTags.length > 0 && (
            <p className="text-xs text-orange-600 mt-1">Disabled: Include Tags (OR) is active</p>
          )}
        </div>

        {availableTags && (
          <div className="mb-4">
            <p className="text-xs text-gray-600">
              Available tags: {availableTags.length}
            </p>
          </div>
        )}

        {graphData && (
          <div className="mt-6 p-3 bg-gray-100 rounded">
            <h3 className="font-medium mb-2">Stats</h3>
            <div className="text-sm space-y-1">
              <div className="font-semibold text-blue-600">
                Found: {graphData.stats.totalMatching} problems
              </div>
              <div className="text-gray-600">
                Showing: {graphData.stats.totalProblems} of {graphData.stats.totalMatching}
              </div>
              <div>Solved: {graphData.stats.solvedProblems}</div>
              <div>Unsolved: {graphData.stats.unsolvedProblems}</div>
              <div>Edges: {graphData.stats.totalEdges}</div>
            </div>
          </div>
        )}
      </div>

      {/* Center - Graph */}
      <div className="flex-1 flex flex-col">
        <div className="p-4 border-b">
          <h1 className="text-2xl font-bold">LeetCode Problem Graph</h1>
        </div>
        <div className="flex-1">
          {graphLoading && (
            <div className="flex items-center justify-center h-full">
              <p>Loading graph...</p>
            </div>
          )}
          {graphError && (
            <div className="flex items-center justify-center h-full">
              <p className="text-red-500">Error loading graph</p>
            </div>
          )}
          {graphData && !graphLoading && (
            <ForceGraph data={graphData} onNodeClick={handleNodeClick} />
          )}
        </div>
      </div>

      {/* Right Sidebar - Problem Details */}
      <div className="w-80 p-4 border-l overflow-y-auto">
        {selectedNode ? (
          <div>
            <h2 className="text-xl font-bold mb-4">{selectedNode.title}</h2>
            
            <div className="mb-4">
              <span className={`inline-block px-2 py-1 rounded text-sm ${
                selectedNode.difficulty === 'Easy' ? 'bg-green-200' :
                selectedNode.difficulty === 'Medium' ? 'bg-yellow-200' : 'bg-red-200'
              }`}>
                {selectedNode.difficulty}
              </span>
              {selectedNode.solved && (
                <span className="ml-2 inline-block px-2 py-1 rounded text-sm bg-blue-200">
                  ✓ Solved
                </span>
              )}
            </div>

            <div className="mb-4">
              <p className="text-sm text-gray-600">Acceptance Rate</p>
              <p className="text-2xl font-bold">{selectedNode.acceptanceRate}%</p>
            </div>

            <div className="mb-4">
              <p className="text-sm text-gray-600 mb-2">Tags</p>
              <div className="flex flex-wrap gap-1">
                {selectedNode.tags.map(tag => (
                  <span key={tag} className="px-2 py-1 bg-gray-200 rounded text-xs">
                    {tag}
                  </span>
                ))}
              </div>
            </div>

            {problemDetail && (
              <>
                <div className="mb-4">
                  <p className="text-sm text-gray-600 mb-2">Submissions: {problemDetail.totalSubmissions}</p>
                </div>

                {problemDetail.submissions.length > 0 && (
                  <div className="mb-4">
                    <p className="text-sm font-medium mb-2">Recent Submissions</p>
                    <div className="space-y-2 max-h-40 overflow-y-auto">
                      {problemDetail.submissions.slice(0, 5).map(sub => (
                        <div key={sub.id} className="text-xs p-2 bg-gray-50 rounded">
                          <div className={`font-medium ${
                            sub.status === 'Accepted' ? 'text-green-600' : 'text-red-600'
                          }`}>
                            {sub.status}
                          </div>
                          <div className="text-gray-500">
                            {new Date(sub.createdAt).toLocaleDateString()}
                          </div>
                          {sub.timeSpentMinutes && (
                            <div className="text-gray-500">
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
                    <p className="text-sm font-medium mb-2">Related Problems</p>
                    <div className="text-xs space-y-1">
                      {problemDetail.relatedProblems.slice(0, 5).map(slug => (
                        <div key={slug} className="text-blue-600">
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
    </div>
  );
}

//             Deploy Now
//           </a>
//           <a
//             className="flex h-12 w-full items-center justify-center rounded-full border border-solid border-black/[.08] px-5 transition-colors hover:border-transparent hover:bg-black/[.04] dark:border-white/[.145] dark:hover:bg-[#1a1a1a] md:w-[158px]"
//             href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             Documentation
//           </a>
//         </div>
//       </main>
//     </div>
//   );
// }
