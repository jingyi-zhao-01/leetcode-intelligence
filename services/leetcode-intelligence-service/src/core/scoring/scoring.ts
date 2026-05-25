import { OpenRouter } from "@openrouter/sdk";

import {
  type ScoringAlgorithm,
  type LlmScore,
  type ScoreRequest,
} from "../types.ts";
import { createLogger } from "../../logger.ts";
import { clamp } from "../shared/weight.ts";

const logger = createLogger("intelligence/scoring");

const INTERVIEW_SCORING_PROMPT = `
You are scoring a candidate's LeetCode interview discussion reply, not grading a final coded solution.

Score the reply from 1-5 based on the quality of the candidate's thinking:
- correctness of the proposed approach
- completeness of the reasoning
- soundness of assumptions and edge-case handling
- clarity around complexity tradeoffs
- awareness of blind spots, risks, or missing cases

Do not require code. Do not penalize the candidate for not providing code, syntax, or a fully implemented solution.
If the reasoning is strong, accurate, and interview-sound, it can earn a high score without code.
If the reply is vague, incorrect, logically unsound, or misses important constraints, lower the score accordingly.

Return JSON with:
- score: integer 1-5
- approachSummary: short summary of the candidate's proposed approach
- complexityNotes: brief note on complexity discussion quality
- blindSpots: important missing cases, incorrect assumptions, or weaknesses
- tags: short labels describing the reasoning quality
- reason: concise explanation for the score
`.trim();

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
            content: INTERVIEW_SCORING_PROMPT,
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
