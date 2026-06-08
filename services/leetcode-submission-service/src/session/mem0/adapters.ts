import os from 'node:os';
import MemoryClient from 'mem0ai';
import {
  DEFAULT_MEM0_AGENT_ID,
  DEFAULT_MEM0_APP_ID,
  DEFAULT_MEM0_BASE_URL,
  MIN_INTERACTIONS_TO_PERSIST,
  logger,
} from './constants.ts';
import {
  buildMem0RunId,
  buildPersistedSessionRecordMetadata,
  countSessionInteractions,
  renderPersistedSessionRecord,
} from './render.ts';
import { summarizeSimilarProblemRecall } from './similarity.ts';
import { readMetadataRecord, readStringValue } from './shared.ts';
import type {
  Mem0AddResponse,
  Mem0GetAllResponse,
  Mem0SessionRecordPersisterOptions,
  Mem0SessionRecordRecallerOptions,
  MemoryClientConstructor,
  MemoryClientLike,
  RecalledSessionRecord,
  SessionRecordPersister,
  SessionRecordRecallResult,
  SessionRecordRecaller,
  SimilarProblemRecallQuery,
  SimilarProblemRecallResult,
} from './types.ts';
import type { ActiveSessionScope } from '../scope.ts';
import type { SessionEndEvent } from './types.ts';

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

  async recallSimilarByQuery(query: SimilarProblemRecallQuery): Promise<SimilarProblemRecallResult> {
    return summarizeSimilarProblemRecall(
      {
        titleSlug: query.titleSlug,
        records: [],
      },
      query,
    );
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
    const interactionCount = countSessionInteractions(scope);
    if (interactionCount < MIN_INTERACTIONS_TO_PERSIST && !event.forcePersist) {
      logger.info(
        {
          titleSlug: scope.titleSlug,
          interactionCount,
          minimumInteractionsToPersist: MIN_INTERACTIONS_TO_PERSIST,
          endReason: event.reason,
        },
        'Skipped persisting LeetCode session record to Mem0 because interaction count is below threshold',
      );
      return;
    }

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
        metadata: buildPersistedSessionRecordMetadata(scope, event),
      },
    )) as Mem0AddResponse;
    logger.info(
      {
        titleSlug: scope.titleSlug,
        runId,
        interactionCount,
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

  private async fetchRecords(filters: Record<string, unknown>): Promise<RecalledSessionRecord[]> {
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

    return records;
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
    const records = await this.fetchRecords(filters);

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

  async recallSimilarByQuery(query: SimilarProblemRecallQuery): Promise<SimilarProblemRecallResult> {
    const filters = {
      AND: [
        { user_id: this.options.userId },
        { agent_id: this.agentId },
        { app_id: this.appId },
        { metadata: { record_type: 'leetcode_session_record' } },
      ],
    };
    const records = await this.fetchRecords(filters);
    const result = summarizeSimilarProblemRecall(
      {
        titleSlug: query.titleSlug,
        records,
      },
      query,
    );

    logger.info(
      {
        titleSlug: query.titleSlug,
        similarMatchCount: result.matches.length,
      },
      'Recalled similar LeetCode session records from Mem0',
    );

    return result;
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
