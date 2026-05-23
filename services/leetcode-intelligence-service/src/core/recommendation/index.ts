import { OpenRouter } from "@openrouter/sdk";

import type {
  FocusRecommendation,
  FocusRecommendationResult,
  IntelligenceConfig,
} from "../types.ts";
import { createLogger } from "../../logger.ts";
import { clamp, normalizedWeightSignal } from "../shared/weight.ts";

const logger = createLogger("intelligence/recommendation");

const DAY_MS = 24 * 60 * 60 * 1000;

const round = (value: number, digits = 3): number => {
  const factor = 10 ** digits;
  return Math.round(value * factor) / factor;
};

const daysSince = (value: Date | null | undefined): number => {
  if (!value) {
    return 365;
  }
  return Math.max(0, (Date.now() - value.getTime()) / DAY_MS);
};

const normalizeStatus = (status: string | null | undefined): string => {
  return (status ?? "").trim().toLowerCase();
};

const isFailedStatus = (status: string | null | undefined): boolean => {
  const normalized = normalizeStatus(status);
  return ["wrong answer", "runtime error", "time limit exceeded", "memory limit exceeded", "compile error"].includes(normalized);
};

const difficultyBoost = (difficulty: string): number => {
  const normalized = difficulty.trim().toLowerCase();
  if (normalized === "hard") {
    return 0.45;
  }
  if (normalized === "medium") {
    return 0.2;
  }
  return 0;
};

const buildReason = (recommendation: FocusRecommendation): string => {
  const failurePct = Math.round(recommendation.signals.failureRate * 100);
  const avgScoreText = recommendation.signals.avgScore === null ? "n/a" : recommendation.signals.avgScore.toFixed(2);

  return [
    `weight=${recommendation.signals.weight.toFixed(2)}`,
    `failureRate=${failurePct}%`,
    `staleness=${Math.round(recommendation.signals.stalenessDays)}d`,
    `avgScore=${avgScoreText}`,
  ].join(", ");
};

export class FocusRecommendationService {
  constructor(
    private readonly prisma: any,
    private readonly openRouter: OpenRouter | null,
    private readonly config: IntelligenceConfig,
  ) {}

  async recommend(limit: number): Promise<FocusRecommendationResult> {
    const lookbackDays = this.config.INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS;
    const since = new Date(Date.now() - lookbackDays * DAY_MS);
    const topK = Math.max(1, Math.min(limit, 50));

    const weights = (await this.prisma.intelligenceWeight.findMany({
      orderBy: { weight: "desc" },
      take: this.config.INTELLIGENCE_MAX_CANDIDATES,
      include: { Question: true },
    })) as Array<{
      questionSlug: string;
      weight: number;
      lastPromptAt: Date | null;
      lastResponseAt: Date | null;
      Question: { title: string; difficulty: string } | null;
    }>;

    if (weights.length === 0) {
      return {
        generatedAt: new Date().toISOString(),
        lookbackDays,
        recommendations: [],
        narrative: "No intelligence weights found yet. Trigger a few prompts first.",
      };
    }

    const slugs = [...new Set(weights.map((item) => item.questionSlug))];

    const submissions = (await this.prisma.submission.findMany({
      where: {
        titleSlug: { in: slugs },
        createdAt: { gte: since },
      },
      select: {
        titleSlug: true,
        status: true,
      },
    })) as Array<{ titleSlug: string | null; status: string }>;

    const promptEvents = (await this.prisma.intelligencePromptEvent.findMany({
      where: {
        questionSlug: { in: slugs },
        selectedAt: { gte: since },
      },
      select: {
        questionSlug: true,
        responseScore: true,
      },
    })) as Array<{ questionSlug: string; responseScore: number | null }>;

    const submissionAgg = new Map<string, { total: number; failed: number }>();
    for (const submission of submissions) {
      if (!submission.titleSlug) {
        continue;
      }
      const current = submissionAgg.get(submission.titleSlug) ?? { total: 0, failed: 0 };
      current.total += 1;
      if (isFailedStatus(submission.status)) {
        current.failed += 1;
      }
      submissionAgg.set(submission.titleSlug, current);
    }

    const promptAgg = new Map<string, { count: number; scoreSum: number; scoreCount: number }>();
    for (const event of promptEvents) {
      const current = promptAgg.get(event.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };
      current.count += 1;
      if (typeof event.responseScore === "number") {
        current.scoreSum += event.responseScore;
        current.scoreCount += 1;
      }
      promptAgg.set(event.questionSlug, current);
    }

    const recommendations = weights
      .map<FocusRecommendation>((item) => {
        const submissionStats = submissionAgg.get(item.questionSlug) ?? { total: 0, failed: 0 };
        const promptStats = promptAgg.get(item.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };

        const failureRate = submissionStats.total > 0 ? submissionStats.failed / submissionStats.total : 0;
        const stalenessDays = daysSince(item.lastResponseAt ?? item.lastPromptAt);
        const avgScore = promptStats.scoreCount > 0 ? promptStats.scoreSum / promptStats.scoreCount : null;

        const scoreFromWeight = normalizedWeightSignal(item.weight, this.config.INTELLIGENCE_MAX_WEIGHT) * 1.8;
        const scoreFromFailure = failureRate * 1.8;
        const scoreFromStaleness = clamp(stalenessDays / lookbackDays, 0, 2) * 1.1;
        const scoreFromDifficulty = difficultyBoost(item.Question?.difficulty ?? "");
        const scoreFromLowAverage = avgScore === null ? 0.25 : clamp((3.2 - avgScore) / 3.2, 0, 1) * 0.8;

        const priority = round(scoreFromWeight + scoreFromFailure + scoreFromStaleness + scoreFromDifficulty + scoreFromLowAverage, 4);

        const recommendation: FocusRecommendation = {
          questionSlug: item.questionSlug,
          title: item.Question?.title ?? item.questionSlug,
          difficulty: item.Question?.difficulty ?? "Unknown",
          priority,
          signals: {
            weight: round(item.weight, 3),
            failureRate: round(failureRate, 3),
            stalenessDays: round(stalenessDays, 1),
            promptCount: promptStats.count,
            avgScore: avgScore === null ? null : round(avgScore, 3),
          },
          reason: "",
        };
        recommendation.reason = buildReason(recommendation);

        return recommendation;
      })
      .sort((a, b) => b.priority - a.priority)
      .slice(0, topK);

    const narrative = await this.buildNarrative(recommendations);

    return {
      generatedAt: new Date().toISOString(),
      lookbackDays,
      recommendations,
      narrative,
    };
  }

  private async buildNarrative(recommendations: FocusRecommendation[]): Promise<string> {
    if (recommendations.length === 0) {
      return "No focus recommendations available right now.";
    }

    if (!this.openRouter) {
      return `Focus next: ${recommendations.map((item) => item.questionSlug).join(", ")}.`;
    }

    try {
      logger.info(
        {
          model: this.config.MODEL,
          recommendationCount: recommendations.length,
        },
        "requesting narrative",
      );

      const response = await this.openRouter.chat.send({
        chatRequest: {
          model: this.config.MODEL,
          temperature: 0.3,
          messages: [
            {
              role: "system",
              content: "You generate concise LeetCode study plans. Keep output under 120 words.",
            },
            {
              role: "user",
              content: JSON.stringify({
                topRecommendations: recommendations,
                ask: "Summarize why these should be the current focus and suggest a short execution order.",
              }),
            },
          ],
        },
      });

      const content = response.choices?.[0]?.message?.content?.trim();
      if (!content) {
        logger.warn("OpenRouter narrative response was empty, using fallback summary");
        return `Focus next: ${recommendations.map((item) => item.questionSlug).join(", ")}.`;
      }
      return content;
    } catch (error) {
      logger.warn({ err: error }, "Recommendation narrative fallback used");
      return `Focus next: ${recommendations.map((item) => item.questionSlug).join(", ")}.`;
    }
  }
}
