import express from "express";

import { createIntelligenceService } from "./intelligence.ts";

async function main(): Promise<void> {
  const service = await createIntelligenceService();
  await service.start();

  const app = express();
  app.disable("x-powered-by");
  app.use(express.json({ limit: "1mb" }));

  app.get("/health", async (_req, res) => {
    res.json(await service.health());
  });

  app.post("/trigger", async (_req, res) => {
    try {
      res.json(await service.triggerPrompt("manual", { channelId: "http" }));
    } catch (error) {
      res.status(500).json({ error: String(error) });
    }
  });

  app.post("/reply-by-event", async (req, res) => {
    try {
      const promptEventId = String(req.body?.promptEventId ?? "").trim();
      const rawReply = String(req.body?.rawReply ?? "").trim();

      if (!promptEventId || !rawReply) {
        res.status(400).json({ ok: false, error: "promptEventId and rawReply are required." });
        return;
      }

      res.json(await service.scorePromptReply(promptEventId, rawReply));
    } catch (error) {
      res.status(500).json({ ok: false, error: String(error) });
    }
  });

  app.post("/reply-by-message", async (req, res) => {
    try {
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
      res.status(500).json({ ok: false, error: String(error) });
    }
  });

  app.get("/recommendations", async (req, res) => {
    try {
      const limitRaw = Number(req.query.limit);
      const limit = Number.isFinite(limitRaw) && limitRaw > 0 ? limitRaw : undefined;
      res.json(await service.recommendFocus(limit));
    } catch (error) {
      res.status(500).json({ ok: false, error: String(error) });
    }
  });

  app.post("/recommendations/trigger", async (req, res) => {
    try {
      const limitRaw = Number(req.body?.limit);
      const limit = Number.isFinite(limitRaw) && limitRaw > 0 ? limitRaw : undefined;
      res.json(await service.recommendFocus(limit));
    } catch (error) {
      res.status(500).json({ ok: false, error: String(error) });
    }
  });

  const port = Number(process.env.INTELLIGENCE_PORT ?? 8030);
  const host = process.env.INTELLIGENCE_HOST ?? "0.0.0.0";
  app.listen(port, host, () => {
    console.error(`Intelligence HTTP server listening on ${host}:${port}`);
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
  console.error(error);
  process.exit(1);
}
