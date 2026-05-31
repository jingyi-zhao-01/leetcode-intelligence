import type { FocusRecommendation } from "../types.ts";
import { LinearWeightCalculator, clamp, type WeightCalculator } from "../shared/weight.ts";
import {
  buildReason,
  daysSince,
  difficultyBoost,
  estimatedSolveMinutes,
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

export type ScoringAggregate = {
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
  scoringAgg: Map<string, ScoringAggregate>;
};

export interface FocusRecommendationAlgorithm {
  rank(input: RecommendationAlgorithmInput): FocusRecommendation[];
}

// This heuristic ranks each candidate question by summing several capped signals.
// `scoreFromWeight`: boosts questions whose review weight is already high, meaning
// they have accumulated more urgency from the spaced-review logic.
// `scoreFromFailure`: boosts questions with a high historical failure rate.
// `scoreFromStaleness`: boosts questions that have not been reviewed recently.
// `scoreFromDifficulty`: adds a fixed difficulty bias so harder problems surface sooner.
// `estimatedSolveMinutes`: derives a default time budget from difficulty
// (Easy=15m, Medium=30m, Hard=45m) so downstream clients can show expected effort.
// `scoreFromLowAverage`: boosts questions whose past prompt-response scores were weak.
// `scoreFromRecentAttempts`: gives a small boost to questions with repeated recent attempts.
// `scoreFromFailureStreak`: boosts questions where the user is currently failing repeatedly.
// `scoreFromRecentSubmission`: boosts questions that were submitted recently, so the system
// can recommend timely follow-up while the context is still fresh.
// The final `priority` is the rounded sum of those sub-scores, then the algorithm
// sorts descending by priority and returns the top K questions.
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
        const scoringStats = input.scoringAgg.get(item.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };

        const failureRate = submissionStats.total > 0 ? submissionStats.failed / submissionStats.total : 0;
        const stalenessDays = daysSince(item.lastResponseAt ?? item.lastPromptAt);
        const avgScore = scoringStats.scoreCount > 0 ? scoringStats.scoreSum / scoringStats.scoreCount : null;
        const estimatedTimeMinutes = estimatedSolveMinutes(item.Question?.difficulty ?? "");
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
            promptCount: scoringStats.count,
            avgScore: avgScore === null ? null : round(avgScore, 3),
            estimatedSolveMinutes: estimatedTimeMinutes,
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
