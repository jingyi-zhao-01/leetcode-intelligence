import net from "node:net";
import { fileURLToPath } from "node:url";
import { Prisma, PrismaClient } from "@prisma/client";
import { extractThought, normalizeForEmbedding } from "./codeCleaner.js";
import { getDatabaseDiagnostics, resolveDatabaseUrl } from "./database.js";
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
}

type SubmissionItem = Record<string, unknown>;

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
    const submissionFlag = readSubmissionFlag(metadata as SubmissionItem, "submission");
    if (typeof submissionFlag === "boolean") {
      return !submissionFlag;
    }
  }

  return content.includes("#TEST#");
}

export class SubmissionServer {
  private readonly host: string;
  private readonly port: number;
  private readonly timerManager = new TimerManager();
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

  private async saveSubmission(titleSlug: string, content: string, item: SubmissionItem): Promise<boolean> {
    const status = readString(item.status_msg, "Unknown");
    const isTest = inferIsTestSubmission(content, item);
    const isCheat = content.includes("#CHEAT#");

    let timeSpentMinutes: number | null = null;
    if (this.timerManager.hasActiveTimer(titleSlug)) {
      timeSpentMinutes = this.timerManager.getElapsedTime(titleSlug);
      logger.info({ titleSlug, timeSpentMinutes }, "Current elapsed time");
    }

    try {
      const cleanedContent = normalizeForEmbedding(content);
      const thought = extractThought(content);
      const submissionDetails = JSON.parse(JSON.stringify(item)) as SubmissionItem;
      submissionDetails.lcnvim_is_test = isTest;

      const submission = await this.db.submission.create({
        data: {
          titleSlug,
          content: cleanedContent,
          status,
          isCheat,
          timeSpentMinutes,
          thought,
          submissionDetails: submissionDetails as Prisma.InputJsonValue,
        },
      });

      if (status === "Accepted" && !isTest) {
        if (this.timerManager.hasActiveTimer(titleSlug)) {
          this.timerManager.stop(titleSlug);
        }
        this.timerManager.start(titleSlug);
        logger.info({ titleSlug }, "Timer restarted for accepted solution");
      }

      logger.info(
        {
          submissionId: submission.id,
          titleSlug,
          status,
          isTest,
          isCheat,
          timeSpentMinutes,
        },
        "Submission saved successfully",
      );

      return true;
    } catch (error) {
      logger.error({ err: error, titleSlug }, "Error saving submission");
      return false;
    }
  }

  private async getPastSubmissions(titleSlug: string, limit = 10): Promise<Record<string, unknown>[]> {
    const safeLimit = Math.max(1, Math.min(limit, 50));
    const submissions = await this.db.submission.findMany({
      where: { titleSlug },
      orderBy: { createdAt: "desc" },
      take: safeLimit,
    });

    return submissions.map((submission) => {
      const details =
        submission.submissionDetails && typeof submission.submissionDetails === "object" && !Array.isArray(submission.submissionDetails)
          ? (submission.submissionDetails as SubmissionItem)
          : {};
      const isTest = inferIsTestSubmission(submission.content, details);

      return {
        id: submission.id,
        title_slug: submission.titleSlug,
        submitted_at: submission.createdAt.toISOString(),
        submitted_at_pst: formatPacificTimestamp(submission.createdAt),
        time_spent_minutes: submission.timeSpentMinutes,
        submit_result: submission.status,
        is_test: isTest,
      };
    });
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
        const submissions = await this.getPastSubmissions(titleSlug, limit);

        return {
          success: true,
          action: ServerAction.GET_PAST_SUBMISSIONS,
          title_slug: titleSlug,
          submissions,
          count: submissions.length,
        };
      }

      case ServerAction.SAVE_SUBMISSION: {
        const titleSlug = readString(request.title_slug);
        const content = readString(request.content);
        const item = (request.item ?? {}) as SubmissionItem;
        const success = await this.saveSubmission(titleSlug, content, item);
        return {
          success,
          action: ServerAction.SAVE_SUBMISSION,
          title_slug: titleSlug,
        };
      }

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
