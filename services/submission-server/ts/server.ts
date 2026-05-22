import net from "node:net";
import { PrismaClient } from "../../../node_modules/@prisma/client";
import { extractThought, normalizeForEmbedding } from "./codeCleaner.js";
import { TimerManager } from "./timer.js";

enum ServerAction {
  START_TIMER = "start_timer",
  STOP_TIMER = "stop_timer",
  DROP_TIMER = "drop_timer",
  GET_ACTIVE_TIMERS = "get_active_timers",
  GET_ACTIVE_SESSIONS = "get_active_sessions",
  SAVE_SUBMISSION = "save_submission",
}

type SubmissionItem = Record<string, unknown>;

function readString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback;
}

class SubmissionServer {
  private readonly host: string;
  private readonly port: number;
  private readonly timerManager = new TimerManager();
  private readonly db = new PrismaClient();

  constructor(host = process.env.SUBMISSION_HOST ?? "127.0.0.1", port = Number(process.env.SUBMISSION_PORT ?? 3000)) {
    this.host = host;
    this.port = Number.isFinite(port) ? port : 3000;
  }

  private startActiveSessionLogger(): void {
    setInterval(() => {
      const timers = this.timerManager.getActiveTimers();
      const entries = Object.entries(timers);
      if (entries.length === 0) {
        console.error("💤 No active sessions");
        return;
      }
      console.error(`\n⏱️  Active sessions (${entries.length}):`);
      for (const [slug, elapsed] of entries) {
        console.error(`   • ${slug}: ${elapsed} min`);
      }
    }, 5000);
  }

  private async saveSubmission(titleSlug: string, content: string, item: SubmissionItem): Promise<boolean> {
    const status = readString(item.status_msg, "Unknown");

    if (content.includes("#TEST#")) {
      console.error(`⊘ Skipping test submission: ${titleSlug}`);
      return false;
    }

    const isCheat = content.includes("#CHEAT#");

    let timeSpentMinutes: number | null = null;
    if (this.timerManager.hasActiveTimer(titleSlug)) {
      timeSpentMinutes = this.timerManager.getElapsedTime(titleSlug);
      console.error(`⏱️  Current elapsed time: ${timeSpentMinutes} minutes`);
    }

    try {
      const cleanedContent = normalizeForEmbedding(content);
      const thought = extractThought(content);

      const submission = await this.db.submission.create({
        data: {
          titleSlug,
          content: cleanedContent,
          status,
          isCheat,
          timeSpentMinutes,
          thought,
          submissionDetails: item,
        },
      });

      if (status === "Accepted") {
        if (this.timerManager.hasActiveTimer(titleSlug)) {
          this.timerManager.stop(titleSlug);
        }
        this.timerManager.start(titleSlug);
        console.error("🔄 Timer restarted for accepted solution");
      }

      const cheatFlag = isCheat ? " [CHEAT - needs revisit]" : "";
      const timeInfo = timeSpentMinutes ? ` (${timeSpentMinutes}min)` : "";
      console.error(
        `✓ Submission saved successfully: ${submission.id} ${titleSlug} ${status}${cheatFlag}${timeInfo}`,
      );

      return true;
    } catch (error) {
      console.error(`✗ Error saving submission: ${String(error)}`);
      return false;
    }
  }

  private async handleRequest(request: Record<string, unknown>): Promise<Record<string, unknown>> {
    const action = readString(request.action);
    console.error(`📨 Received request: ${action}`);

    switch (action) {
      case ServerAction.START_TIMER: {
        const titleSlug = readString(request.title_slug);
        this.timerManager.start(titleSlug, false);
        return { success: true, action: ServerAction.START_TIMER, title_slug: titleSlug };
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
    await this.db.$connect();
    this.startActiveSessionLogger();

    const server = net.createServer((socket) => {
      const peer = `${socket.remoteAddress ?? "unknown"}:${socket.remotePort ?? "?"}`;
      console.error(`🔌 Client connected from ${peer}`);

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
        console.error(`❌ Client disconnected: ${peer}`);
      });

      socket.on("error", (error) => {
        console.error(`⚠️  Client socket error from ${peer}: ${String(error)}`);
      });
    });

    server.listen(this.port, this.host, () => {
      console.error(`🚀 Submission server started on ${this.host}:${this.port}`);
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

const app = new SubmissionServer();
try {
  await app.start();
} catch (error) {
  console.error(error);
  process.exit(1);
}
