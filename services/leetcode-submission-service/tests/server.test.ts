import assert from "node:assert/strict";
import { describe, it } from "vitest";

import { Cache } from "../src/cache.ts";
import { parseFailureAnalysis } from "../src/utils/failureAnalysisParser.ts";
import { formatPacificTimestamp, inferIsTestSubmission } from "../src/server.ts";

describe("submission server helpers", () => {
  it("formats timestamps in America/Los_Angeles time", () => {
    const formatted = formatPacificTimestamp(new Date("2026-01-15T18:30:45.000Z"));

    assert.equal(formatted, "2026-01-15 10:30:45 PST");
  });

  it("detects test submissions from leetcode metadata", () => {
    const isTest = inferIsTestSubmission("print('hello')", {
      _: {
        submission: false,
      },
    });

    assert.equal(isTest, true);
  });

  it("prefers persisted lcnvim_is_test when present", () => {
    const isTest = inferIsTestSubmission("print('hello')", {
      lcnvim_is_test: false,
      _: {
        submission: false,
      },
    });

    assert.equal(isTest, false);
  });

  it("serves recent submissions from cache in descending order", () => {
    const cache = new Cache();

    cache.savePending({
      id: "pending-1",
      title_slug: "insert-interval",
      submitted_at: "2026-05-25T21:00:00.000Z",
      submitted_at_pst: "2026-05-25 14:00:00 PDT",
      time_spent_minutes: 12,
      submit_result: "Accepted",
      is_test: false,
    });
    cache.savePending({
      id: "pending-2",
      title_slug: "insert-interval",
      submitted_at: "2026-05-25T21:01:00.000Z",
      submitted_at_pst: "2026-05-25 14:01:00 PDT",
      time_spent_minutes: 15,
      submit_result: "Wrong Answer",
      is_test: true,
    });

    const result = cache.get("insert-interval", 2);
    assert.deepEqual(
      result.map((entry) => entry.id),
      ["pending-2", "pending-1"],
    );
  });

  it("replaces pending ids with persisted ids and avoids duplicate merges", () => {
    const cache = new Cache();
    const cacheKey = cache.savePending({
      id: "pending-1",
      title_slug: "insert-interval",
      submitted_at: "2026-05-25T21:00:00.000Z",
      submitted_at_pst: "2026-05-25 14:00:00 PDT",
      time_spent_minutes: 12,
      submit_result: "Accepted",
      is_test: false,
    });

    cache.markPersisted("insert-interval", cacheKey, "db-1");
    const merged = cache.mergePersisted("insert-interval", [
      {
        id: "db-1",
        title_slug: "insert-interval",
        submitted_at: "2026-05-25T21:00:00.000Z",
        submitted_at_pst: "2026-05-25 14:00:00 PDT",
        time_spent_minutes: 12,
        submit_result: "Accepted",
        is_test: false,
      },
    ]);

    assert.equal(merged.length, 1);
    assert.equal(merged[0]?.id, "db-1");
  });

  it("parses structured failure annotations and filters invalid lines", () => {
    const parsed = parseFailureAnalysis(
      JSON.stringify({
        summary: "第 2 行条件分支少考虑了空输入。",
        annotations: [
          { line: 2, reason: "这里可能越界", severity: "error" },
          { line: 9, reason: "超出编辑器范围", severity: "warn" },
          { line: 2, reason: "需要先判空", severity: "warn" },
        ],
      }),
      4,
    );

    assert.equal(parsed.summary, "第 2 行条件分支少考虑了空输入。");
    assert.deepEqual(parsed.annotations, [
      {
        line: 2,
        reason: "这里可能越界 | 需要先判空",
        severity: "error",
        column: undefined,
      },
    ]);
  });
});
