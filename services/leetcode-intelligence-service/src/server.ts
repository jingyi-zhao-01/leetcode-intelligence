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
