import express from "express";
import { PrismaClient } from "../../../node_modules/@prisma/client";
import { z } from "zod";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  analyzeThoughtProgression,
  checkProblemSolved,
  getProblemDetails,
  getRelatedProblems,
  getSubmissionDetail,
  getSubmissionHistory,
  listPopularProblems,
  listProblemsByFilters,
  reviewSubmissions,
  saveSubmissionMistakes,
  searchProblems,
} from "./tools.js";

const db = new PrismaClient();

function parsePort(raw: string | undefined, fallback = 8000): number {
  const parsed = Number(raw);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    return fallback;
  }
  return parsed;
}

function jsonToolResult(data: unknown) {
  return {
    content: [{ type: "text" as const, text: JSON.stringify(data, null, 2) }],
    structuredContent: data as Record<string, unknown>,
  };
}

function registerMcpTools(server: any) {
  server.tool(
    "get_submission_history",
    "List all submissions for a specific problem.",
    { title_slug: z.string() },
    async ({ title_slug }: { title_slug: string }) =>
      jsonToolResult(await getSubmissionHistory(db, title_slug)),
  );

  server.tool(
    "analyze_thought_progression",
    "Analyze comment and thought evolution across submissions.",
    { title_slug: z.string() },
    async ({ title_slug }: { title_slug: string }) =>
      jsonToolResult(await analyzeThoughtProgression(db, title_slug)),
  );

  server.tool(
    "review_submissions",
    "Review submissions by period or explicit date range.",
    {
      period: z.string().optional(),
      start_date: z.string().optional(),
      end_date: z.string().optional(),
    },
    async ({ period, start_date, end_date }: { period?: string; start_date?: string; end_date?: string }) =>
      jsonToolResult(await reviewSubmissions(db, period, start_date, end_date)),
  );

  server.tool(
    "search_problems",
    "Search problems by query, topic and difficulty.",
    {
      query: z.string(),
      topic: z.string().optional(),
      difficulty: z.string().optional(),
      limit: z.number().optional(),
      offset: z.number().optional(),
    },
    async ({ query, topic, difficulty, limit, offset }: { query: string; topic?: string; difficulty?: string; limit?: number; offset?: number }) =>
      jsonToolResult(await searchProblems(db, query, topic, difficulty, limit, offset)),
  );

  server.tool(
    "get_problem_details",
    "Get a problem with submission summary.",
    { slug: z.string() },
    async ({ slug }: { slug: string }) => jsonToolResult(await getProblemDetails(db, slug)),
  );

  server.tool(
    "get_related_problems",
    "Get related problems for a slug.",
    {
      slug: z.string(),
      include_details: z.boolean().optional(),
    },
    async ({ slug, include_details }: { slug: string; include_details?: boolean }) =>
      jsonToolResult(await getRelatedProblems(db, slug, include_details ?? true)),
  );

  server.tool(
    "list_problems_by_filters",
    "List problems by topics, difficulty and sorting.",
    {
      topics: z.array(z.string()).optional(),
      difficulty: z.string().optional(),
      sort_by: z.string().optional(),
      limit: z.number().optional(),
      offset: z.number().optional(),
    },
    async ({ topics, difficulty, sort_by, limit, offset }: { topics?: string[]; difficulty?: string; sort_by?: string; limit?: number; offset?: number }) =>
      jsonToolResult(await listProblemsByFilters(db, topics, difficulty, sort_by, limit, offset)),
  );

  server.tool(
    "list_popular_problems",
    "List popular problems by frequency score.",
    {
      topic: z.string().optional(),
      difficulty: z.string().optional(),
      limit: z.number().optional(),
      offset: z.number().optional(),
    },
    async ({ topic, difficulty, limit, offset }: { topic?: string; difficulty?: string; limit?: number; offset?: number }) =>
      jsonToolResult(await listPopularProblems(db, topic, difficulty, limit, offset)),
  );

  server.tool(
    "check_problem_solved",
    "Check whether a problem has at least one accepted submission.",
    { slug: z.string() },
    async ({ slug }: { slug: string }) => jsonToolResult(await checkProblemSolved(db, slug)),
  );

  server.tool(
    "get_submission_detail",
    "Get all fields for one submission.",
    { submission_id: z.string() },
    async ({ submission_id }: { submission_id: string }) =>
      jsonToolResult(await getSubmissionDetail(db, submission_id)),
  );

  server.tool(
    "save_submission_mistakes",
    "Save mistakes for a submission; this is the only retained mutation tool.",
    {
      submission_id: z.string(),
      mistakes: z.array(z.string()),
    },
    async ({ submission_id, mistakes }: { submission_id: string; mistakes: string[] }) =>
      jsonToolResult(await saveSubmissionMistakes(db, submission_id, mistakes)),
  );
}

async function startStdio() {
  await db.$connect();
  const server = new McpServer({
    name: "LeetCode Submission Evolution Server",
    version: "0.2.0",
  });
  registerMcpTools(server);

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

async function startHttp() {
  await db.$connect();

  const app = express();
  app.disable("x-powered-by");
  app.use(express.json({ limit: "1mb" }));

  app.get("/health", (_req: any, res: any) => {
    res.json({ status: "ok", service: "mcp-server-ts" });
  });

  app.post("/tools/get_submission_history", async (req: any, res: any) => {
    res.json(await getSubmissionHistory(db, req.body.title_slug));
  });

  app.post("/tools/analyze_thought_progression", async (req: any, res: any) => {
    res.json(await analyzeThoughtProgression(db, req.body.title_slug));
  });

  app.post("/tools/review_submissions", async (req: any, res: any) => {
    res.json(await reviewSubmissions(db, req.body.period, req.body.start_date, req.body.end_date));
  });

  app.post("/tools/search_problems", async (req: any, res: any) => {
    res.json(
      await searchProblems(
        db,
        req.body.query,
        req.body.topic,
        req.body.difficulty,
        req.body.limit,
        req.body.offset,
      ),
    );
  });

  app.post("/tools/get_problem_details", async (req: any, res: any) => {
    res.json(await getProblemDetails(db, req.body.slug));
  });

  app.post("/tools/get_related_problems", async (req: any, res: any) => {
    res.json(await getRelatedProblems(db, req.body.slug, req.body.include_details ?? true));
  });

  app.post("/tools/list_problems_by_filters", async (req: any, res: any) => {
    res.json(
      await listProblemsByFilters(
        db,
        req.body.topics,
        req.body.difficulty,
        req.body.sort_by,
        req.body.limit,
        req.body.offset,
      ),
    );
  });

  app.post("/tools/list_popular_problems", async (req: any, res: any) => {
    res.json(await listPopularProblems(db, req.body.topic, req.body.difficulty, req.body.limit, req.body.offset));
  });

  app.post("/tools/check_problem_solved", async (req: any, res: any) => {
    res.json(await checkProblemSolved(db, req.body.slug));
  });

  app.post("/tools/get_submission_detail", async (req: any, res: any) => {
    res.json(await getSubmissionDetail(db, req.body.submission_id));
  });

  app.post("/tools/save_submission_mistakes", async (req: any, res: any) => {
    res.json(await saveSubmissionMistakes(db, req.body.submission_id, req.body.mistakes));
  });

  const port = parsePort(process.env.MCP_PORT, 8000);
  app.listen(port, () => {
    console.error(`MCP insight HTTP server listening on :${port}`);
  });
}

async function main() {
  const transport = process.argv[2] ?? "http";
  if (transport === "stdio") {
    await startStdio();
    return;
  }
  await startHttp();
}

try {
  await main();
} catch (error) {
  console.error(error);
  await db.$disconnect().catch(() => undefined);
  process.exit(1);
}

process.on("SIGINT", async () => {
  await db.$disconnect().catch(() => undefined);
  process.exit(0);
});

process.on("SIGTERM", async () => {
  await db.$disconnect().catch(() => undefined);
  process.exit(0);
});
