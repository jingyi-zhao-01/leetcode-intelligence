export type IntelligenceConfig = {
  DATABASE_URL: string;
  OPEN_ROUTER_API_KEY?: string;
  API_KEY?: string;
  MODEL: string;
  INTELLIGENCE_PORT: number;
  INTELLIGENCE_HOST: string;
  INTELLIGENCE_CRON: string;
  INTELLIGENCE_MAX_CANDIDATES: number;
  INTELLIGENCE_SELECTION_WINDOW: number;
  INTELLIGENCE_MIN_WEIGHT: number;
  INTELLIGENCE_MAX_WEIGHT: number;
};

export type CandidateSubmission = {
  id: string;
  titleSlug: string | null;
  content: string;
  status: string;
  createdAt: Date;
};

export type CandidateQuestion = {
  title: string;
  titleSlug: string;
  difficulty: string;
  content: string | null;
  topicTags: string[];
  freqBar: number | null;
};

export type IntelligencePromptEventRecord = {
  id: string;
  questionSlug: string;
  promptText: string;
  selectedAt: Date;
  weightBefore: number | null;
  Submission: CandidateSubmission;
  IntelligenceResponse: { id: string } | null;
};

export type LlmScore = {
  score: number;
  approachSummary: string;
  complexityNotes: string;
  blindSpots: string;
  tags: string[];
  reason: string;
};

export type ScoreRequest = {
  questionSlug: string;
  promptText: string;
  submission: CandidateSubmission;
  rawReply: string;
};

export type WeightedCandidate = {
  submission: CandidateSubmission;
  question: CandidateQuestion;
  weight: number;
};

export type PromptTransport = {
  channelId: string;
  messageId?: string | null;
};

export type PromptEventWithRelations = {
  id: string;
  questionSlug: string;
  promptText: string;
  selectedAt: Date;
  weightBefore: number | null;
  Submission: CandidateSubmission;
  Question: CandidateQuestion;
  IntelligenceResponse: { id: string } | null;
};

export interface ScoringAlgorithm {
  score(request: ScoreRequest): Promise<LlmScore>;
}
