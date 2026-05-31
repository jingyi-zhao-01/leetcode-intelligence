import type { Cache, SubmissionSummary } from "./cache.ts";

export type ActionContext = {
  cache: Cache;
  logger: {
    info(bindings: Record<string, unknown>, message: string): void;
  };
};

export type ActionHandler<TArgs extends unknown[] = unknown[], TResult = unknown> = (
  context: ActionContext,
  ...args: TArgs
) => Promise<TResult>;

type ReadCacheOptions<TArgs extends unknown[], TResult> = {
  actionName: string;
  getTitleSlug: (...args: TArgs) => string;
  getLimit: (...args: TArgs) => number;
  readPersisted: ActionHandler<TArgs, SubmissionSummary[]>;
  buildResponse: (submissions: SubmissionSummary[], ...args: TArgs) => TResult;
};

type WriteCacheOptions<TArgs extends unknown[], TPending, TResult> = {
  actionName: string;
  toPending: (...args: TArgs) => TPending;
  cachePending: (
    context: ActionContext,
    pending: TPending,
  ) => {
    cacheKey: string;
    titleSlug: string;
    response: TResult;
  };
  persist: (context: ActionContext, pending: TPending, cacheKey: string) => Promise<void>;
};


export function withReadSubmissionCache<TArgs extends unknown[], TResult>(
  options: ReadCacheOptions<TArgs, TResult>,
): ActionHandler<TArgs, TResult> {
  return async (context, ...args) => {
    const titleSlug = options.getTitleSlug(...args);
    const limit = options.getLimit(...args);
    const cached = context.cache.get(titleSlug, limit);

    if (cached.length >= limit) {
      context.logger.info(
        {
          action: options.actionName,
          titleSlug,
          limit,
          count: cached.length,
        },
        "Serving cached submissions via middleware",
      );
      return options.buildResponse(cached, ...args);
    }

    const persisted = await options.readPersisted(context, ...args);
    const merged = context.cache.mergePersisted(titleSlug, persisted).slice(0, limit);

    context.logger.info(
      {
        action: options.actionName,
        titleSlug,
        limit,
        cacheCount: cached.length,
        mergedCount: merged.length,
      },
      "Serving merged submissions via middleware",
    );

    return options.buildResponse(merged, ...args);
  };
}


export function withWriteThroughSubmissionCache<TArgs extends unknown[], TPending, TResult>(
  options: WriteCacheOptions<TArgs, TPending, TResult>,
): ActionHandler<TArgs, TResult> {
  return async (context, ...args) => {
    const pending = options.toPending(...args);
    const cached = options.cachePending(context, pending);

    void options.persist(context, pending, cached.cacheKey).catch((error) => {
      context.logger.info(
        {
          action: options.actionName,
          titleSlug: cached.titleSlug,
          cacheKey: cached.cacheKey,
          error: error instanceof Error ? error.message : String(error),
        },
        "Async persistence failed after cache write",
      );
    });

    return cached.response;
  };
}
