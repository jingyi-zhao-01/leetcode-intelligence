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

class NoopSessionRecordPersister implements SessionRecordPersister {
  async persist(): Promise<void> {}
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
