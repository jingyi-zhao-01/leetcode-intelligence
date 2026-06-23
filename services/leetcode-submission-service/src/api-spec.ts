import { ServerAction } from './server.ts';

type FieldSpec = {
  name: string;
  type: string;
  required?: boolean;
  note?: string;
};

type ActionSpec = {
  action: ServerAction;
  summary: string;
  request: FieldSpec[];
  responseKeys: string[];
};

type HttpRouteSpec = {
  method: 'GET' | 'POST';
  path: string;
  summary: string;
  request?: FieldSpec[];
  responseKeys: string[];
};

export const submissionActionApiSpec: readonly ActionSpec[] = [
  {
    action: ServerAction.START_TIMER,
    summary: 'Start or reactivate the active timer for a LeetCode title slug.',
    request: [{ name: 'title_slug', type: 'string', required: true }],
    responseKeys: ['success', 'action', 'title_slug', 'already_active', 'evicted_title_slugs'],
  },
  {
    action: ServerAction.STOP_TIMER,
    summary: 'Stop the active timer for a title slug and persist its elapsed minutes.',
    request: [{ name: 'title_slug', type: 'string', required: true }],
    responseKeys: ['success', 'action', 'title_slug', 'minutes'],
  },
  {
    action: ServerAction.DROP_TIMER,
    summary: 'Stop an active timer and mark the session as dropped.',
    request: [{ name: 'title_slug', type: 'string', required: true }],
    responseKeys: ['success', 'action', 'title_slug'],
  },
  {
    action: ServerAction.GET_ACTIVE_TIMERS,
    summary: 'Read the in-memory timer map keyed by title slug.',
    request: [],
    responseKeys: ['success', 'action', 'timers'],
  },
  {
    action: ServerAction.GET_ACTIVE_SESSIONS,
    summary: 'List active sessions derived from the in-memory timer state.',
    request: [],
    responseKeys: ['success', 'action', 'sessions', 'count'],
  },
  {
    action: ServerAction.GET_PAST_SUBMISSIONS,
    summary: 'Fetch recent submissions for a title slug from cache plus persistence.',
    request: [
      { name: 'title_slug', type: 'string', required: true },
      { name: 'limit', type: 'number', note: 'clamped to 1..50, defaults to 10' },
    ],
    responseKeys: ['success', 'action', 'title_slug', 'submissions', 'count'],
  },
  {
    action: ServerAction.GET_MEM0_RECALL_SUMMARY,
    summary: 'Fetch recalled session history and similar-problem recall for a title slug.',
    request: [
      { name: 'title_slug', type: 'string', required: true },
      { name: 'title', type: 'string' },
      { name: 'difficulty', type: 'string' },
      { name: 'question_content', type: 'string' },
      { name: 'topic_tags', type: 'string[]' },
    ],
    responseKeys: [
      'success',
      'action',
      'title_slug',
      'record_count',
      'has_history',
      'summary',
      'sessions',
      'similar_match_count',
      'similar_summary',
      'similar_matches',
    ],
  },
  {
    action: ServerAction.SAVE_SUBMISSION,
    summary: 'Normalize, cache, and persist a submission payload.',
    request: [
      { name: 'title_slug', type: 'string', required: true },
      { name: 'content', type: 'string', required: true },
      { name: 'item', type: 'object', required: true, note: 'raw LeetCode submission payload' },
    ],
    responseKeys: ['success', 'action', 'title_slug'],
  },
  {
    action: ServerAction.ANALYZE_FAILURE,
    summary: 'Run LLM-backed failure analysis bound to the active submission session.',
    request: [
      { name: 'title_slug', type: 'string', required: true },
      { name: 'editor_content', type: 'string', required: true },
      { name: 'title', type: 'string' },
      { name: 'difficulty', type: 'string' },
      { name: 'topic_tags', type: 'string[]' },
      { name: 'question_content', type: 'string' },
      { name: 'submission_content', type: 'string' },
      { name: 'testcase', type: 'string' },
      { name: 'item', type: 'object' },
      { name: 'filetype', type: 'string' },
    ],
    responseKeys: ['success', 'action', 'event_id', 'title_slug', 'summary', 'annotations', 'count'],
  },
] as const;

export const companionHttpApiSpec: readonly HttpRouteSpec[] = [
  {
    method: 'GET',
    path: '/health',
    summary: 'Companion server health check.',
    responseKeys: ['status', 'service', 'port'],
  },
  {
    method: 'GET',
    path: '/v1/models',
    summary: 'List the configured companion models using an OpenAI-compatible shape.',
    responseKeys: ['object', 'data'],
  },
  {
    method: 'POST',
    path: '/v1/chat/completions',
    summary: 'Create a non-streaming or streaming OpenAI-compatible companion chat completion.',
    request: [
      { name: 'messages', type: 'object[]', required: true },
      { name: 'model', type: 'string' },
      { name: 'temperature', type: 'number' },
      { name: 'stream', type: 'boolean' },
    ],
    responseKeys: ['id', 'object', 'created', 'model', 'choices', 'usage'],
  },
] as const;
