import os from 'node:os';
import MemoryClient from 'mem0ai';
import type { CompanionChatMessage } from '../core/companionChat.ts';
import { createLogger } from '../logger.ts';
import type { ActiveSessionScope } from './scope.ts';

const logger = createLogger('session-mem0');

const DEFAULT_MEM0_APP_ID = 'leetcode-qa';
const DEFAULT_MEM0_AGENT_ID = 'leetcode-submission-service';
const MAX_TEXT_SECTION_CHARS = 6_000;
const MAX_JSON_SECTION_CHARS = 4_000;
const MAX_MESSAGE_CHARS = 1_200;
const MAX_COMPANION_TURNS = 12;
const MAX_SERVICE_UPDATES = 8;
const MAX_RECALLED_SESSION_RECORDS = 12;
const MAX_RECALLED_CODE_CHARS = 600;
const DEFAULT_MEM0_BASE_URL = 'https://api.mem0.ai';

export type SessionEndReason =
  | 'stop_timer'
  | 'drop_timer'
  | 'session_evicted'
  | 'accepted_restart'
  | 'process_shutdown';

export type SessionEndEvent = {
  reason: SessionEndReason;
  endedAt: string;
  elapsedMinutes?: number | null;
  replacedByTitleSlug?: string;
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

export type SessionRecordRecaller = {
  recallByTitleSlug(titleSlug: string): Promise<SessionRecordRecallResult>;
};

type Mem0AddResponse = {
  eventId?: string;
  message?: string;
  status?: string;
};

type MemoryClientLike = {
  add(
    messages: Array<{ role: 'user' | 'assistant'; content: string }>,
    options: Record<string, unknown>,
  ): Promise<unknown>;
};

type MemoryClientConstructor = new (options: { apiKey: string; host?: string }) => MemoryClientLike;

type Mem0SessionRecordPersisterOptions = {
  apiKey: string;
  userId: string;
  agentId?: string;
  appId?: string;
  host?: string;
  client?: MemoryClientLike;
};

type Mem0GetAllResponse = {
  next?: string | null;
  results?: unknown;
};

type Mem0SessionRecordRecallerOptions = {
  apiKey: string;
  userId: string;
  agentId?: string;
  appId?: string;
  host?: string;
  fetchImpl?: typeof fetch;
};

const readJudgeStatus = (judgeResult: unknown): string | null => {
  if (!judgeResult || typeof judgeResult !== 'object' || Array.isArray(judgeResult)) {
    return null;
  }

  const status = (judgeResult as { status_msg?: unknown }).status_msg;
  return typeof status === 'string' && status.trim().length > 0 ? status.trim() : null;
};

const truncate = (value: string, maxChars: number): string => {
  const trimmed = value.trim();
  if (trimmed.length <= maxChars) {
    return trimmed;
  }

  const clipped = trimmed.slice(0, maxChars).trimEnd();
  return `${clipped}\n\n[truncated ${trimmed.length - clipped.length} chars]`;
};

const truncateJson = (value: unknown): string => {
  try {
    return truncate(JSON.stringify(value, null, 2), MAX_JSON_SECTION_CHARS);
  } catch {
    return '"[unserializable judge result]"';
  }
};

const readStringValue = (value: unknown): string | undefined => {
  const normalized = typeof value === 'string' ? value.trim() : '';
  return normalized.length > 0 ? normalized : undefined;
};

const readMetadataRecord = (value: unknown): Record<string, unknown> | undefined => {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    return undefined;
  }

  return value as Record<string, unknown>;
};

const readMetadataString = (metadata: Record<string, unknown>, ...keys: string[]): string | undefined => {
  for (const key of keys) {
    const value = readStringValue(metadata[key]);
    if (value) {
      return value;
    }
  }

  return undefined;
};

const readMetadataNumber = (metadata: Record<string, unknown>, ...keys: string[]): number | null => {
  for (const key of keys) {
    const value = metadata[key];
    if (typeof value === 'number' && Number.isFinite(value)) {
      return value;
    }
  }

  return null;
};

const hasMarkdownSection = (content: string, heading: string): boolean =>
  new RegExp(`(^|\\n)## ${heading}(\\n|$)`).test(content);

const readMarkdownSection = (content: string, heading: string): string | undefined => {
  const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = content.match(new RegExp(`(?:^|\\n)## ${escapedHeading}\\n([\\s\\S]*?)(?=\\n## |$)`));
  const section = match?.[1]?.trim();
  return section && section.length > 0 ? section : undefined;
};

const stripCodeFence = (content: string): string => {
  const fenced = content.match(/^```[^\n]*\n([\s\S]*?)\n```$/);
  return fenced?.[1]?.trim() ?? content.trim();
};

const pushTextSection = (parts: string[], heading: string, content?: string): void => {
  if (!content || content.trim().length === 0) {
    return;
  }

  parts.push('', `## ${heading}`, truncate(content, MAX_TEXT_SECTION_CHARS));
};

const pushCodeSection = (parts: string[], heading: string, code: string | undefined, fence: string): void => {
  if (!code || code.trim().length === 0) {
    return;
  }

  parts.push('', `## ${heading}`, `\`\`\`${fence}`, truncate(code, MAX_TEXT_SECTION_CHARS), '```');
};

const pushMessagesSection = (
  parts: string[],
  heading: string,
  messages: CompanionChatMessage[] | undefined,
  maxItems: number,
): void => {
  if (!messages || messages.length === 0) {
    return;
  }

  parts.push('', `## ${heading}`);
  for (const message of messages.slice(-maxItems)) {
    parts.push(`- ${message.role}: ${truncate(message.content, MAX_MESSAGE_CHARS)}`);
  }
};

export function buildMem0RunId(scope: ActiveSessionScope): string {
  return `leetcode-session:${scope.titleSlug}:${scope.activatedAt}`;
}

export function renderPersistedSessionRecord(scope: ActiveSessionScope, event: SessionEndEvent): string {
  const parts = [
    '# LeetCode Session Record',
    '',
    `- Title Slug: ${scope.titleSlug}`,
    `- Run ID: ${buildMem0RunId(scope)}`,
    `- Activated At: ${scope.activatedAt}`,
    `- Ended At: ${event.endedAt}`,
    `- End Reason: ${event.reason}`,
  ];

  if (typeof event.elapsedMinutes === 'number' && Number.isFinite(event.elapsedMinutes)) {
    parts.push(`- Elapsed Minutes: ${event.elapsedMinutes}`);
  }

  if (event.replacedByTitleSlug) {
    parts.push(`- Replaced By Title Slug: ${event.replacedByTitleSlug}`);
  }

  if (scope.title) {
    parts.push(`- Title: ${scope.title}`);
  }

  if (scope.difficulty) {
    parts.push(`- Difficulty: ${scope.difficulty}`);
  }

  if (scope.lang) {
    parts.push(`- Language: ${scope.lang}`);
  }

  pushTextSection(parts, 'Problem Description', scope.questionContent);

  if (scope.testcase?.trim()) {
    parts.push('', '## Active Testcase', '```text', truncate(scope.testcase, MAX_TEXT_SECTION_CHARS), '```');
  }

  pushCodeSection(parts, 'Final Editor Code', scope.editorContent, scope.filetype ?? scope.lang ?? 'text');

  if (scope.submissionContent?.trim() && scope.submissionContent.trim() !== scope.editorContent?.trim()) {
    pushCodeSection(parts, 'Last Submitted Code', scope.submissionContent, scope.filetype ?? scope.lang ?? 'text');
  }

  if (scope.latestFailure) {
    parts.push('', '## Latest LeetCode Failure', `- Event ID: ${scope.latestFailure.eventId}`);

    const status = readJudgeStatus(scope.latestFailure.judgeResult);
    if (status) {
      parts.push(`- Judge Status: ${status}`);
    }

    if (scope.latestFailure.testcase?.trim()) {
      parts.push(
        '',
        '### Failed Testcase',
        '```text',
        truncate(scope.latestFailure.testcase, MAX_TEXT_SECTION_CHARS),
        '```',
      );
    }

    parts.push('', '### Raw Judge Result', '```json', truncateJson(scope.latestFailure.judgeResult), '```');
  }

  if (scope.lastFailureAnalysis) {
    parts.push(
      '',
      '## Latest Failure Analysis',
      `- Summary: ${truncate(scope.lastFailureAnalysis.summary, MAX_MESSAGE_CHARS)}`,
    );

    if (scope.lastFailureAnalysis.annotations.length > 0) {
      parts.push('- Annotations:');
      for (const annotation of scope.lastFailureAnalysis.annotations) {
        parts.push(`  - line ${annotation.line} [${annotation.severity}]: ${truncate(annotation.reason, 240)}`);
      }
    }
  }

  pushMessagesSection(parts, 'Service Session Memory', scope.sessionMemory?.messages, MAX_SERVICE_UPDATES);
  pushMessagesSection(parts, 'Companion Conversation', scope.companionMemory?.messages, MAX_COMPANION_TURNS);

  return parts.join('\n');
}

export function renderRecalledSessionRecords(result: SessionRecordRecallResult): CompanionChatMessage {
  const records = [...result.records].sort((left, right) =>
    (left.createdAt ?? left.updatedAt ?? '').localeCompare(right.createdAt ?? right.updatedAt ?? ''),
  );
  const visibleRecords = records.slice(-MAX_RECALLED_SESSION_RECORDS);
  const omittedCount = records.length - visibleRecords.length;
  const parts = [
    '# Submission Service Mem0 Recall',
    '',
    `- Title Slug: ${result.titleSlug}`,
    `- Recalled Session Count: ${records.length}`,
    '- These are ended-session records recalled from Mem0 for this exact LeetCode problem.',
    '- Treat these as historical summaries only; do not assume omitted code or truncated snapshots are ground truth.',
  ];

  if (omittedCount > 0) {
    parts.push(`- Omitted Older Session Count: ${omittedCount}`);
  }

  visibleRecords.forEach((record, index) => {
    const metadata = record.metadata ?? {};
    const activatedAt = readMetadataString(metadata, 'activated_at', 'activatedAt');
    const endedAt = readMetadataString(metadata, 'ended_at', 'endedAt');
    const endReason = readMetadataString(metadata, 'end_reason', 'endReason');
    const language = readMetadataString(metadata, 'language');
    const difficulty = readMetadataString(metadata, 'difficulty');
    const latestFailureStatus = readMetadataString(metadata, 'latest_failure_status', 'latestFailureStatus');
    const elapsedMinutes = readMetadataNumber(metadata, 'elapsed_minutes', 'elapsedMinutes');
    const hasEditorCode = hasMarkdownSection(record.memory, 'Final Editor Code');
    const hasSubmittedCode = hasMarkdownSection(record.memory, 'Last Submitted Code');
    const hasFailureSnapshot = hasMarkdownSection(record.memory, 'Latest LeetCode Failure');
    const hasFailureAnalysis = hasMarkdownSection(record.memory, 'Latest Failure Analysis');
    const hasCompanionConversation = hasMarkdownSection(record.memory, 'Companion Conversation');
    const submittedCode = readMarkdownSection(record.memory, 'Last Submitted Code');
    const editorCode = readMarkdownSection(record.memory, 'Final Editor Code');

    parts.push('', `## Session ${index + 1}`);

    if (activatedAt) {
      parts.push(`- Activated At: ${activatedAt}`);
    }

    if (endedAt) {
      parts.push(`- Ended At: ${endedAt}`);
    }

    if (endReason) {
      parts.push(`- End Reason: ${endReason}`);
    }

    if (typeof elapsedMinutes === 'number' && Number.isFinite(elapsedMinutes)) {
      parts.push(`- Elapsed Minutes: ${elapsedMinutes}`);
    }

    if (difficulty) {
      parts.push(`- Difficulty: ${difficulty}`);
    }

    if (language) {
      parts.push(`- Language: ${language}`);
    }

    if (latestFailureStatus) {
      parts.push(`- Latest Failure Status: ${latestFailureStatus}`);
    }

    const observed: string[] = [];
    if (hasEditorCode) {
      observed.push('editor_code');
    }
    if (hasSubmittedCode) {
      observed.push('submitted_code');
    }
    if (hasFailureSnapshot) {
      observed.push('failure_snapshot');
    }
    if (hasFailureAnalysis) {
      observed.push('failure_analysis');
    }
    if (hasCompanionConversation) {
      observed.push('companion_conversation');
    }

    if (observed.length > 0) {
      parts.push(`- Observed Artifacts: ${observed.join(', ')}`);
    } else {
      parts.push('- Observed Artifacts: metadata_only');
    }

    const preferredCode = submittedCode ?? editorCode;
    if (preferredCode) {
      parts.push(
        '',
        '### Recalled Code Excerpt',
        '```text',
        truncate(stripCodeFence(preferredCode), MAX_RECALLED_CODE_CHARS),
        '```',
      );
    }
  });

  return {
    role: 'user',
    content: parts.join('\n'),
  };
}

class NoopSessionRecordPersister implements SessionRecordPersister {
  async persist(): Promise<void> {}
}

class NoopSessionRecordRecaller implements SessionRecordRecaller {
  async recallByTitleSlug(titleSlug: string): Promise<SessionRecordRecallResult> {
    return {
      titleSlug,
      records: [],
    };
  }
}

export class Mem0SessionRecordPersister implements SessionRecordPersister {
  private readonly agentId: string;
  private readonly appId: string;
  private readonly client: MemoryClientLike;

  constructor(private readonly options: Mem0SessionRecordPersisterOptions) {
    this.agentId = options.agentId?.trim() || DEFAULT_MEM0_AGENT_ID;
    this.appId = options.appId?.trim() || DEFAULT_MEM0_APP_ID;
    const MemoryClientCtor = MemoryClient as unknown as MemoryClientConstructor;
    this.client =
      options.client ??
      new MemoryClientCtor({
        apiKey: options.apiKey,
        host: options.host,
      });
  }

  async persist(scope: ActiveSessionScope, event: SessionEndEvent): Promise<void> {
    const runId = buildMem0RunId(scope);
    const response = (await this.client.add(
      [
        {
          role: 'user',
          content: renderPersistedSessionRecord(scope, event),
        },
      ],
      {
        userId: this.options.userId,
        agentId: this.agentId,
        appId: this.appId,
        runId,
        infer: false,
        metadata: {
          source: 'leetcode-submission-service',
          recordType: 'leetcode_session_record',
          titleSlug: scope.titleSlug,
          endReason: event.reason,
          activatedAt: scope.activatedAt,
          endedAt: event.endedAt,
          elapsedMinutes: event.elapsedMinutes ?? null,
          difficulty: scope.difficulty ?? null,
          language: scope.lang ?? null,
          latestFailureStatus: readJudgeStatus(scope.latestFailure?.judgeResult),
          replacedByTitleSlug: event.replacedByTitleSlug ?? null,
        },
      },
    )) as Mem0AddResponse;
    logger.info(
      {
        titleSlug: scope.titleSlug,
        runId,
        mem0EventId: response.eventId,
        mem0Status: response.status,
        endReason: event.reason,
      },
      'Persisted LeetCode session record to Mem0',
    );
  }
}

function resolveMem0BaseUrl(host?: string): string {
  const base = host?.trim() || DEFAULT_MEM0_BASE_URL;
  return base.endsWith('/') ? base : `${base}/`;
}

function parseRecalledSessionRecords(payload: unknown): RecalledSessionRecord[] {
  const envelope = payload as Mem0GetAllResponse | undefined;
  const results = Array.isArray(envelope?.results) ? envelope.results : [];

  return results.flatMap((entry) => {
    if (!entry || typeof entry !== 'object' || Array.isArray(entry)) {
      return [];
    }

    const record = entry as Record<string, unknown>;
    const id = readStringValue(record.id);
    const memory = readStringValue(record.memory);
    if (!id || !memory) {
      return [];
    }

    return [
      {
        id,
        memory,
        createdAt: readStringValue(record.created_at),
        updatedAt: readStringValue(record.updated_at),
        metadata: readMetadataRecord(record.metadata),
      } satisfies RecalledSessionRecord,
    ];
  });
}

export class Mem0SessionRecordRecaller implements SessionRecordRecaller {
  private readonly agentId: string;
  private readonly appId: string;
  private readonly baseUrl: string;
  private readonly fetchImpl: typeof fetch;

  constructor(private readonly options: Mem0SessionRecordRecallerOptions) {
    this.agentId = options.agentId?.trim() || DEFAULT_MEM0_AGENT_ID;
    this.appId = options.appId?.trim() || DEFAULT_MEM0_APP_ID;
    this.baseUrl = resolveMem0BaseUrl(options.host);
    this.fetchImpl = options.fetchImpl ?? fetch;
  }

  async recallByTitleSlug(titleSlug: string): Promise<SessionRecordRecallResult> {
    const filters = {
      AND: [
        { user_id: this.options.userId },
        { agent_id: this.agentId },
        { app_id: this.appId },
        { metadata: { record_type: 'leetcode_session_record' } },
        { metadata: { title_slug: titleSlug } },
      ],
    };
    const records: RecalledSessionRecord[] = [];
    let page = 1;
    let hasNextPage = true;

    while (hasNextPage) {
      const url = new URL(`v3/memories/?page=${page}&page_size=200`, this.baseUrl);
      const response = await this.fetchImpl(url, {
        method: 'POST',
        headers: {
          Authorization: `Token ${this.options.apiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filters }),
      });

      if (!response.ok) {
        throw new Error(`Mem0 recall failed with ${response.status} ${response.statusText}`);
      }

      const payload = (await response.json()) as Mem0GetAllResponse;
      records.push(...parseRecalledSessionRecords(payload));
      hasNextPage = typeof payload.next === 'string' && payload.next.trim().length > 0;
      page += 1;
    }

    logger.info(
      {
        titleSlug,
        recalledCount: records.length,
      },
      'Recalled LeetCode session records from Mem0',
    );
    return {
      titleSlug,
      records,
    };
  }
}

function resolveDefaultMem0UserId(): string {
  const explicit = process.env.MEM0_USER_ID?.trim();
  if (explicit) {
    return explicit;
  }

  const envUser = process.env.USER?.trim() || process.env.USERNAME?.trim();
  if (envUser) {
    return envUser;
  }

  try {
    return os.userInfo().username;
  } catch {
    return 'local-user';
  }
}

export function createDefaultSessionRecordPersister(): SessionRecordPersister {
  const apiKey = process.env.MEM0_API_KEY?.trim();
  if (!apiKey) {
    return new NoopSessionRecordPersister();
  }

  return new Mem0SessionRecordPersister({
    apiKey,
    userId: resolveDefaultMem0UserId(),
    agentId: process.env.MEM0_AGENT_ID?.trim(),
    appId: process.env.MEM0_APP_ID?.trim(),
    host: process.env.MEM0_BASE_URL?.trim(),
  });
}

export function createDefaultSessionRecordRecaller(): SessionRecordRecaller {
  const apiKey = process.env.MEM0_API_KEY?.trim();
  if (!apiKey) {
    return new NoopSessionRecordRecaller();
  }

  return new Mem0SessionRecordRecaller({
    apiKey,
    userId: resolveDefaultMem0UserId(),
    agentId: process.env.MEM0_AGENT_ID?.trim(),
    appId: process.env.MEM0_APP_ID?.trim(),
    host: process.env.MEM0_BASE_URL?.trim(),
  });
}
