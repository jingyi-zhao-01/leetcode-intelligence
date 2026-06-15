import { timingSafeEqual } from "node:crypto";

import express from "express";

import { createBffApi } from "./api/index.ts";
import { ensureServiceEnvLoaded } from "./core/load-env.ts";
import { createLogger } from "./logger.ts";
import { runBffRoute } from "./observability/bff.ts";
import { createHttpTracingMiddleware } from "./observability/http.ts";
import { configureTracing, shutdownTracing } from "./observability/tracing.ts";
import { createIntelligenceServiceRuntime } from "./service-runtime/index.ts";

ensureServiceEnvLoaded();

const SERVICE_NAME = "leetcode-intelligence-service";
const STARTUP_RETRY_MS = Number(process.env.INTELLIGENCE_STARTUP_RETRY_MS ?? 5000);
const logger = createLogger("server");
const BFF_TOKEN = process.env.BFF_TOKEN?.trim() || process.env.BFF_SERVICE_TOKEN?.trim() || "";

const sleep = async (ms: number): Promise<void> => {
  await new Promise((resolve) => setTimeout(resolve, ms));
};

const formatError = (error: unknown): string => {
  if (error instanceof Error) {
    return error.message;
  }

  return String(error);
};

const readBearerToken = (authorizationHeader: string | undefined): string | null => {
  if (!authorizationHeader) {
    return null;
  }

  const [scheme, token] = authorizationHeader.split(" ", 2);
  if (!scheme || !token || scheme.toLowerCase() !== "bearer") {
    return null;
  }

  return token.trim() || null;
};

const tokenMatches = (candidate: string | null): boolean => {
  if (!candidate || !BFF_TOKEN) {
    return false;
  }

  const expectedBuffer = Buffer.from(BFF_TOKEN);
  const candidateBuffer = Buffer.from(candidate);

  if (expectedBuffer.length !== candidateBuffer.length) {
    return false;
  }

  return timingSafeEqual(expectedBuffer, candidateBuffer);
};

async function main(): Promise<void> {
  if (!BFF_TOKEN) {
    throw new Error("BFF_TOKEN is required for authenticated HTTP access.");
  }

  await configureTracing(SERVICE_NAME);

  const { composition, service } = createIntelligenceServiceRuntime();
  const bffApi = createBffApi({ prisma: composition.persistence.prisma });
  let ready = false;
  let startupError: unknown = null;
  let shutdownPromise: Promise<void> | null = null;

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
  app.use("/bff", createHttpTracingMiddleware(SERVICE_NAME, "bff"));
  app.use((req, res, next) => {
    if (req.path === "/health") {
      next();
      return;
    }

    const token = readBearerToken(req.header("authorization"));
    if (!tokenMatches(token)) {
      res.status(401).json({ error: "Unauthorized" });
      return;
    }

    next();
  });

  app.get("/health", async (_req, res) => {
    if (!ready) {
      res.json({
        status: startupError ? "degraded" : "starting",
        service: SERVICE_NAME,
        error: startupError ? formatError(startupError) : undefined,
      });
      return;
    }

    res.json(await service.health());
  });

  app.get("/bff/tag-workbench", async (req, res) => {
    await runBffRoute(req, res, "tag_workbench", async () => bffApi.getTagWorkbenchData());
  });

  app.get("/bff/templates-page", async (req, res) => {
    await runBffRoute(req, res, "templates_page", async () => bffApi.getTemplatesPageData());
  });

  app.get("/bff/graph-page", async (req, res) => {
    await runBffRoute(req, res, "graph_page", async () => bffApi.getGraphPageData());
  });

  app.post("/bff/submissions/:submissionId/tags", async (req, res) => {
    await runBffRoute(req, res, "submission_tags", async () => {
      const submissionId = String(req.params.submissionId ?? "").trim();
      const patternTagIds = Array.isArray(req.body?.patternTagIds)
        ? req.body.patternTagIds.filter((value: unknown): value is string => typeof value === "string")
        : [];

      if (!submissionId) {
        res.status(400).json({ error: "submissionId is required." });
        return;
      }

      return bffApi.saveSubmissionTags(submissionId, patternTagIds);
    });
  });

  app.post("/bff/submissions/:submissionId/template-benchmark", async (req, res) => {
    await runBffRoute(req, res, "submission_template_benchmark", async () => {
      const submissionId = String(req.params.submissionId ?? "").trim();
      const excludedGroupKeys = Array.isArray(req.body?.excludedGroupKeys)
        ? req.body.excludedGroupKeys.filter((value: unknown): value is string => typeof value === "string")
        : [];

      if (!submissionId) {
        res.status(400).json({ error: "submissionId is required." });
        return;
      }

      return bffApi.benchmarkSubmissionTemplates(submissionId, excludedGroupKeys);
    });
  });

  app.post("/bff/submissions/:submissionId/template-benchmark-opt-out", async (req, res) => {
    await runBffRoute(req, res, "submission_template_benchmark_opt_out", async () => {
      const submissionId = String(req.params.submissionId ?? "").trim();
      const templateBenchmarkOptOut = Boolean(req.body?.templateBenchmarkOptOut);

      if (!submissionId) {
        res.status(400).json({ error: "submissionId is required." });
        return;
      }

      return bffApi.setSubmissionTemplateOptOut(submissionId, templateBenchmarkOptOut);
    });
  });

  app.post("/bff/templates/draft", async (req, res) => {
    await runBffRoute(req, res, "template_draft", async () => {
      const groupKey = String(req.body?.groupKey ?? "").trim();
      const submissionId = String(req.body?.submissionId ?? "").trim();
      const prompt = String(req.body?.prompt ?? "").trim();
      const model = typeof req.body?.model === "string" ? req.body.model : undefined;

      if (!groupKey || !submissionId || !prompt) {
        res.status(400).json({ error: "groupKey, submissionId, and prompt are required." });
        return;
      }

      return bffApi.generateTemplateDraft({ groupKey, submissionId, prompt, model });
    });
  });

  app.post("/bff/templates/generated", async (req, res) => {
    await runBffRoute(req, res, "generated_template", async () => {
      const groupKey = String(req.body?.groupKey ?? "").trim();
      const draft = req.body?.draft;

      if (!groupKey || !draft || typeof draft !== "object" || Array.isArray(draft)) {
        res.status(400).json({ error: "groupKey and draft are required." });
        return;
      }

      return bffApi.createGeneratedTemplate(groupKey, draft);
    });
  });

  app.post("/bff/template-groups", async (req, res) => {
    await runBffRoute(req, res, "template_group_create", async () =>
      bffApi.createTemplateGroup({
        label: String(req.body?.label ?? ""),
        key: typeof req.body?.key === "string" ? req.body.key : undefined,
        description: typeof req.body?.description === "string" ? req.body.description : undefined,
      }),
    );
  });

  app.post("/bff/templates/move", async (req, res) => {
    await runBffRoute(req, res, "template_move", async () => {
      const templateId = String(req.body?.templateId ?? "").trim();
      const targetGroupId = String(req.body?.targetGroupId ?? "").trim();

      if (!templateId || !targetGroupId) {
        res.status(400).json({ error: "templateId and targetGroupId are required." });
        return;
      }

      return bffApi.moveTemplateToGroup({ templateId, targetGroupId });
    });
  });

  app.delete("/bff/templates/:patternTagId", async (req, res) => {
    await runBffRoute(req, res, "template_delete", async () => {
      const patternTagId = String(req.params.patternTagId ?? "").trim();
      if (!patternTagId) {
        res.status(400).json({ error: "patternTagId is required." });
        return;
      }

      return bffApi.deleteNonSeededTemplate(patternTagId);
    });
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

  const shutdown = async (signal: NodeJS.Signals) => {
    if (!shutdownPromise) {
      shutdownPromise = (async () => {
        logger.info({ signal }, "shutdown requested");
        await service.stop();
        await shutdownTracing();
      })();
    }

    try {
      await shutdownPromise;
      process.exit(0);
    } catch (error) {
      logger.error({ signal, err: error }, "shutdown failed");
      process.exit(1);
    }
  };

  process.on("SIGINT", () => {
    void shutdown("SIGINT");
  });

  process.on("SIGTERM", () => {
    void shutdown("SIGTERM");
  });
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled startup error");
  process.exit(1);
}
