import { defineConfig, defineProject } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  test: {
    projects: [
      defineProject({
        plugins: [react()],
        test: {
          name: "leetcode-qa-client",
          root: "./client",
          cacheDir: "../node_modules/.vite/leetcode-qa-client",
          environment: "node",
          include: ["tests/**/*.test.ts", "tests/**/*.test.tsx"],
        },
      }),
      defineProject({
        test: {
          name: "leetcode-intelligence-service",
          root: "./services/leetcode-intelligence-service",
          cacheDir: "../../node_modules/.vite/leetcode-intelligence-service",
          environment: "node",
          include: ["__test__/**/*.test.ts"],
          exclude: ["__test__/openrouter-model.test.ts"],
        },
      }),
      defineProject({
        test: {
          name: "leetcode-submission-service",
          root: "./services/leetcode-submission-service",
          cacheDir: "../../node_modules/.vite/leetcode-submission-service",
          environment: "node",
          include: ["tests/**/*.test.ts"],
        },
      }),
      defineProject({
        test: {
          name: "leetcode-submission-classifier",
          root: "./services/leetcode-submission-classifier",
          cacheDir: "../../node_modules/.vite/leetcode-submission-classifier",
          environment: "node",
          include: ["tests/**/*.test.ts"],
        },
      }),
    ],
  },
});
