import type { CompanionChatMessage } from '../../core/companionChat.ts';
import type { ActiveSessionScope } from '../scope.ts';

export type SessionEndReason =
  | 'stop_timer'
  | 'drop_timer'
  | 'session_evicted'
  | 'accepted_restart'
  | 'process_shutdown'
  | 'failure_analysis';

export type SessionEndEvent = {
  reason: SessionEndReason;
  endedAt: string;
  elapsedMinutes?: number | null;
  replacedByTitleSlug?: string;
  forcePersist?: boolean;
};

export type SessionRecordPersister = {
  persist(scope: ActiveSessionScope, event: SessionEndEvent): Promise<void>;
};

export type RecalledSessionRecord = {
  id: string;
  memory: string;
  createdAt?: string;
  updatedAt?: string;
  metadata?: Record<string, unknown>;
};

export type SessionRecordRecallResult = {
  titleSlug: string;
  records: RecalledSessionRecord[];
};

export type SimilarityProfile = {
  patternTags: string[];
  stateTraits: string[];
  errorTags: string[];
  domainTags: string[];
  problemSummary?: string;
};

export type SimilarProblemRecallQuery = {
  titleSlug: string;
  title?: string;
  difficulty?: string;
  questionContent?: string;
  topicTags?: string[];
};

export type SimilarProblemMatch = {
  titleSlug: string;
  title?: string;
  difficulty?: string;
  score: number;
  overlap: {
    patternTags: string[];
    stateTraits: string[];
    errorTags: string[];
    domainTags: string[];
  };
  profile: SimilarityProfile;
  runId?: string;
  endedAt?: string;
  endReason?: string;
  latestFailureStatus?: string;
  failureSummary?: string;
  failureSummaries: string[];
  stuckPoints: string[];
  thoughtProcess: string[];
};

export type SimilarProblemRecallResult = {
  titleSlug: string;
  queryProfile: SimilarityProfile;
  matches: SimilarProblemMatch[];
};

export type RecalledMountSessionSummary = {
  runId?: string;
  endedAt?: string;
  endReason?: string;
  latestFailureStatus?: string;
  distinctMistakeCount?: number;
  failureSummary?: string;
  failureSummaries?: string[];
  stuckPoints: string[];
  thoughtProcess: string[];
};

export type SessionRecordRecaller = {
  recallByTitleSlug(titleSlug: string): Promise<SessionRecordRecallResult>;
  recallSimilarByQuery(query: SimilarProblemRecallQuery): Promise<SimilarProblemRecallResult>;
};

export type Mem0AddResponse = {
  eventId?: string;
  message?: string;
  status?: string;
};

export type MemoryClientLike = {
  add(
    messages: Array<{ role: 'user' | 'assistant'; content: string }>,
    options: Record<string, unknown>,
  ): Promise<unknown>;
};

export type MemoryClientConstructor = new (options: { apiKey: string; host?: string }) => MemoryClientLike;

export type Mem0SessionRecordPersisterOptions = {
  apiKey: string;
  userId: string;
  agentId?: string;
  appId?: string;
  host?: string;
  client?: MemoryClientLike;
};

export type Mem0GetAllResponse = {
  next?: string | null;
  results?: unknown;
};

export type Mem0SessionRecordRecallerOptions = {
  apiKey: string;
  userId: string;
  agentId?: string;
  appId?: string;
  host?: string;
  fetchImpl?: typeof fetch;
};

export type Mem0RenderedMessage = CompanionChatMessage;
