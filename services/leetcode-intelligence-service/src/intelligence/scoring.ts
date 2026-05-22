import { OpenRouter } from "@openrouter/sdk";

import {
  type ScoringAlgorithm,
  type LlmScore,
  type ScoreRequest,
} from "./types.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("intelligence/scoring");

const summarizeError = (error: unknown): string => {
  if (!(error instanceof Error)) {
    return String(error);
  }

  const details = error as Error & {
    status?: number;
    statusCode?: number;
    code?: string;
    cause?: unknown;
    body?: unknown;
    response?: {
      status?: number;
      statusText?: string;
      data?: unknown;
      body?: unknown;
    };
  };

  const status = details.statusCode ?? details.status ?? details.response?.status;
  const code = details.code;
  const responseBody = details.body ?? details.response?.data ?? details.response?.body;

  const parts = [
    `${details.name}: ${details.message}`,
    status ? `status=${status}` : "",
    code ? `code=${code}` : "",
    responseBody ? `response=${JSON.stringify(responseBody)}` : "",
  ].filter(Boolean);

  return parts.join(" | ");
};

const clamp = (value: number, min: number, max: number): number => {
  return Math.max(min, Math.min(max, value));
};

const truncate = (value: string, maxLength: number): string => {
  if (value.length <= maxLength) {
    return value;
  }
  return `${value.slice(0, maxLength - 3)}...`;
};

const parseStructuredJson = (content: string): LlmScore => {
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
};

const fallbackStructuredScore = (rawReply: string): LlmScore => {
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
};

export class OpenRouterScoringAlgorithm implements ScoringAlgorithm {
  constructor(
    private readonly openRouter: OpenRouter,
    private readonly model: string,
  ) {}

  async score(request: ScoreRequest): Promise<LlmScore> {
    logger.info(
      {
        model: this.model,
        questionSlug: request.questionSlug,
        replyChars: request.rawReply.length,
      },
      "requesting OpenRouter score",
    );

    const response = await this.openRouter.chat.send({
      chatRequest: {
        model: this.model,
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
              questionSlug: request.questionSlug,
              promptText: request.promptText,
              selectedSubmission: {
                id: request.submission.id,
                content: truncate(request.submission.content, 1200),
                status: request.submission.status,
              },
              reply: request.rawReply,
            }),
          },
        ],
      },
    });

    const text = response.choices?.[0]?.message?.content ?? "{}";
    if (!response.choices?.length) {
      logger.warn({ model: this.model, questionSlug: request.questionSlug }, "OpenRouter response had no choices");
    }
    return parseStructuredJson(text);
  }
}

export class FallbackScoringAlgorithm implements ScoringAlgorithm {
  async score(request: ScoreRequest): Promise<LlmScore> {
    return fallbackStructuredScore(request.rawReply);
  }
}

export class ReplyScorer {
  constructor(
    private readonly primary: ScoringAlgorithm | null,
    private readonly fallback: ScoringAlgorithm,
  ) {}

  async score(request: ScoreRequest): Promise<LlmScore> {
    if (!this.primary) {
      return this.fallback.score(request);
    }

    try {
      return await this.primary.score(request);
    } catch (error) {
      logger.warn({ err: error }, "OpenRouter scoring unavailable, using fallback scorer");
      return this.fallback.score(request);
    }
  }
}
