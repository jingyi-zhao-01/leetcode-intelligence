import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";
import {
  extractThought,
  normalizeForEmbedding,
} from "../src/ts/codeCleaner.ts";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function loadSampleCode(): string {
  const samplePath = join(__dirname, "sample.txt");
  return readFileSync(samplePath, "utf8");
}

describe("codeCleaner", () => {
  it("extracts @thought from sample.txt", () => {
    const sample = loadSampleCode();
    const thought = extractThought(sample);

    assert.ok(thought);
    assert.ok(thought.toLowerCase().includes("two pointer approach"));
    assert.ok(thought.toLowerCase().includes("last non zero element"));
  });

  it("normalizes sample and removes class wrapper", () => {
    const sample = loadSampleCode();
    const normalized = normalizeForEmbedding(sample);

    assert.ok(normalized.includes("def moveZeroes"));
    assert.ok(normalized.includes("p1"));
    assert.ok(!normalized.includes("class Solution"));
    assert.ok(normalized.includes("#"));
  });

  it("extracts function from class wrapper", () => {
    const code = `class Solution:\n    def twoSum(self, nums, target):\n        return []`;

    const extracted = normalizeForEmbedding(code);
    assert.ok(extracted.startsWith("def twoSum"));
    assert.ok(!extracted.includes("class"));
  });

  it("retains comments while normalizing", () => {
    const code = `\n    class Solution:\n        def foo(x):\n            # This comment should be retained\n            return x + 1\n    `;

    const result = normalizeForEmbedding(code);
    assert.ok(result.includes("def foo"));
    assert.ok(result.includes("# This comment should be retained"));
    assert.ok(!result.includes("class"));
  });

  it("returns null thought when @thought is absent", () => {
    const code = `class Solution:\n    def solve(self, nums):\n        # Regular comment without marker\n        return 42\n`;

    const thought = extractThought(code);
    assert.equal(thought, null);
  });
});
