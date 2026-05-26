import { randomUUID } from "node:crypto";
import { createLogger } from "./logger.js";

export type SubmissionSummary = {
  id: string;
  title_slug: string;
  submitted_at: string;
  submitted_at_pst: string;
  time_spent_minutes: number | null;
  submit_result: string;
  is_test: boolean;
};

type CachedSubmission = {
  cacheKey: string;
  persisted: boolean;
  dbId?: string;
  summary: SubmissionSummary;
};

const MAX_CACHE_ENTRIES_PER_SLUG = 100;
const logger = createLogger("cache");

export class Cache {
  private readonly entriesBySlug = new Map<string, CachedSubmission[]>();

  savePending(summary: SubmissionSummary): string {
    const cacheKey = randomUUID();
    const entries = this.entriesBySlug.get(summary.title_slug) ?? [];
    entries.unshift({
      cacheKey,
      persisted: false,
      summary,
    });
    this.entriesBySlug.set(summary.title_slug, entries.slice(0, MAX_CACHE_ENTRIES_PER_SLUG));
    logger.info(
      {
        titleSlug: summary.title_slug,
        cacheKey,
        status: summary.submit_result,
        isTest: summary.is_test,
        entryCount: this.entriesBySlug.get(summary.title_slug)?.length ?? 0,
      },
      "Cached pending submission",
    );
    return cacheKey;
  }

  markPersisted(titleSlug: string, cacheKey: string, persistedId: string): void {
    const entries = this.entriesBySlug.get(titleSlug);
    if (!entries) {
      logger.info({ titleSlug, cacheKey, persistedId }, "markPersisted skipped because slug cache was missing");
      return;
    }

    const entry = entries.find((item) => item.cacheKey === cacheKey);
    if (!entry) {
      logger.info({ titleSlug, cacheKey, persistedId, entryCount: entries.length }, "markPersisted skipped because cache entry was missing");
      return;
    }

    entry.persisted = true;
    entry.dbId = persistedId;
    entry.summary.id = persistedId;
    logger.info(
      {
        titleSlug,
        cacheKey,
        persistedId,
        status: entry.summary.submit_result,
      },
      "Marked cached submission as persisted",
    );
  }

  mergePersisted(titleSlug: string, persisted: SubmissionSummary[]): SubmissionSummary[] {
    const cacheEntries = this.entriesBySlug.get(titleSlug) ?? [];
    if (cacheEntries.length === 0) {
      this.entriesBySlug.set(
        titleSlug,
        persisted.slice(0, MAX_CACHE_ENTRIES_PER_SLUG).map((summary) => ({
          cacheKey: `db:${summary.id}`,
          persisted: true,
          dbId: summary.id,
          summary,
        })),
      );
      logger.info(
        {
          titleSlug,
          persistedCount: persisted.length,
          entryCount: this.entriesBySlug.get(titleSlug)?.length ?? 0,
        },
        "Primed cache from persisted submissions",
      );
      return persisted;
    }

    const seenIds = new Set(
      cacheEntries
        .map((entry) => entry.dbId ?? entry.summary.id)
        .filter((value): value is string => Boolean(value)),
    );

    for (const summary of persisted) {
      if (seenIds.has(summary.id)) {
        continue;
      }

      cacheEntries.push({
        cacheKey: `db:${summary.id}`,
        persisted: true,
        dbId: summary.id,
        summary,
      });
      seenIds.add(summary.id);
    }

    cacheEntries.sort((left, right) => right.summary.submitted_at.localeCompare(left.summary.submitted_at));
    this.entriesBySlug.set(titleSlug, cacheEntries.slice(0, MAX_CACHE_ENTRIES_PER_SLUG));
    logger.info(
      {
        titleSlug,
        persistedCount: persisted.length,
        mergedEntryCount: this.entriesBySlug.get(titleSlug)?.length ?? 0,
      },
      "Merged persisted submissions into cache",
    );

    return this.get(titleSlug, persisted.length + cacheEntries.length);
  }

  get(titleSlug: string, limit: number): SubmissionSummary[] {
    const entries = this.entriesBySlug.get(titleSlug) ?? [];
    const result = entries.slice(0, limit).map((entry) => ({ ...entry.summary }));
    logger.info(
      {
        titleSlug,
        limit,
        hitCount: result.length,
        cachedEntryCount: entries.length,
      },
      "Read submissions from cache",
    );
    return result;
  }
}
