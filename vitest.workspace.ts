import { defineWorkspace } from "vitest/config";

export default defineWorkspace([
  {
    test: {
      name: "leetcode-intelligence-service",
      root: "./services/leetcode-intelligence-service",
      environment: "node",
      include: ["__test__/**/*.test.ts"],
    },
  },
  {
    test: {
      name: "leetcode-submission-service",
      root: "./services/leetcode-submission-service",
      environment: "node",
      include: ["tests/**/*.test.ts"],
    },
  },
]);
