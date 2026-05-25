import assert from "node:assert/strict";
import { describe, it } from "vitest";

import { formatPacificTimestamp, inferIsTestSubmission } from "../src/ts/server.ts";

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
});
