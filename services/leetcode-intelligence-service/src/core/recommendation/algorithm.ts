import type { FocusRecommendation } from "../types.ts";
import { LinearWeightCalculator, clamp, type WeightCalculator } from "../shared/weight.ts";
import {
  buildReason,
  daysSince,
  difficultyBoost,
  round,
} from "./util.ts";

export type RecommendationWeightRecord = {
  questionSlug: string;
  weight: number;
  lastPromptAt: Date | null;
  lastResponseAt: Date | null;
  Question: { title: string; difficulty: string } | null;
};

export type SubmissionAggregate = {
  total: number;
  failed: number;
  recentFailureStreak: number;
  lastSubmittedAt: Date | null;
};

export type PromptAggregate = {
  count: number;
  scoreSum: number;
  scoreCount: number;
};

export type RecommendationAlgorithmInput = {
  lookbackDays: number;
  topK: number;
  maxWeight: number;
  weights: RecommendationWeightRecord[];
  submissionAgg: Map<string, SubmissionAggregate>;
  promptAgg: Map<string, PromptAggregate>;
};

export interface FocusRecommendationAlgorithm {
  rank(input: RecommendationAlgorithmInput): FocusRecommendation[];
}

export class HeuristicFocusRecommendationAlgorithm implements FocusRecommendationAlgorithm {
  constructor(private readonly weightCalculator: WeightCalculator = new LinearWeightCalculator()) {}

  rank(input: RecommendationAlgorithmInput): FocusRecommendation[] {
    return input.weights
      .map<FocusRecommendation>((item) => {
        const submissionStats = input.submissionAgg.get(item.questionSlug) ?? {
          total: 0,
          failed: 0,
          recentFailureStreak: 0,
          lastSubmittedAt: null,
        };
        const promptStats = input.promptAgg.get(item.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };

        const failureRate = submissionStats.total > 0 ? submissionStats.failed / submissionStats.total : 0;
        const stalenessDays = daysSince(item.lastResponseAt ?? item.lastPromptAt);
        const avgScore = promptStats.scoreCount > 0 ? promptStats.scoreSum / promptStats.scoreCount : null;
        const recentSubmissionDays = submissionStats.lastSubmittedAt
          ? daysSince(submissionStats.lastSubmittedAt)
          : null;

        const scoreFromWeight = this.weightCalculator.normalizedSignal(item.weight, input.maxWeight) * 1.8;
        const scoreFromFailure = failureRate * 1.8;
        const scoreFromStaleness = clamp(stalenessDays / input.lookbackDays, 0, 2) * 1.1;
        const scoreFromDifficulty = difficultyBoost(item.Question?.difficulty ?? "");
        const scoreFromLowAverage = avgScore === null ? 0.25 : clamp((3.2 - avgScore) / 3.2, 0, 1) * 0.8;
        const scoreFromRecentAttempts = clamp((submissionStats.total - 1) / 4, 0, 1) * 0.45;
        const scoreFromFailureStreak = clamp(submissionStats.recentFailureStreak / 3, 0, 1) * 0.9;
        const scoreFromRecentSubmission = recentSubmissionDays === null
          ? 0
          : clamp(1 - recentSubmissionDays / Math.max(input.lookbackDays / 2, 1), 0, 1) * 0.6;

        const priority = round(
          scoreFromWeight
            + scoreFromFailure
            + scoreFromStaleness
            + scoreFromDifficulty
            + scoreFromLowAverage
            + scoreFromRecentAttempts
            + scoreFromFailureStreak
            + scoreFromRecentSubmission,
          4,
        );

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
            recentAttemptCount: submissionStats.total,
            recentFailureStreak: submissionStats.recentFailureStreak,
            recentSubmissionDays: recentSubmissionDays === null ? null : round(recentSubmissionDays, 1),
          },
          reason: "",
        };
        recommendation.reason = buildReason(recommendation);

        return recommendation;
      })
      .sort((a, b) => b.priority - a.priority)
      .slice(0, input.topK);
  }
}

// Placeholder for future experimentation with alternative ranking logic
// such as topic-balancing, spaced repetition, or model-driven prioritization.
export class PlaceholderFocusRecommendationAlgorithm implements FocusRecommendationAlgorithm {
  constructor(private readonly fallback = new HeuristicFocusRecommendationAlgorithm()) {}

  rank(input: RecommendationAlgorithmInput): FocusRecommendation[] {
    return this.fallback.rank(input);
  }
}
