
export interface Node {
  id: number;
  title: string;
  titleSlug: string;
  difficulty: string;
  tags: string[];
  acceptanceRate: number;
  totalSubmissions: number;
  solved: boolean;
  freqBar: number;
}

export interface Edge {
  source: number;
  target: number;
  type: 'explicit' | 'tag_similarity';
  sharedTags?: number;
}

export interface GraphStats {
  totalProblems: number;
  totalMatching: number;
  totalEdges: number;
  explicitEdges: number;
  tagEdges: number;
  solvedProblems: number;
  unsolvedProblems: number;
}

export interface GraphData {
  nodes: Node[];
  edges: Edge[];
  stats: GraphStats;
}

export interface SubmissionHistory {
  id: string;
  status: string;
  createdAt: string;
  timeSpentMinutes?: number;
  isCheat: boolean;
  content?: string;
}

export interface ProblemDetail {
  title: string;
  titleSlug: string;
  difficulty: string;
  tags: string[];
  relatedProblems: string[];
  content?: string;
  acceptanceRate: number;
  totalSubmissions: number;
  solved: boolean;
  submissions: SubmissionHistory[];
}

export interface Stats {
  totalProblems: number;
  solvedCount: number;
  totalSubmissions: number;
  acceptanceRate: number;
}
