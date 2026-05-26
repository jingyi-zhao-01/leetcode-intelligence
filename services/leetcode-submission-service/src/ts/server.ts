import net from "node:net";
import { randomUUID } from "node:crypto";
import { fileURLToPath } from "node:url";
import { OpenRouter } from "@openrouter/sdk";
import { type Submission, PrismaClient } from "@prisma/client";
import { withReadSubmissionCache, withWriteThroughSubmissionCache, type ActionContext, type ActionHandler } from "./action-middleware.js";
import { Cache, type SubmissionSummary } from "./cache.js";
import { extractThought, normalizeForEmbedding } from "./codeCleaner.js";
import { getDatabaseDiagnostics, resolveDatabaseUrl } from "./database.js";
import { type FailureAnalysisRequest, OpenRouterFailureAnalyzer } from "./failureAnalysis.js";
import { createLogger } from "./logger.js";
import { TimerManager } from "./timer.js";

enum ServerAction {
  START_TIMER = "start_timer",
  STOP_TIMER = "stop_timer",
  DROP_TIMER = "drop_timer",
  GET_ACTIVE_TIMERS = "get_active_timers",
  GET_ACTIVE_SESSIONS = "get_active_sessions",
  GET_PAST_SUBMISSIONS = "get_past_submissions",
  SAVE_SUBMISSION = "save_submission",
  ANALYZE_FAILURE = "analyze_failure",
}

type JsonPrimitive = string | number | boolean | null;
type JsonValue = JsonPrimitive | { [key: string]: JsonValue } | JsonValue[];
type SubmissionItem = { [key: string]: JsonValue | undefined };
type PendingSubmission = {
  titleSlug: string;
  status: string;
  isTest: boolean;
  isCheat: boolean;
  timeSpentMinutes: number | null;
  createdAt: Date;
  cleanedContent: string;
  thought: string | null;
  submissionDetails: SubmissionItem;
};
type SubmissionActionResponse = Record<string, unknown>;
type SubmissionActionHandlers = {
  [ServerAction.GET_PAST_SUBMISSIONS]: ActionHandler<[string, number?], SubmissionActionResponse>;
  [ServerAction.SAVE_SUBMISSION]: ActionHandler<[string, string, SubmissionItem], SubmissionActionResponse>;
};

const logger = createLogger("server");

function readString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback;
}

function readNumber(value: unknown, fallback: number): number {
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}

export function formatPacificTimestamp(date: Date): string {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Los_Angeles",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
    timeZoneName: "short",
  }).formatToParts(date);

  const part = (type: Intl.DateTimeFormatPartTypes): string =>
    parts.find((entry) => entry.type === type)?.value ?? "";

  return `${part("year")}-${part("month")}-${part("day")} ${part("hour")}:${part("minute")}:${part("second")} ${part("timeZoneName")}`;
}

function readSubmissionFlag(item: SubmissionItem, key: string): boolean | undefined {
  const value = item[key];
  return typeof value === "boolean" ? value : undefined;
}

export function inferIsTestSubmission(content: string, item: SubmissionItem): boolean {
  const topLevelFlag = readSubmissionFlag(item, "lcnvim_is_test");
  if (typeof topLevelFlag === "boolean") {
    return topLevelFlag;
  }

  const metadata = item._;
  if (metadata && typeof metadata === "object" && !Array.isArray(metadata)) {
    const submissionFlag = readSubmissionFlag(metadata, "submission");
    if (typeof submissionFlag === "boolean") {
      return !submissionFlag;
    }
  }

  return content.includes("#TEST#");
}

function createSubmissionSummary(args: {
  id: string;
  titleSlug: string;
  createdAt: Date;
  timeSpentMinutes: number | null;
  status: string;
  isTest: boolean;
}): SubmissionSummary {
  return {
    id: args.id,
    title_slug: args.titleSlug,
    submitted_at: args.createdAt.toISOString(),
    submitted_at_pst: formatPacificTimestamp(args.createdAt),
    time_spent_minutes: args.timeSpentMinutes,
    submit_result: args.status,
    is_test: args.isTest,
  };
}

export class SubmissionServer {
  private readonly host: string;
  private readonly port: number;
  private readonly timerManager = new TimerManager();
  readonly logger = logger;
  readonly cache = new Cache();
  private readonly openRouter = process.env.OPEN_ROUTER_API_KEY
    ? new OpenRouter({
        apiKey: process.env.OPEN_ROUTER_API_KEY,
        httpReferer: "https://github.com/kawre/leetcode.nvim",
        appTitle: "leetcode-submission-service",
      })
    : null;
  private readonly failureAnalyzer = this.openRouter
    ? new OpenRouterFailureAnalyzer(
        this.openRouter,
        process.env.FAILURE_ANALYSIS_MODEL ?? process.env.MODEL ?? "qwen/qwen3-coder-next",
      )
    : null;
  private readonly actionContext: ActionContext = {
    cache: this.cache,
    logger: this.logger,
  };
  private readonly actionHandlers: Partial<SubmissionActionHandlers> = {
    [ServerAction.GET_PAST_SUBMISSIONS]: withReadSubmissionCache<[string, number?], SubmissionActionResponse>({
      actionName: ServerAction.GET_PAST_SUBMISSIONS,
      getTitleSlug: (titleSlug: string) => titleSlug,
      getLimit: (_titleSlug: string, limit = 10) => Math.max(1, Math.min(limit, 50)),
      readPersisted: (_context, titleSlug: string, limit = 10) => this.fetchPersistedPastSubmissions(titleSlug, limit),
      buildResponse: (submissions: SubmissionSummary[], titleSlug: string) => ({
        success: true,
        action: ServerAction.GET_PAST_SUBMISSIONS,
        title_slug: titleSlug,
        submissions,
        count: submissions.length,
      }),
    }),
    [ServerAction.SAVE_SUBMISSION]: withWriteThroughSubmissionCache<[string, string, SubmissionItem], PendingSubmission, SubmissionActionResponse>({
      actionName: ServerAction.SAVE_SUBMISSION,
      toPending: (titleSlug: string, content: string, item: SubmissionItem) => this.createPendingSubmission(titleSlug, content, item),
      cachePending: (context, pending: PendingSubmission) => {
        const cacheKey = context.cache.savePending(
          createSubmissionSummary({
            id: `pending:${randomUUID()}`,
            titleSlug: pending.titleSlug,
            createdAt: pending.createdAt,
            timeSpentMinutes: pending.timeSpentMinutes,
            status: pending.status,
            isTest: pending.isTest,
          }),
        );

        context.logger.info(
          {
            cacheKey,
            titleSlug: pending.titleSlug,
            status: pending.status,
            isTest: pending.isTest,
            isCheat: pending.isCheat,
            timeSpentMinutes: pending.timeSpentMinutes,
          },
          "Submission cached successfully",
        );

        return {
          cacheKey,
          titleSlug: pending.titleSlug,
          response: {
            success: true,
            action: ServerAction.SAVE_SUBMISSION,
            title_slug: pending.titleSlug,
          },
        };
      },
      persist: (_context, pending: PendingSubmission, cacheKey: string) => this.persistPendingSubmission(pending, cacheKey),
    }),
  };
  private readonly db = (() => {
    const databaseUrl = resolveDatabaseUrl();
    if (!databaseUrl) {
      return new PrismaClient();
    }

    return new PrismaClient({
      datasources: {
        db: {
          url: databaseUrl,
        },
      },
    });
  })();

  constructor(host = process.env.SUBMISSION_HOST ?? "127.0.0.1", port = Number(process.env.SUBMISSION_PORT ?? 3000)) {
    this.host = host;
    this.port = Number.isFinite(port) ? port : 3000;
  }

  private startActiveSessionLogger(): void {
    setInterval(() => {
      const timers = this.timerManager.getActiveTimers();
      const entries = Object.entries(timers);
      if (entries.length === 0) {
        logger.info("No active sessions");
        return;
      }
      logger.info({ count: entries.length }, "Active sessions");
      for (const [slug, elapsed] of entries) {
        logger.info({ titleSlug: slug, elapsedMinutes: elapsed }, "Active session");
      }
    }, 5000);
  }

  private createPendingSubmission(titleSlug: string, content: string, item: SubmissionItem): PendingSubmission {
    const status = readString(item.status_msg, "Unknown");
    const isTest = inferIsTestSubmission(content, item);
    const isCheat = content.includes("#CHEAT#");

    let timeSpentMinutes: number | null = null;
    if (this.timerManager.hasActiveTimer(titleSlug)) {
      timeSpentMinutes = this.timerManager.getElapsedTime(titleSlug);
      this.logger.info({ titleSlug, timeSpentMinutes }, "Current elapsed time");
    }

    const submissionDetails = structuredClone(item);
    submissionDetails.lcnvim_is_test = isTest;

    if (status === "Accepted" && !isTest) {
      if (this.timerManager.hasActiveTimer(titleSlug)) {
        this.timerManager.stop(titleSlug);
      }
      this.timerManager.start(titleSlug);
      this.logger.info({ titleSlug }, "Timer restarted for accepted solution");
    }

    return {
      titleSlug,
      status,
      isTest,
      isCheat,
      timeSpentMinutes,
      createdAt: new Date(),
      cleanedContent: normalizeForEmbedding(content),
      thought: extractThought(content),
      submissionDetails,
    };
  }

  private async persistSubmission(args: {
    titleSlug: string;
    content: string;
    status: string;
    isCheat: boolean;
    timeSpentMinutes: number | null;
    thought: string | null;
    submissionDetails: SubmissionItem;
  }): Promise<string> {
    const submission = await this.db.submission.create({
      data: {
        titleSlug: args.titleSlug,
        content: args.content,
        status: args.status,
        isCheat: args.isCheat,
        timeSpentMinutes: args.timeSpentMinutes,
        thought: args.thought,
        submissionDetails: args.submissionDetails,
      },
    });

    return submission.id;
  }

  private async persistPendingSubmission(pending: PendingSubmission, cacheKey: string): Promise<void> {
    const submissionId = await this.persistSubmission({
      titleSlug: pending.titleSlug,
      content: pending.cleanedContent,
      status: pending.status,
      isCheat: pending.isCheat,
      timeSpentMinutes: pending.timeSpentMinutes,
      thought: pending.thought,
      submissionDetails: pending.submissionDetails,
    });

    this.cache.markPersisted(pending.titleSlug, cacheKey, submissionId);
    this.logger.info(
      {
        submissionId,
        titleSlug: pending.titleSlug,
        status: pending.status,
        isTest: pending.isTest,
        isCheat: pending.isCheat,
        timeSpentMinutes: pending.timeSpentMinutes,
      },
      "Submission persisted successfully",
    );
  }

  private async fetchPersistedPastSubmissions(titleSlug: string, limit = 10): Promise<SubmissionSummary[]> {
    const safeLimit = Math.max(1, Math.min(limit, 50));
    const persisted = await this.db.submission.findMany({
      where: { titleSlug },
      orderBy: { createdAt: "desc" },
      take: safeLimit,
    });

    return persisted.map((submission: Submission) => {
      const details =
        submission.submissionDetails && typeof submission.submissionDetails === "object" && !Array.isArray(submission.submissionDetails)
          ? (submission.submissionDetails as SubmissionItem)
          : {};
      const isTest = inferIsTestSubmission(submission.content, details);

      return createSubmissionSummary({
        id: submission.id,
        titleSlug: submission.titleSlug ?? titleSlug,
        createdAt: submission.createdAt,
        timeSpentMinutes: submission.timeSpentMinutes,
        status: submission.status,
        isTest,
      });
    });
  }

  private async saveSubmission(titleSlug: string, content: string, item: SubmissionItem): Promise<Record<string, unknown>> {
    const handler = this.actionHandlers[ServerAction.SAVE_SUBMISSION];
    if (!handler) {
      throw new Error("save_submission handler not configured");
    }
    return handler(this.actionContext, titleSlug, content, item);
  }

  private async getPastSubmissions(titleSlug: string, limit = 10): Promise<Record<string, unknown>> {
    const handler = this.actionHandlers[ServerAction.GET_PAST_SUBMISSIONS];
    if (!handler) {
      throw new Error("get_past_submissions handler not configured");
    }
    return handler(this.actionContext, titleSlug, limit);
  }

  private async analyzeFailure(request: Record<string, unknown>): Promise<Record<string, unknown>> {
    if (!this.failureAnalyzer) {
      return {
        success: false,
        action: ServerAction.ANALYZE_FAILURE,
        error: "OPEN_ROUTER_API_KEY is not configured for submission failure analysis.",
      };
    }

    const payload = {
      titleSlug: readString(request.title_slug),
      title: readString(request.title),
      questionContent: readString(request.question_content),
      editorContent: readString(request.editor_content),
      submissionContent: readString(request.submission_content),
      testcase: readString(request.testcase),
      judgeResult: (request.item ?? {}) as FailureAnalysisRequest["judgeResult"],
      filetype: readString(request.filetype, "text"),
    } satisfies FailureAnalysisRequest;

    if (!payload.titleSlug || !payload.editorContent) {
      return {
        success: false,
        action: ServerAction.ANALYZE_FAILURE,
        error: "title_slug and editor_content are required.",
      };
    }

    logger.info(
      {
        action: ServerAction.ANALYZE_FAILURE,
        titleSlug: payload.titleSlug,
        editorChars: payload.editorContent.length,
        testcaseChars: payload.testcase.length,
      },
      "starting failure analysis",
    );
    const analysis = await this.failureAnalyzer.analyze(payload);
    logger.info(
      {
        action: ServerAction.ANALYZE_FAILURE,
        titleSlug: payload.titleSlug,
        annotationCount: analysis.annotations.length,
      },
      "completed failure analysis",
    );
    return {
      success: true,
      action: ServerAction.ANALYZE_FAILURE,
      title_slug: payload.titleSlug,
      summary: analysis.summary,
      annotations: analysis.annotations,
      count: analysis.annotations.length,
    };
  }

  private async handleRequest(request: Record<string, unknown>): Promise<Record<string, unknown>> {
    const action = readString(request.action);
    logger.info({ action }, "Received request");

    switch (action) {
      case ServerAction.START_TIMER: {
        const titleSlug = readString(request.title_slug);
        const result = this.timerManager.start(titleSlug);
        return {
          success: true,
          action: ServerAction.START_TIMER,
          title_slug: titleSlug,
          already_active: result.alreadyActive,
          evicted_title_slugs: result.evictedTitleSlugs,
        };
      }

      case ServerAction.STOP_TIMER: {
        const titleSlug = readString(request.title_slug);
        const minutes = this.timerManager.stop(titleSlug);
        return {
          success: true,
          action: ServerAction.STOP_TIMER,
          title_slug: titleSlug,
          minutes,
        };
      }

      case ServerAction.DROP_TIMER: {
        const titleSlug = readString(request.title_slug);
        this.timerManager.stop(titleSlug);
        return { success: true, action: ServerAction.DROP_TIMER, title_slug: titleSlug };
      }

      case ServerAction.GET_ACTIVE_TIMERS: {
        return {
          success: true,
          action: ServerAction.GET_ACTIVE_TIMERS,
          timers: this.timerManager.getActiveTimers(),
        };
      }

      case ServerAction.GET_ACTIVE_SESSIONS: {
        const timers = this.timerManager.getActiveTimers();
        const sessions = Object.entries(timers).map(([titleSlug, elapsedMinutes]) => ({
          title_slug: titleSlug,
          elapsed_minutes: elapsedMinutes,
          status: "active",
        }));

        return {
          success: true,
          action: ServerAction.GET_ACTIVE_SESSIONS,
          sessions,
          count: sessions.length,
        };
      }

      case ServerAction.GET_PAST_SUBMISSIONS: {
        const titleSlug = readString(request.title_slug);
        const limit = readNumber(request.limit, 10);
        return this.getPastSubmissions(titleSlug, limit);
      }

      case ServerAction.SAVE_SUBMISSION: {
        const titleSlug = readString(request.title_slug);
        const content = readString(request.content);
        const item = (request.item ?? {}) as SubmissionItem;
        return this.saveSubmission(titleSlug, content, item);
      }

      case ServerAction.ANALYZE_FAILURE:
        return this.analyzeFailure(request);

      default:
        return { error: `Unknown action: ${action}` };
    }
  }

  async start(): Promise<void> {
    const database = getDatabaseDiagnostics();
    const connectStartedAt = Date.now();

    logger.info({ database }, "Connecting to database");

    try {
      await this.db.$connect();
      logger.info({ database, connectMs: Date.now() - connectStartedAt }, "Database connection established");
    } catch (error) {
      logger.error({ err: error, database, connectMs: Date.now() - connectStartedAt }, "Database connection failed during startup");
      throw error;
    }

    this.startActiveSessionLogger();

    const server = net.createServer((socket) => {
      const peer = `${socket.remoteAddress ?? "unknown"}:${socket.remotePort ?? "?"}`;
      logger.info({ peer }, "Client connected");

      let buffer = "";

      socket.on("data", async (chunk) => {
        buffer += chunk.toString("utf8");
        const lines = buffer.split("\n");
        buffer = lines.pop() ?? "";

        for (const rawLine of lines) {
          const line = rawLine.trim();
          if (!line) {
            continue;
          }

          try {
            const request = JSON.parse(line) as Record<string, unknown>;
            const response = await this.handleRequest(request);
            socket.write(`${JSON.stringify(response)}\n`);
          } catch (error) {
            const response = { error: `Invalid JSON or request error: ${String(error)}` };
            socket.write(`${JSON.stringify(response)}\n`);
          }
        }
      });

      socket.on("close", () => {
        logger.info({ peer }, "Client disconnected");
      });

      socket.on("error", (error) => {
        logger.error({ err: error, peer }, "Client socket error");
      });
    });

    server.listen(this.port, this.host, () => {
      logger.info({ host: this.host, port: this.port }, "Submission server started");
    });

    process.on("SIGINT", async () => {
      await this.db.$disconnect().catch(() => undefined);
      server.close(() => process.exit(0));
    });

    process.on("SIGTERM", async () => {
      await this.db.$disconnect().catch(() => undefined);
      server.close(() => process.exit(0));
    });
  }
}

export async function main(): Promise<void> {
  const app = new SubmissionServer();
  try {
    await app.start();
  } catch (error) {
    logger.fatal({ err: error }, "Unhandled startup error");
    process.exit(1);
  }
}

const entrypoint = process.argv[1];
if (entrypoint && fileURLToPath(import.meta.url) == entrypoint) {
  await main();
}
