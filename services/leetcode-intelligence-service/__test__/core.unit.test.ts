import assert from 'node:assert/strict';
import { describe, it } from 'vitest';

import { loadIntelligenceConfig } from '../src/core/env.ts';
import { PromptCandidatePipeline } from '../src/core/scoring/pipeline.ts';
import { FallbackScoringAlgorithm, ReplyScorer } from '../src/core/scoring/scoring.ts';
import {
  HeuristicFocusRecommendationAlgorithm,
  PlaceholderFocusRecommendationAlgorithm,
} from '../src/core/recommendation/algorithm.ts';
import { RecommendationAggregationBuilder } from '../src/core/recommendation/aggregation.ts';
import {
  FallbackRecommendationNarrativeGenerator,
  PlaceholderRecommendationNarrativeGenerator,
} from '../src/core/recommendation/narrative.ts';
import {
  DEFAULT_QUESTION_WEIGHT,
  LinearWeightCalculator,
  MIN_SELECTION_WEIGHT,
  PlaceholderWeightCalculator,
  clamp,
  nextWeightFromScore,
  normalizedWeightSignal,
  scoreToWeightDelta,
  selectionWeight,
} from '../src/core/shared/weight.ts';
import type { PromptCooldownRule } from '../src/core/types.ts';

const defaultCooldownRules: PromptCooldownRule[] = [{ name: 'default', cooldownHours: 24 }];

describe('core/shared/weight', () => {
  it('exports the expected default weight constants', () => {
    assert.equal(DEFAULT_QUESTION_WEIGHT, 1);
    assert.equal(MIN_SELECTION_WEIGHT, 0.01);
  });

  it('clamp bounds values into the requested range', () => {
    assert.equal(clamp(-1, 0, 5), 0);
    assert.equal(clamp(3, 0, 5), 3);
    assert.equal(clamp(8, 0, 5), 5);
  });

  it('scoreToWeightDelta raises weak scores and lowers strong scores', () => {
    assert.equal(scoreToWeightDelta(1), 0.5);
    assert.equal(scoreToWeightDelta(3), 0);
    assert.equal(scoreToWeightDelta(5), -0.5);
  });

  it('selectionWeight falls back to defaults and enforces the minimum sampling floor', () => {
    assert.equal(selectionWeight(undefined), DEFAULT_QUESTION_WEIGHT);
    assert.equal(selectionWeight(null), DEFAULT_QUESTION_WEIGHT);
    assert.equal(selectionWeight(0), MIN_SELECTION_WEIGHT);
    assert.equal(selectionWeight(0.005), MIN_SELECTION_WEIGHT);
    assert.equal(selectionWeight(2.25), 2.25);
  });

  it('nextWeightFromScore respects min and max bounds', () => {
    const config = {
      INTELLIGENCE_MIN_WEIGHT: 0.25,
      INTELLIGENCE_MAX_WEIGHT: 5,
    };

    assert.equal(nextWeightFromScore(1, 1, config), 1.5);
    assert.equal(nextWeightFromScore(1, 5, config), 0.5);
    assert.equal(nextWeightFromScore(0.3, 5, config), 0.25);
    assert.equal(nextWeightFromScore(4.9, 1, config), 5);
  });

  it('normalizedWeightSignal compresses weight into the recommendation signal range', () => {
    assert.equal(normalizedWeightSignal(0, 5), 0);
    assert.equal(normalizedWeightSignal(2.5, 5), 0.5);
    assert.equal(normalizedWeightSignal(6, 5), 1.2);
  });

  it('LinearWeightCalculator exposes the default shared weight policy', () => {
    const calculator = new LinearWeightCalculator();

    assert.equal(calculator.defaultWeight, DEFAULT_QUESTION_WEIGHT);
    assert.equal(calculator.minSelectionWeight, MIN_SELECTION_WEIGHT);
    assert.equal(calculator.scoreToWeightDelta(2), 0.25);
    assert.equal(calculator.selectionWeight(0), MIN_SELECTION_WEIGHT);
    assert.equal(
      calculator.nextWeightFromScore(1, 1, {
        INTELLIGENCE_MIN_WEIGHT: 0.25,
        INTELLIGENCE_MAX_WEIGHT: 5,
      }),
      1.5,
    );
    assert.equal(calculator.normalizedSignal(2.5, 5), 0.5);
  });

  it('PlaceholderWeightCalculator delegates to its fallback policy', () => {
    const calculator = new PlaceholderWeightCalculator({
      defaultWeight: 4,
      minSelectionWeight: 0.2,
      clamp: (value, min, max) => Math.max(min + 1, Math.min(max - 1, value)),
      scoreToWeightDelta: () => 0.75,
      selectionWeight: () => 8,
      nextWeightFromScore: () => 9,
      normalizedSignal: () => 0.33,
    });

    assert.equal(calculator.defaultWeight, 4);
    assert.equal(calculator.minSelectionWeight, 0.2);
    assert.equal(calculator.clamp(10, 0, 5), 4);
    assert.equal(calculator.scoreToWeightDelta(5), 0.75);
    assert.equal(calculator.selectionWeight(null), 8);
    assert.equal(
      calculator.nextWeightFromScore(1, 5, {
        INTELLIGENCE_MIN_WEIGHT: 0.25,
        INTELLIGENCE_MAX_WEIGHT: 5,
      }),
      9,
    );
    assert.equal(calculator.normalizedSignal(1, 5), 0.33);
  });
});

describe('core/recommendation', () => {
  it('RecommendationAggregationBuilder groups submission and prompt signals', () => {
    const builder = new RecommendationAggregationBuilder();

    const submissionAgg = builder.buildSubmissionAggregate([
      { titleSlug: 'two-sum', status: 'Wrong Answer', createdAt: new Date('2026-05-04T00:00:00.000Z') },
      { titleSlug: 'two-sum', status: 'Accepted', createdAt: new Date('2026-05-03T00:00:00.000Z') },
      { titleSlug: 'three-sum', status: 'Runtime Error', createdAt: new Date('2026-05-02T00:00:00.000Z') },
      { titleSlug: null, status: 'Accepted', createdAt: new Date('2026-05-01T00:00:00.000Z') },
    ]);
    const scoringAgg = builder.buildScoringAggregate([
      { questionSlug: 'two-sum', responseScore: 2 },
      { questionSlug: 'two-sum', responseScore: 4 },
      { questionSlug: 'three-sum', responseScore: null },
    ]);

    assert.deepEqual(submissionAgg.get('two-sum'), {
      total: 2,
      failed: 1,
      recentFailureStreak: 1,
      lastSubmittedAt: new Date('2026-05-04T00:00:00.000Z'),
    });
    assert.deepEqual(submissionAgg.get('three-sum'), {
      total: 1,
      failed: 1,
      recentFailureStreak: 1,
      lastSubmittedAt: new Date('2026-05-02T00:00:00.000Z'),
    });
    assert.deepEqual(scoringAgg.get('two-sum'), { count: 2, scoreSum: 6, scoreCount: 2 });
    assert.deepEqual(scoringAgg.get('three-sum'), { count: 1, scoreSum: 0, scoreCount: 0 });
  });

  it('HeuristicFocusRecommendationAlgorithm ranks weaker and staler questions higher', () => {
    const algorithm = new HeuristicFocusRecommendationAlgorithm();

    const recommendations = algorithm.rank({
      lookbackDays: 30,
      topK: 2,
      maxWeight: 5,
      weights: [
        {
          questionSlug: 'hard-old',
          weight: 4,
          lastPromptAt: new Date(Date.now() - 20 * 24 * 60 * 60 * 1000),
          lastResponseAt: null,
          Question: { title: 'Hard Old', difficulty: 'Hard' },
        },
        {
          questionSlug: 'easy-fresh',
          weight: 1,
          lastPromptAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000),
          lastResponseAt: new Date(),
          Question: { title: 'Easy Fresh', difficulty: 'Easy' },
        },
      ],
      submissionAgg: new Map([
        [
          'hard-old',
          {
            total: 4,
            failed: 3,
            recentFailureStreak: 2,
            lastSubmittedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000),
          },
        ],
        [
          'easy-fresh',
          {
            total: 3,
            failed: 0,
            recentFailureStreak: 0,
            lastSubmittedAt: new Date(),
          },
        ],
      ]),
      scoringAgg: new Map([
        ['hard-old', { count: 2, scoreSum: 4, scoreCount: 2 }],
        ['easy-fresh', { count: 2, scoreSum: 8, scoreCount: 2 }],
      ]),
    });

    assert.equal(recommendations.length, 2);
    assert.equal(recommendations[0]?.questionSlug, 'hard-old');
    assert.equal(recommendations[1]?.questionSlug, 'easy-fresh');
    assert.match(recommendations[0]?.reason ?? '', /failureRate=75%/);
    assert.match(recommendations[0]?.reason ?? '', /estimatedTime=45m/);
    assert.equal(recommendations[0]?.signals.estimatedSolveMinutes, 45);
    assert.equal(recommendations[1]?.signals.estimatedSolveMinutes, 15);
    assert.equal(recommendations[0]?.signals.recentFailureStreak, 2);
    assert.equal(recommendations[0]?.signals.recentAttemptCount, 4);
  });

  it('PlaceholderFocusRecommendationAlgorithm delegates to its fallback algorithm', () => {
    const placeholder = new PlaceholderFocusRecommendationAlgorithm({
      rank: () => [
        {
          questionSlug: 'delegated',
          title: 'Delegated',
          difficulty: 'Medium',
          priority: 9.9,
          signals: {
            weight: 1,
            failureRate: 0.5,
            stalenessDays: 7,
            promptCount: 3,
            avgScore: 2.5,
            estimatedSolveMinutes: 30,
            recentAttemptCount: 2,
            recentFailureStreak: 1,
            recentSubmissionDays: 1,
          },
          reason: 'delegated',
        },
      ],
    });

    const recommendations = placeholder.rank({
      lookbackDays: 30,
      topK: 1,
      maxWeight: 5,
      weights: [],
      submissionAgg: new Map(),
      scoringAgg: new Map(),
    });

    assert.deepEqual(
      recommendations.map((item) => item.questionSlug),
      ['delegated'],
    );
  });

  it('FallbackRecommendationNarrativeGenerator summarizes recommendations without OpenRouter', async () => {
    const generator = new FallbackRecommendationNarrativeGenerator();

    const narrative = await generator.generate([
      {
        questionSlug: 'two-sum',
        title: 'Two Sum',
        difficulty: 'Easy',
        priority: 1.2,
        signals: {
          weight: 1,
          failureRate: 0.2,
          stalenessDays: 5,
          promptCount: 2,
          avgScore: 3,
          estimatedSolveMinutes: 15,
          recentAttemptCount: 2,
          recentFailureStreak: 1,
          recentSubmissionDays: 2,
        },
        reason: 'weight=1.00',
      },
      {
        questionSlug: 'three-sum',
        title: 'Three Sum',
        difficulty: 'Medium',
        priority: 1.8,
        signals: {
          weight: 2,
          failureRate: 0.5,
          stalenessDays: 9,
          promptCount: 3,
          avgScore: 2.5,
          estimatedSolveMinutes: 30,
          recentAttemptCount: 4,
          recentFailureStreak: 2,
          recentSubmissionDays: 1,
        },
        reason: 'weight=2.00',
      },
    ]);

    assert.equal(narrative, 'Focus next: two-sum, three-sum.');
  });

  it('PlaceholderRecommendationNarrativeGenerator delegates to its fallback generator', async () => {
    const generator = new PlaceholderRecommendationNarrativeGenerator({
      generate: async () => 'delegated narrative',
    });

    const narrative = await generator.generate([]);

    assert.equal(narrative, 'delegated narrative');
  });
});

describe('core/scoring/pipeline', () => {
  it('dedupes candidates at the question level by keeping the latest submission entry', () => {
    const now = new Date('2026-05-25T20:00:00.000Z');
    const pipeline = new PromptCandidatePipeline(
      [
        {
          submission: {
            id: 'newer',
            titleSlug: 'insert-interval',
            content: 'newer',
            status: 'Accepted',
            createdAt: new Date('2026-05-25T10:00:00.000Z'),
          },
          question: {
            title: 'Insert Interval',
            titleSlug: 'insert-interval',
            difficulty: 'Medium',
            content: null,
            topicTags: [],
            freqBar: null,
          },
          weight: 1,
          lastPromptAt: null,
        },
        {
          submission: {
            id: 'older',
            titleSlug: 'insert-interval',
            content: 'older',
            status: 'Wrong Answer',
            createdAt: new Date('2026-05-24T10:00:00.000Z'),
          },
          question: {
            title: 'Insert Interval',
            titleSlug: 'insert-interval',
            difficulty: 'Medium',
            content: null,
            topicTags: [],
            freqBar: null,
          },
          weight: 2,
          lastPromptAt: null,
        },
      ],
      now,
    );

    const candidates = pipeline.dedupeByQuestion().toArray();

    assert.equal(candidates.length, 1);
    assert.equal(candidates[0]?.submission.id, 'newer');
  });

  it('drops recently prompted questions out of the prompt pipeline according to cooldown rules', () => {
    const now = new Date('2026-05-25T20:00:00.000Z');
    const pipeline = new PromptCandidatePipeline(
      [
        {
          submission: {
            id: 'accepted-recent',
            titleSlug: 'insert-interval',
            content: 'accepted',
            status: 'Accepted',
            createdAt: new Date('2026-05-25T10:00:00.000Z'),
          },
          question: {
            title: 'Insert Interval',
            titleSlug: 'insert-interval',
            difficulty: 'Medium',
            content: null,
            topicTags: [],
            freqBar: null,
          },
          weight: 1,
          lastPromptAt: new Date('2026-05-25T12:00:00.000Z'),
        },
        {
          submission: {
            id: 'eligible',
            titleSlug: 'merge-intervals',
            content: 'eligible',
            status: 'Wrong Answer',
            createdAt: new Date('2026-05-24T10:00:00.000Z'),
          },
          question: {
            title: 'Merge Intervals',
            titleSlug: 'merge-intervals',
            difficulty: 'Medium',
            content: null,
            topicTags: [],
            freqBar: null,
          },
          weight: 2,
          lastPromptAt: new Date('2026-05-24T10:00:00.000Z'),
        },
      ],
      now,
    );

    const candidates = pipeline
      .dropPromptedQuestions([
        { name: 'accepted-cooldown', cooldownHours: 12, statuses: ['Accepted'] },
        ...defaultCooldownRules,
      ])
      .toArray();

    assert.deepEqual(
      candidates.map((candidate) => candidate.question.titleSlug),
      ['merge-intervals'],
    );
  });
});

describe('core/env', () => {
  it('loads defaults for optional intelligence settings', () => {
    const originalEnv = process.env;
    process.env = {
      DATABASE_URL: 'postgres://example',
    };

    try {
      const config = loadIntelligenceConfig();
      assert.equal(config.MODEL, 'openai/gpt-4o-mini');
      assert.equal(config.INTELLIGENCE_PORT, 8030);
      assert.equal(config.INTELLIGENCE_HOST, '0.0.0.0');
      assert.equal(config.INTELLIGENCE_PROMPT_CRON, '0 9 * * *');
      assert.equal(config.INTELLIGENCE_RECOMMEND_CRON, '0 20 * * *');
      assert.equal(config.INTELLIGENCE_RECOMMEND_TOP_K, 10);
      assert.equal(config.INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS, 30);
      assert.equal(config.INTELLIGENCE_MAX_CANDIDATES, 500);
      assert.equal(config.INTELLIGENCE_SELECTION_WINDOW, 200);
      assert.equal(config.INTELLIGENCE_MIN_WEIGHT, 0.25);
      assert.equal(config.INTELLIGENCE_MAX_WEIGHT, 5);
      assert.deepEqual(config.INTELLIGENCE_PROMPT_COOLDOWN_RULES, defaultCooldownRules);
    } finally {
      process.env = originalEnv;
    }
  });

  it('preserves explicit prompt cron overrides', () => {
    const originalEnv = process.env;
    process.env = {
      DATABASE_URL: 'postgres://example',
      INTELLIGENCE_PROMPT_CRON: '*/15 * * * *',
      INTELLIGENCE_PROMPT_COOLDOWN_RULES: JSON.stringify([
        { name: 'accepted', cooldownHours: 48, statuses: ['Accepted'] },
        { name: 'default', cooldownHours: 12 },
      ]),
    };

    try {
      const config = loadIntelligenceConfig();
      assert.equal(config.INTELLIGENCE_PROMPT_CRON, '*/15 * * * *');
      assert.deepEqual(config.INTELLIGENCE_PROMPT_COOLDOWN_RULES, [
        { name: 'accepted', cooldownHours: 48, statuses: ['Accepted'] },
        { name: 'default', cooldownHours: 12 },
      ]);
    } finally {
      process.env = originalEnv;
    }
  });
});

describe('core/scoring/scoring', () => {
  it('FallbackScoringAlgorithm scores empty replies conservatively', async () => {
    const scorer = new FallbackScoringAlgorithm();

    const result = await scorer.score({
      questionSlug: 'two-sum',
      promptText: 'Solve it',
      submission: {
        id: 'submission-1',
        titleSlug: 'two-sum',
        content: 'old answer',
        status: 'Accepted',
        createdAt: new Date('2026-01-01T00:00:00.000Z'),
      },
      rawReply: '   ',
    });

    assert.equal(result.score, 2);
    assert.equal(result.approachSummary, 'No reply provided.');
    assert.match(result.complexityNotes, /Fallback scorer used/);
    assert.deepEqual(result.tags, ['fallback', 'cli-e2e']);
  });

  it('FallbackScoringAlgorithm upgrades longer replies', async () => {
    const scorer = new FallbackScoringAlgorithm();

    const mediumReply = await scorer.score({
      questionSlug: 'two-sum',
      promptText: 'Solve it',
      submission: {
        id: 'submission-1',
        titleSlug: 'two-sum',
        content: 'old answer',
        status: 'Accepted',
        createdAt: new Date('2026-01-01T00:00:00.000Z'),
      },
      rawReply: 'x'.repeat(40),
    });

    const longReply = await scorer.score({
      questionSlug: 'two-sum',
      promptText: 'Solve it',
      submission: {
        id: 'submission-1',
        titleSlug: 'two-sum',
        content: 'old answer',
        status: 'Accepted',
        createdAt: new Date('2026-01-01T00:00:00.000Z'),
      },
      rawReply: 'x'.repeat(120),
    });

    assert.equal(mediumReply.score, 3);
    assert.equal(longReply.score, 4);
  });

  it('ReplyScorer falls back when the primary scorer throws', async () => {
    const primary = {
      score: async () => {
        throw new Error('OpenRouter down');
      },
    };
    const fallback = new FallbackScoringAlgorithm();
    const scorer = new ReplyScorer(primary, fallback);

    const result = await scorer.score({
      questionSlug: 'two-sum',
      promptText: 'Solve it',
      submission: {
        id: 'submission-1',
        titleSlug: 'two-sum',
        content: 'old answer',
        status: 'Accepted',
        createdAt: new Date('2026-01-01T00:00:00.000Z'),
      },
      rawReply: 'x'.repeat(50),
    });

    assert.equal(result.score, 3);
    assert.deepEqual(result.tags, ['fallback', 'cli-e2e']);
  });
});
