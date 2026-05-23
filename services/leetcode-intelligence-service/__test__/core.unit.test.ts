import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { loadIntelligenceConfig } from "../src/core/env.ts";
import { FallbackScoringAlgorithm, ReplyScorer } from "../src/core/evaluation/scoring.ts";
import {
  DEFAULT_QUESTION_WEIGHT,
  MIN_SELECTION_WEIGHT,
  clamp,
  nextWeightFromScore,
  normalizedWeightSignal,
  scoreToWeightDelta,
  selectionWeight,
} from "../src/core/shared/weight.ts";

describe("core/shared/weight", () => {
  it("exports the expected default weight constants", () => {
    assert.equal(DEFAULT_QUESTION_WEIGHT, 1);
    assert.equal(MIN_SELECTION_WEIGHT, 0.01);
  });

  it("clamp bounds values into the requested range", () => {
    assert.equal(clamp(-1, 0, 5), 0);
    assert.equal(clamp(3, 0, 5), 3);
    assert.equal(clamp(8, 0, 5), 5);
  });

  it("scoreToWeightDelta raises weak scores and lowers strong scores", () => {
    assert.equal(scoreToWeightDelta(1), 0.5);
    assert.equal(scoreToWeightDelta(3), 0);
    assert.equal(scoreToWeightDelta(5), -0.5);
  });

  it("selectionWeight falls back to defaults and enforces the minimum sampling floor", () => {
    assert.equal(selectionWeight(undefined), DEFAULT_QUESTION_WEIGHT);
    assert.equal(selectionWeight(null), DEFAULT_QUESTION_WEIGHT);
    assert.equal(selectionWeight(0), MIN_SELECTION_WEIGHT);
    assert.equal(selectionWeight(0.005), MIN_SELECTION_WEIGHT);
    assert.equal(selectionWeight(2.25), 2.25);
  });

  it("nextWeightFromScore respects min and max bounds", () => {
    const config = {
      INTELLIGENCE_MIN_WEIGHT: 0.25,
      INTELLIGENCE_MAX_WEIGHT: 5,
    };

    assert.equal(nextWeightFromScore(1, 1, config), 1.5);
    assert.equal(nextWeightFromScore(1, 5, config), 0.5);
    assert.equal(nextWeightFromScore(0.3, 5, config), 0.25);
    assert.equal(nextWeightFromScore(4.9, 1, config), 5);
  });

  it("normalizedWeightSignal compresses weight into the recommendation signal range", () => {
    assert.equal(normalizedWeightSignal(0, 5), 0);
    assert.equal(normalizedWeightSignal(2.5, 5), 0.5);
    assert.equal(normalizedWeightSignal(6, 5), 1.2);
  });
});

describe("core/env", () => {
  it("loads defaults for optional intelligence settings", () => {
    const originalEnv = process.env;
    process.env = {
      DATABASE_URL: "postgres://example",
    };

    try {
      const config = loadIntelligenceConfig();
      assert.equal(config.MODEL, "openai/gpt-4o-mini");
      assert.equal(config.INTELLIGENCE_PORT, 8030);
      assert.equal(config.INTELLIGENCE_HOST, "0.0.0.0");
      assert.equal(config.INTELLIGENCE_PROMPT_CRON, "0 9 * * *");
      assert.equal(config.INTELLIGENCE_RECOMMEND_CRON, "0 20 * * *");
      assert.equal(config.INTELLIGENCE_RECOMMEND_TOP_K, 5);
      assert.equal(config.INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS, 30);
      assert.equal(config.INTELLIGENCE_MAX_CANDIDATES, 500);
      assert.equal(config.INTELLIGENCE_SELECTION_WINDOW, 200);
      assert.equal(config.INTELLIGENCE_MIN_WEIGHT, 0.25);
      assert.equal(config.INTELLIGENCE_MAX_WEIGHT, 5);
    } finally {
      process.env = originalEnv;
    }
  });

  it("preserves explicit prompt cron overrides", () => {
    const originalEnv = process.env;
    process.env = {
      DATABASE_URL: "postgres://example",
      INTELLIGENCE_PROMPT_CRON: "*/15 * * * *",
    };

    try {
      const config = loadIntelligenceConfig();
      assert.equal(config.INTELLIGENCE_PROMPT_CRON, "*/15 * * * *");
    } finally {
      process.env = originalEnv;
    }
  });
});

describe("core/evaluation/scoring", () => {
  it("FallbackScoringAlgorithm scores empty replies conservatively", async () => {
    const scorer = new FallbackScoringAlgorithm();

    const result = await scorer.score({
      questionSlug: "two-sum",
      promptText: "Solve it",
      submission: {
        id: "submission-1",
        titleSlug: "two-sum",
        content: "old answer",
        status: "Accepted",
        createdAt: new Date("2026-01-01T00:00:00.000Z"),
      },
      rawReply: "   ",
    });

    assert.equal(result.score, 2);
    assert.equal(result.approachSummary, "No reply provided.");
    assert.match(result.complexityNotes, /Fallback scorer used/);
    assert.deepEqual(result.tags, ["fallback", "cli-e2e"]);
  });

  it("FallbackScoringAlgorithm upgrades longer replies", async () => {
    const scorer = new FallbackScoringAlgorithm();

    const mediumReply = await scorer.score({
      questionSlug: "two-sum",
      promptText: "Solve it",
      submission: {
        id: "submission-1",
        titleSlug: "two-sum",
        content: "old answer",
        status: "Accepted",
        createdAt: new Date("2026-01-01T00:00:00.000Z"),
      },
      rawReply: "x".repeat(40),
    });

    const longReply = await scorer.score({
      questionSlug: "two-sum",
      promptText: "Solve it",
      submission: {
        id: "submission-1",
        titleSlug: "two-sum",
        content: "old answer",
        status: "Accepted",
        createdAt: new Date("2026-01-01T00:00:00.000Z"),
      },
      rawReply: "x".repeat(120),
    });

    assert.equal(mediumReply.score, 3);
    assert.equal(longReply.score, 4);
  });

  it("ReplyScorer falls back when the primary scorer throws", async () => {
    const primary = {
      score: async () => {
        throw new Error("OpenRouter down");
      },
    };
    const fallback = new FallbackScoringAlgorithm();
    const scorer = new ReplyScorer(primary, fallback);

    const result = await scorer.score({
      questionSlug: "two-sum",
      promptText: "Solve it",
      submission: {
        id: "submission-1",
        titleSlug: "two-sum",
        content: "old answer",
        status: "Accepted",
        createdAt: new Date("2026-01-01T00:00:00.000Z"),
      },
      rawReply: "x".repeat(50),
    });

    assert.equal(result.score, 3);
    assert.deepEqual(result.tags, ["fallback", "cli-e2e"]);
  });
});
