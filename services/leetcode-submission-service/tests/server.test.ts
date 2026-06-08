import assert from "node:assert/strict";
import { describe, it } from "vitest";

import { sanitizeCompanionMessages } from "../src/core/companionChat.ts";
import { Cache } from "../src/cache.ts";
import { ActiveSessionScopeManager, extractCompanionSessionContext, renderActiveSessionScope } from "../src/session/index.ts";
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

  it("sanitizes companion messages and drops invalid entries", () => {
    const messages = sanitizeCompanionMessages([
      { role: "system", content: "hidden prompt" },
      { role: "user", content: " explain this " },
      { role: "assistant", content: "previous answer" },
      { role: "tool", content: "unsupported" },
      { role: "user", content: "   " },
      null,
    ]);

    assert.deepEqual(messages, [
      { role: "system", content: "hidden prompt" },
      { role: "user", content: "explain this" },
      { role: "assistant", content: "previous answer" },
    ]);
  });

  it("extracts leetcode companion context from the hidden problem message", () => {
    const context = extractCompanionSessionContext([
      {
        role: "user",
        content: [
          "# LeetCode Problem Context",
          "",
          "- Title: Two Sum",
          "- Title Slug: two-sum",
          "- Difficulty: Easy",
          "- Language: python3",
          "",
          "## Problem Description",
          "Find two numbers.",
          "",
          "## Active Testcase",
          "```text",
          "[2,7,11,15]",
          "```",
          "",
          "## Current Code",
          "```python3",
          "class Solution:",
          "    pass",
          "```",
        ].join("\n"),
      },
    ]);

    assert.deepEqual(context, {
      title: "Two Sum",
      titleSlug: "two-sum",
      difficulty: "Easy",
      lang: "python3",
      description: "Find two numbers.",
      testcase: "[2,7,11,15]",
      code: "class Solution:\n    pass",
    });
  });

  it("binds failure analysis and companion context into the same active session scope", () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate("two-sum");
    manager.recordCompanionContext({
      title: "Two Sum",
      titleSlug: "two-sum",
      difficulty: "Easy",
      lang: "python3",
      description: "Find two numbers.",
      testcase: "[2,7,11,15]",
      code: "class Solution:\n    pass",
    });
    manager.recordCompanionMessages("two-sum", [
      { role: "user", content: "为什么我的哈希表做法不对？" },
    ]);
    manager.appendCompanionReply("two-sum", "因为你先插入再查找，会错过配对。");
    manager.recordFailureAnalysis(
      {
        titleSlug: "two-sum",
        title: "Two Sum",
        questionContent: "Find two numbers.",
        editorContent: "class Solution:\n    pass",
        submissionContent: "class Solution:\n    pass",
        testcase: "[2,7,11,15]",
        judgeResult: { status_msg: "Wrong Answer" },
        filetype: "python",
      },
      {
        summary: "The hash map lookup happens after the insert.",
        annotations: [{ line: 2, reason: "order is wrong", severity: "error" }],
      },
    );

    const scope = manager.getActiveScope();
    assert.ok(scope);
    assert.equal(scope.titleSlug, "two-sum");
    assert.equal(scope.companionMemory?.messages.length, 2);
    assert.equal(scope.latestFailure?.judgeResult && typeof scope.latestFailure.judgeResult === "object" ? scope.latestFailure.judgeResult.status_msg : "", "Wrong Answer");
    assert.equal(scope.lastFailureAnalysis?.summary, "The hash map lookup happens after the insert.");

    const rendered = renderActiveSessionScope(scope);
    assert.match(rendered, /Title Slug: two-sum/);
    assert.match(rendered, /Latest LeetCode Failure/);
    assert.match(rendered, /Wrong Answer/);
    assert.match(rendered, /Latest Failure Analysis/);
    assert.match(rendered, /order is wrong/);
  });

  it("stores companion turns as session memory while stripping hidden context messages", () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate("two-sum");
    manager.recordCompanionContext({
      titleSlug: "two-sum",
      title: "Two Sum",
      description: "Find two numbers.",
      code: "class Solution:\n    pass",
    });

    const messages = manager.buildCompanionMessages([
      {
        role: "user",
        content: [
          "# LeetCode Problem Context",
          "",
          "- Title: Two Sum",
          "- Title Slug: two-sum",
        ].join("\n"),
      },
      { role: "user", content: "帮我看下为什么 test 过不了" },
    ]);

    assert.equal(messages[0]?.role, "user");
    assert.match(messages[0]?.content ?? "", /Submission Service Active Session/);
    assert.deepEqual(manager.getActiveScope()?.companionMemory?.messages, [
      { role: "user", content: "帮我看下为什么 test 过不了" },
    ]);
  });
});
