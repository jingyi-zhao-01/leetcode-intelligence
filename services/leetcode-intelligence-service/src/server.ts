import express from "express";

import { createIntelligenceService } from "./intelligence.ts";
import { createLogger } from "./logger.ts";

const STARTUP_RETRY_MS = Number(process.env.INTELLIGENCE_STARTUP_RETRY_MS ?? 5000);
const logger = createLogger("server");

const sleep = async (ms: number): Promise<void> => {
  await new Promise((resolve) => setTimeout(resolve, ms));
};

const formatError = (error: unknown): string => {
  if (error instanceof Error) {
    return error.message;
  }

  return String(error);
};

async function main(): Promise<void> {
  const service = await createIntelligenceService();
  let ready = false;
  let startupError: unknown = null;

  const startInBackground = async (): Promise<void> => {
    let attempt = 0;

    while (!ready) {
      attempt += 1;
      try {
        logger.info({ attempt }, "startup attempt: connecting dependencies");
        await service.start();
        ready = true;
        startupError = null;
        logger.info("startup complete");
        return;
      } catch (error) {
        startupError = error;
        logger.error({ attempt, err: error }, "startup failed");
        await sleep(STARTUP_RETRY_MS);
      }
    }
  };

  void startInBackground();

  const app = express();
  app.disable("x-powered-by");
  app.use(express.json({ limit: "1mb" }));

  app.get("/health", async (_req, res) => {
    if (!ready) {
      res.json({
        status: startupError ? "degraded" : "starting",
        service: "leetcode-intelligence-service",
        error: startupError ? formatError(startupError) : undefined,
      });
      return;
    }

    try {
      res.json(await service.health());
    } catch (error) {
      res.json({ status: "degraded", service: "leetcode-intelligence-service", error: formatError(error) });
    }
  });

  app.post("/trigger", async (_req, res) => {
    try {
      if (!ready) {
        res.status(503).json({ error: "Service is still starting." });
        return;
      }
      res.json(await service.triggerPrompt("manual", { channelId: "http" }));
    } catch (error) {
      res.status(500).json({ error: formatError(error) });
    }
  });

  app.post("/reply-by-event", async (req, res) => {
    try {
      if (!ready) {
        res.status(503).json({ ok: false, error: "Service is still starting." });
        return;
      }
      const promptEventId = String(req.body?.promptEventId ?? "").trim();
      const rawReply = String(req.body?.rawReply ?? "").trim();

      if (!promptEventId || !rawReply) {
        res.status(400).json({ ok: false, error: "promptEventId and rawReply are required." });
        return;
      }

      res.json(await service.scorePromptReply(promptEventId, rawReply));
    } catch (error) {
      res.status(500).json({ ok: false, error: formatError(error) });
    }
  });

  app.post("/reply-by-message", async (req, res) => {
    try {
      if (!ready) {
        res.status(503).json({ ok: false, error: "Service is still starting." });
        return;
      }
      const messageId = String(req.body?.messageId ?? "").trim();
      const rawReply = String(req.body?.rawReply ?? "").trim();

      if (!messageId || !rawReply) {
        res.status(400).json({ ok: false, error: "messageId and rawReply are required." });
        return;
      }

      const result = await service.scorePromptReplyByMessageId(messageId, rawReply);
      if (!result) {
        res.status(404).json({ ok: false, error: "No prompt event found for this messageId." });
        return;
      }

      res.json(result);
    } catch (error) {
      res.status(500).json({ ok: false, error: formatError(error) });
    }
  });

  app.get("/recommendations", async (req, res) => {
    try {
      if (!ready) {
        res.status(503).json({ ok: false, error: "Service is still starting." });
        return;
      }
      const limitRaw = Number(req.query.limit);
      const limit = Number.isFinite(limitRaw) && limitRaw > 0 ? limitRaw : undefined;
      res.json(await service.recommendFocus(limit));
    } catch (error) {
      res.status(500).json({ ok: false, error: formatError(error) });
    }
  });

  app.post("/recommendations/trigger", async (req, res) => {
    try {
      if (!ready) {
        res.status(503).json({ ok: false, error: "Service is still starting." });
        return;
      }
      const limitRaw = Number(req.body?.limit);
      const limit = Number.isFinite(limitRaw) && limitRaw > 0 ? limitRaw : undefined;
      res.json(await service.recommendFocus(limit));
    } catch (error) {
      res.status(500).json({ ok: false, error: formatError(error) });
    }
  });

  const port = Number(process.env.INTELLIGENCE_PORT ?? 8030);
  const host = process.env.INTELLIGENCE_HOST ?? "0.0.0.0";
  app.listen(port, host, () => {
    logger.info({ host, port }, "HTTP server listening");
  });

  process.on("SIGINT", async () => {
    await service.stop();
    process.exit(0);
  });

  process.on("SIGTERM", async () => {
    await service.stop();
    process.exit(0);
  });
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled startup error");
  process.exit(1);
}
