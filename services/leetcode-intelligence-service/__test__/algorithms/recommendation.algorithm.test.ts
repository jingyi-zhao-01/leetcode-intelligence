import assert from "node:assert/strict";
import { describe, it, vi } from "vitest";

import {
  HeuristicFocusRecommendationAlgorithm,
  PlaceholderFocusRecommendationAlgorithm,
  type RecommendationAlgorithmInput,
} from "../../src/core/recommendation/algorithm.ts";
import type { WeightCalculator } from "../../src/core/shared/weight.ts";
import type { FocusRecommendation } from "../../src/core/types.ts";

const createInput = (): RecommendationAlgorithmInput => ({
  lookbackDays: 30,
  topK: 2,
  maxWeight: 5,
  weights: [
    {
      questionSlug: "medium-retry",
      weight: 2,
      lastPromptAt: new Date(Date.now() - 10 * 24 * 60 * 60 * 1000),
      lastResponseAt: new Date(Date.now() - 9 * 24 * 60 * 60 * 1000),
      Question: { title: "Medium Retry", difficulty: "Medium" },
    },
    {
      questionSlug: "easy-fresh",
      weight: 1,
      lastPromptAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000),
      lastResponseAt: new Date(),
      Question: { title: "Easy Fresh", difficulty: "Easy" },
    },
  ],
  submissionAgg: new Map([
    [
      "medium-retry",
      {
        total: 3,
        failed: 2,
        recentFailureStreak: 2,
        lastSubmittedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000),
      },
    ],
    [
      "easy-fresh",
      {
        total: 1,
        failed: 0,
        recentFailureStreak: 0,
        lastSubmittedAt: new Date(),
      },
    ],
  ]),
  scoringAgg: new Map([
    ["medium-retry", { count: 2, scoreSum: 4, scoreCount: 2 }],
    ["easy-fresh", { count: 1, scoreSum: 4, scoreCount: 1 }],
  ]),
});

describe("algorithms/recommendation", () => {
  it("HeuristicFocusRecommendationAlgorithm can use a mocked weight policy", () => {
    const normalizedSignal = vi.fn<WeightCalculator["normalizedSignal"]>().mockImplementation((weight) =>
      weight >= 2 ? 1 : 0.1
    );
    const weightCalculator: WeightCalculator = {
      defaultWeight: 1,
      minSelectionWeight: 0.01,
      clamp: (value, min, max) => Math.max(min, Math.min(max, value)),
      scoreToWeightDelta: () => 0,
      selectionWeight: (weight) => weight ?? 1,
      nextWeightFromScore: (previousWeight) => previousWeight,
      normalizedSignal,
    };

    const algorithm = new HeuristicFocusRecommendationAlgorithm(weightCalculator);
    const recommendations = algorithm.rank(createInput());

    assert.equal(normalizedSignal.mock.calls.length, 2);
    assert.equal(recommendations[0]?.questionSlug, "medium-retry");
    assert.equal(recommendations[0]?.signals.estimatedSolveMinutes, 30);
    assert.match(recommendations[0]?.reason ?? "", /estimatedTime=30m/);
  });

  it("PlaceholderFocusRecommendationAlgorithm can return a mocked result directly", () => {
    const mockedResult: FocusRecommendation[] = [
      {
        questionSlug: "mocked-question",
        title: "Mocked Question",
        difficulty: "Hard",
        priority: 7.7,
        signals: {
          weight: 3,
          failureRate: 0.8,
          stalenessDays: 21,
          promptCount: 4,
          avgScore: 1.8,
          estimatedSolveMinutes: 45,
          recentAttemptCount: 5,
          recentFailureStreak: 3,
          recentSubmissionDays: 1,
        },
        reason: "mocked reason",
      },
    ];
    const rank = vi.fn().mockReturnValue(mockedResult);
    const placeholder = new PlaceholderFocusRecommendationAlgorithm({ rank });

    const result = placeholder.rank(createInput());

    assert.deepEqual(result, mockedResult);
    assert.equal(rank.mock.calls.length, 1);
  });
});
