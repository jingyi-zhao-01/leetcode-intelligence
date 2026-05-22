import { randomInt } from "node:crypto";
import path from "node:path";

import { PrismaClient } from "@prisma/client";
import { config as loadDotenv } from "dotenv";
import { OpenRouter } from "@openrouter/sdk";
import { z } from "zod";

loadDotenv({ path: path.resolve(process.cwd(), ".env") });

const envSchema = z.object({
  DATABASE_URL: z.string().min(1),
  OPEN_ROUTER_API_KEY: z.string().min(1).optional(),
  API_KEY: z.string().min(1).optional(),
  MODEL: z.string().min(1).default("openai/gpt-4o-mini"),
  INTELLIGENCE_PORT: z.coerce.number().int().positive().default(8030),
  INTELLIGENCE_HOST: z.string().min(1).default("0.0.0.0"),
  INTELLIGENCE_CRON: z.string().min(1).default("0 9 * * *"),
  INTELLIGENCE_MAX_CANDIDATES: z.coerce.number().int().positive().default(500),
  INTELLIGENCE_SELECTION_WINDOW: z.coerce.number().int().positive().default(200),
  INTELLIGENCE_MIN_WEIGHT: z.coerce.number().positive().default(0.25),
  INTELLIGENCE_MAX_WEIGHT: z.coerce.number().positive().default(5),
});

export type IntelligenceConfig = z.infer<typeof envSchema>;

type CandidateSubmission = {
  id: string;
  titleSlug: string | null;
  content: string;
  status: string;
  createdAt: Date;
};

type CandidateQuestion = {
  title: string;
  titleSlug: string;
  difficulty: string;
  content: string | null;
  topicTags: string[];
  freqBar: number | null;
};

type IntelligencePromptEventRecord = {
  id: string;
  questionSlug: string;
  promptText: string;
  selectedAt: Date;
  weightBefore: number | null;
  Submission: CandidateSubmission;
  IntelligenceResponse: { id: string } | null;
};

type LlmScore = {
  score: number;
  approachSummary: string;
  complexityNotes: string;
  blindSpots: string;
  tags: string[];
  reason: string;
};

type WeightedCandidate = {
  submission: CandidateSubmission;
  question: CandidateQuestion;
  weight: number;
};

type PromptTransport = {
  channelId: string;
  messageId?: string | null;
};

type PromptEventWithRelations = {
  id: string;
  questionSlug: string;
  promptText: string;
  selectedAt: Date;
  weightBefore: number | null;
  Submission: CandidateSubmission;
  Question: CandidateQuestion;
  IntelligenceResponse: { id: string } | null;
};

function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value));
}

function truncate(value: string, maxLength: number): string {
  if (value.length <= maxLength) {
    return value;
  }
  return `${value.slice(0, maxLength - 3)}...`;
}

function parseStructuredJson(content: string): LlmScore {
  const parsed = JSON.parse(content) as Partial<LlmScore>;
  const score = Number(parsed.score ?? 3);
  return {
    score: clamp(Number.isFinite(score) ? score : 3, 1, 5),
    approachSummary: String(parsed.approachSummary ?? ""),
    complexityNotes: String(parsed.complexityNotes ?? ""),
    blindSpots: String(parsed.blindSpots ?? ""),
    tags: Array.isArray(parsed.tags) ? parsed.tags.map((tag) => String(tag).trim()).filter(Boolean) : [],
    reason: String(parsed.reason ?? ""),
  };
}

function buildPromptText(question: CandidateQuestion, submission: CandidateSubmission): string {
  const description = question.content?.trim() || `${question.title} (${question.difficulty})`;

  return [
    `Problem: ${question.title} [${question.titleSlug}]`,
    `Difficulty: ${question.difficulty}`,
    `Topics: ${(question.topicTags ?? []).join(", ") || "n/a"}`,
    "",
    "Problem description:",
    description,
    "",
    "Past submission:",
    `Submission ID: ${submission.id}`,
    `Status: ${submission.status}`,
    `SubmittedAt: ${submission.createdAt.toISOString()}`,
    "",
    "Reply in this channel with your approach. Include your reasoning, complexity, and any blind spot you see.",
  ].join("\n");
}

function scoreToWeightDelta(score: number): number {
  // score 5 -> -0.5, score 3 -> 0, score 1 -> +0.5
  return (3 - score) * 0.25;
}

function fallbackStructuredScore(rawReply: string): LlmScore {
  const cleanedReply = rawReply.trim();
  let score = 2;
  if (cleanedReply.length >= 120) {
    score = 4;
  } else if (cleanedReply.length >= 40) {
    score = 3;
  }

  return {
    score,
    approachSummary: truncate(cleanedReply || "No reply provided.", 240),
    complexityNotes: "Fallback scorer used because OpenRouter scoring is unavailable.",
    blindSpots: "",
    tags: ["fallback", "cli-e2e"],
    reason: "Used local fallback scoring because OpenRouter was unavailable or rejected the API key.",
  };
}

export class IntelligenceService {
  private readonly prisma: any = new PrismaClient();
  private readonly openRouter: OpenRouter | null;

  constructor(private readonly config: IntelligenceConfig) {
    const apiKey = this.config.OPEN_ROUTER_API_KEY ?? this.config.API_KEY;
    this.openRouter = apiKey
      ? new OpenRouter({
          apiKey,
          httpReferer: "https://github.com/kawre/leetcode.nvim",
          appTitle: "leetcode-intelligence-service",
        })
      : null;
  }

  async start(): Promise<void> {
    await this.prisma.$connect();
  }

  async stop(): Promise<void> {
    await this.prisma.$disconnect().catch(() => undefined);
  }

  async health(): Promise<Record<string, unknown>> {
    const count = await this.prisma.intelligencePromptEvent.count();
    return {
      status: "ok",
      service: "leetcode-intelligence-service",
      prompts: count,
    };
  }

  async triggerPrompt(triggerSource = "manual", transport?: PromptTransport): Promise<Record<string, unknown>> {
    const resolvedTransport = transport ?? { channelId: "cli" };
    const candidate = await this.pickCandidate();
    if (!candidate) {
      return { ok: false, message: "No candidate submission found." };
    }

    const promptText = buildPromptText(candidate.question, candidate.submission);
    const weightBefore = candidate.weight;

    const promptEvent = await this.prisma.intelligencePromptEvent.create({
      data: {
        questionSlug: candidate.question.titleSlug,
        submissionId: candidate.submission.id,
        promptText,
        triggerSource,
        discordChannelId: resolvedTransport.channelId,
        discordMessageId: resolvedTransport.messageId ?? null,
        weightBefore,
        metadata: {
          selectionWindow: this.config.INTELLIGENCE_SELECTION_WINDOW,
          selectedSubmissionStatus: candidate.submission.status,
          selectedSubmissionAt: candidate.submission.createdAt.toISOString(),
        },
      },
    });

    await this.prisma.intelligenceWeight.upsert({
      where: { questionSlug: candidate.question.titleSlug },
      create: {
        questionSlug: candidate.question.titleSlug,
        weight: weightBefore,
        sampleCount: 1,
        lastPromptAt: new Date(),
      },
      update: {
        sampleCount: { increment: 1 },
        lastPromptAt: new Date(),
      },
    });

    return {
      ok: true,
      promptEventId: promptEvent.id,
      questionSlug: candidate.question.titleSlug,
      submissionId: candidate.submission.id,
      weightBefore,
      promptText,
    };
  }

  async attachPromptMessage(promptEventId: string, messageId: string): Promise<void> {
    await this.prisma.intelligencePromptEvent.update({
      where: { id: promptEventId },
      data: {
        discordMessageId: messageId,
      },
    });
  }

  async scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    const promptEvent = (await this.prisma.intelligencePromptEvent.findUnique({
      where: { id: promptEventId },
      include: { Question: true, Submission: true, IntelligenceResponse: true },
    })) as PromptEventWithRelations | null;

    if (!promptEvent) {
      throw new Error(`Prompt event ${promptEventId} not found.`);
    }

    if (promptEvent.IntelligenceResponse) {
      return { ok: false, message: "Prompt event already scored.", promptEventId };
    }

    let structured: LlmScore;
    try {
      structured = await this.scoreDiscordReply(
        {
          questionSlug: promptEvent.questionSlug,
          promptText: promptEvent.promptText,
          Submission: promptEvent.Submission,
        },
        rawReply,
      );
    } catch (error) {
      console.error(`OpenRouter scoring unavailable, using fallback scorer: ${String(error)}`);
      structured = fallbackStructuredScore(rawReply);
    }
    const previousWeight = promptEvent.weightBefore ?? 1;
    const nextWeight = clamp(previousWeight + scoreToWeightDelta(structured.score), this.config.INTELLIGENCE_MIN_WEIGHT, this.config.INTELLIGENCE_MAX_WEIGHT);

    await this.prisma.$transaction(async (tx: any) => {
      await tx.intelligenceResponse.create({
        data: {
          promptEventId,
          rawContent: rawReply,
          structuredTags: structured.tags,
          approachSummary: structured.approachSummary,
          complexityNotes: structured.complexityNotes,
          blindSpots: structured.blindSpots,
          llmScore: structured.score,
          llmReason: structured.reason,
        },
      });

      await tx.intelligencePromptEvent.update({
        where: { id: promptEventId },
        data: {
          respondedAt: new Date(),
          scoredAt: new Date(),
          responseScore: structured.score,
          weightAfter: nextWeight,
          status: "scored",
        },
      });

      await tx.intelligenceWeight.upsert({
        where: { questionSlug: promptEvent.questionSlug },
        create: {
          questionSlug: promptEvent.questionSlug,
          weight: nextWeight,
          sampleCount: 1,
          lastScore: structured.score,
          lastPromptAt: promptEvent.selectedAt,
          lastResponseAt: new Date(),
        },
        update: {
          weight: nextWeight,
          lastScore: structured.score,
          lastResponseAt: new Date(),
        },
      });

      await tx.intelligenceWeightAudit.create({
        data: {
          questionSlug: promptEvent.questionSlug,
          promptEventId,
          previousWeight,
          nextWeight,
          score: structured.score,
          reason: structured.reason,
        },
      });
    });

    return {
      ok: true,
      promptEventId,
      questionSlug: promptEvent.questionSlug,
      score: structured.score,
      previousWeight,
      nextWeight,
      tags: structured.tags,
      reason: structured.reason,
    };
  }

  async scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    const promptEvent = await this.prisma.intelligencePromptEvent.findUnique({
      where: { discordMessageId: messageId },
      select: { id: true },
    });

    if (!promptEvent) {
      return null;
    }

    return this.scorePromptReply(promptEvent.id, rawReply);
  }

  private async pickCandidate(): Promise<{
    submission: CandidateSubmission;
    question: CandidateQuestion;
    weight: number;
  } | null> {
    const submissions = (await this.prisma.submission.findMany({
      where: { titleSlug: { not: null } },
      orderBy: { createdAt: "desc" },
      take: this.config.INTELLIGENCE_MAX_CANDIDATES,
    })) as CandidateSubmission[];

    if (submissions.length === 0) {
      return null;
    }

    const titleSlugs = [...new Set(submissions.map((submission) => submission.titleSlug).filter(Boolean) as string[])];
    const questions = (await this.prisma.question.findMany({
      where: { titleSlug: { in: titleSlugs } },
    })) as CandidateQuestion[];
    const questionBySlug = new Map<string, CandidateQuestion>(questions.map((question) => [question.titleSlug, question]));

    const weights = (await this.prisma.intelligenceWeight.findMany({
      where: { questionSlug: { in: titleSlugs } },
    })) as Array<{ questionSlug: string; weight: number }>;
    const weightBySlug = new Map(weights.map((weight) => [weight.questionSlug, weight.weight]));

    const candidates = submissions
      .map<WeightedCandidate | null>((submission) => {
        const titleSlug = submission.titleSlug;
        if (!titleSlug) {
          return null;
        }
        const question = questionBySlug.get(titleSlug);
        if (!question) {
          return null;
        }
        return {
          submission: {
            id: submission.id,
            titleSlug,
            content: submission.content,
            status: submission.status,
            createdAt: submission.createdAt,
          },
          question: {
            title: question.title,
            titleSlug: question.titleSlug,
            difficulty: question.difficulty,
            content: question.content,
            topicTags: question.topicTags,
            freqBar: question.freqBar,
          },
          weight: weightBySlug.get(titleSlug) ?? 1,
        };
      })
      .filter((candidate): candidate is WeightedCandidate => candidate !== null)
      .slice(0, this.config.INTELLIGENCE_SELECTION_WINDOW);

    if (candidates.length === 0) {
      return null;
    }

    const totalWeight = candidates.reduce((sum: number, candidate: { weight: number }) => sum + Math.max(candidate.weight, 0.01), 0);
    let cursor = randomInt(0, 1_000_000) / 1_000_000 * totalWeight;

    for (const candidate of candidates) {
      cursor -= Math.max(candidate.weight, 0.01);
      if (cursor <= 0) {
        return candidate;
      }
    }

    return candidates.at(-1) ?? null;
  }

  private async scoreDiscordReply(promptEvent: {
    questionSlug: string;
    promptText: string;
    Submission: CandidateSubmission;
  }, rawReply: string): Promise<LlmScore> {
    if (!this.openRouter) {
      throw new Error("OPEN_ROUTER_API_KEY or API_KEY is required for OpenRouter scoring.");
    }

    const response = await this.openRouter.chat.send({
      chatRequest: {
        model: this.config.MODEL,
        temperature: 0.2,
        responseFormat: { type: "json_object" },
        messages: [
          {
            role: "system",
            content: "You score a LeetCode discussion reply. Return JSON with score (1-5), approachSummary, complexityNotes, blindSpots, tags, and reason.",
          },
          {
            role: "user",
            content: JSON.stringify({
              questionSlug: promptEvent.questionSlug,
              promptText: promptEvent.promptText,
              selectedSubmission: {
                id: promptEvent.Submission.id,
                content: truncate(promptEvent.Submission.content, 1200),
                status: promptEvent.Submission.status,
              },
              reply: rawReply,
            }),
          },
        ],
      },
    });

    const text = response.choices?.[0]?.message?.content ?? "{}";
    return parseStructuredJson(text);
  }
}

export function loadIntelligenceConfig(): IntelligenceConfig {
  const parsed = envSchema.safeParse(process.env);
  if (!parsed.success) {
    const issues = parsed.error.issues.map((issue) => `${issue.path.join(".")}: ${issue.message}`).join("; ");
    throw new Error(`Invalid intelligence service environment: ${issues}`);
  }
  return parsed.data;
}

export async function createIntelligenceService(): Promise<IntelligenceService> {
  return new IntelligenceService(loadIntelligenceConfig());
}
