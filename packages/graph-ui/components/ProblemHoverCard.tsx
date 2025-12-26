'use client';

import React, { useState, useEffect } from 'react';
import useSWR from 'swr';
import { ProblemDetail, Node } from '@/types/api';
import { api } from '@/lib/api';

const fetcher = (url: string) => fetch(url).then(res => res.json());

interface ProblemHoverCardProps {
  node: Node;
  position: { x: number; y: number };
  onClose: () => void;
}

export default function ProblemHoverCard({ node, position, onClose }: ProblemHoverCardProps) {
  const [activeTab, setActiveTab] = useState<'description' | 'code'>('description');
  
  // Fetch problem details
  const { data: problemDetail, isLoading } = useSWR<ProblemDetail>(
    api.problem(node.titleSlug),
    fetcher
  );

  // Get accepted submissions
  const acceptedSubmissions = problemDetail?.submissions.filter(s => s.status === 'Accepted') || [];

  // Determine card position (keep it within viewport)
  const cardStyle: React.CSSProperties = {
    position: 'fixed',
    left: Math.min(position.x + 20, window.innerWidth - 620),
    top: Math.min(position.y - 50, window.innerHeight - 520),
    maxWidth: '600px',
    maxHeight: '500px',
    zIndex: 1000,
  };

  // Close on escape key
  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [onClose]);

  return (
    <>
      {/* Backdrop to close on click outside */}
      <div 
        className="fixed inset-0 z-[999]" 
        onClick={onClose}
      />
      
      {/* Hover Card */}
      <div 
        className="bg-white border-2 border-gray-300 rounded-lg shadow-2xl overflow-hidden"
        style={cardStyle}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-4">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <h3 className="text-lg font-bold mb-1">{node.title}</h3>
              <div className="flex items-center gap-2 text-sm">
                <span className={`px-2 py-0.5 rounded ${
                  node.difficulty === 'Easy' ? 'bg-green-500' :
                  node.difficulty === 'Medium' ? 'bg-orange-500' : 'bg-red-500'
                }`}>
                  {node.difficulty}
                </span>
                {node.solved && (
                  <span className="px-2 py-0.5 rounded bg-green-600">✓ Solved</span>
                )}
                <span className="px-2 py-0.5 rounded bg-blue-600">
                  {node.acceptanceRate.toFixed(1)}% accepted
                </span>
              </div>
            </div>
            <button 
              onClick={onClose}
              className="text-white hover:text-gray-200 text-xl font-bold ml-2"
            >
              ×
            </button>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex border-b border-gray-200">
          <button
            className={`flex-1 px-4 py-2 font-medium transition-colors ${
              activeTab === 'description'
                ? 'bg-blue-50 text-blue-600 border-b-2 border-blue-600'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
            onClick={() => setActiveTab('description')}
          >
            Description
          </button>
          <button
            className={`flex-1 px-4 py-2 font-medium transition-colors ${
              activeTab === 'code'
                ? 'bg-blue-50 text-blue-600 border-b-2 border-blue-600'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
            onClick={() => setActiveTab('code')}
            disabled={acceptedSubmissions.length === 0}
          >
            Code {acceptedSubmissions.length > 0 && `(${acceptedSubmissions.length})`}
          </button>
        </div>

        {/* Content */}
        <div className="p-4 overflow-y-auto" style={{ maxHeight: '400px' }}>
          {isLoading ? (
            <div className="flex items-center justify-center py-8">
              <div className="text-gray-500">Loading...</div>
            </div>
          ) : activeTab === 'description' ? (
            <div>
              {/* Tags */}
              {problemDetail?.tags && problemDetail.tags.length > 0 && (
                <div className="mb-4">
                  <div className="flex flex-wrap gap-1">
                    {problemDetail.tags.map((tag) => (
                      <span
                        key={tag}
                        className="px-2 py-1 text-xs bg-gray-100 text-gray-700 rounded"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Description */}
              {problemDetail?.content ? (
                <div 
                  className="prose prose-sm max-w-none"
                  dangerouslySetInnerHTML={{ __html: problemDetail.content }}
                />
              ) : (
                <div className="text-gray-500 text-sm">
                  No description available
                </div>
              )}

              {/* Stats */}
              <div className="mt-4 pt-4 border-t border-gray-200">
                <div className="grid grid-cols-2 gap-2 text-sm">
                  <div>
                    <span className="text-gray-600">Total Submissions:</span>
                    <span className="ml-2 font-medium">{problemDetail?.totalSubmissions || 0}</span>
                  </div>
                  <div>
                    <span className="text-gray-600">Acceptance Rate:</span>
                    <span className="ml-2 font-medium">{problemDetail?.acceptanceRate || 0}%</span>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div className="space-y-4">
              {acceptedSubmissions.length === 0 ? (
                <div className="text-center text-gray-500 py-8">
                  No accepted submissions yet
                </div>
              ) : (
                acceptedSubmissions.map((submission, idx) => (
                  <div key={submission.id} className="border border-gray-200 rounded-lg overflow-hidden">
                    <div className="bg-gray-50 px-3 py-2 flex items-center justify-between border-b border-gray-200">
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-medium text-gray-700">
                          Solution {acceptedSubmissions.length - idx}
                        </span>
                        {submission.isCheat && (
                          <span className="px-2 py-0.5 text-xs bg-yellow-100 text-yellow-800 rounded">
                            Needs Review
                          </span>
                        )}
                      </div>
                      <div className="text-xs text-gray-500">
                        {new Date(submission.createdAt).toLocaleDateString()}
                        {submission.timeSpentMinutes && (
                          <span className="ml-2">({submission.timeSpentMinutes}min)</span>
                        )}
                      </div>
                    </div>
                    {submission.content && (
                      <pre className="p-3 text-xs overflow-x-auto bg-gray-900 text-gray-100">
                        <code>{submission.content}</code>
                      </pre>
                    )}
                  </div>
                ))
              )}
            </div>
          )}
        </div>
      </div>
    </>
  );
}
