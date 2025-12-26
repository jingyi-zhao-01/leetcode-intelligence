
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = {
  graph: (params: {
    solved?: boolean;
    includeTags?: string[];
    filterTags?: string[];
    limit?: number;
    difficulties?: string[];
  }) => {
    const searchParams = new URLSearchParams();
    if (params.solved) searchParams.append('solved', 'true');
    if (params.includeTags && params.includeTags.length > 0) {
      searchParams.append('include_tags', params.includeTags.join(','));
    }
    if (params.filterTags && params.filterTags.length > 0) {
      searchParams.append('filter_tags', params.filterTags.join(','));
    }
    if (params.limit) searchParams.append('limit', params.limit.toString());
    if (params.difficulties && params.difficulties.length > 0) {
      searchParams.append('difficulties', params.difficulties.join(','));
    }
    
    return `${API_BASE_URL}/api/graph?${searchParams.toString()}`;
  },
  
  problem: (titleSlug: string) => `${API_BASE_URL}/api/problems/${titleSlug}`,
  
  tags: () => `${API_BASE_URL}/api/tags`,
  
  stats: () => `${API_BASE_URL}/api/stats`,
};
