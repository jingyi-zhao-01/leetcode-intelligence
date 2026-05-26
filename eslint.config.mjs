import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";

const trackedServiceFiles = [
  "services/ingestor/**/*.{js,mjs,cjs,ts,mts,cts}",
  "services/leetcode-submission-service/**/*.{js,mjs,cjs,ts,mts,cts}",
];

const trackedTestFiles = [
  "services/leetcode-submission-service/tests/**/*.{js,mjs,cjs,ts,mts,cts}",
];

export default tseslint.config(
  {
    ignores: [
      "**/node_modules/**",
      "**/dist/**",
      "**/build/**",
      "**/.venv/**",
      "**/__pycache__/**",
      "services/**/generated/**",
      "services/**/coverage/**",
    ],
  },
  {
    files: trackedServiceFiles,
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        ...globals.node,
      },
    },
    rules: {
      "no-console": "off",
    },
  },
  {
    files: trackedTestFiles,
    languageOptions: {
      globals: {
        ...globals.node,
        ...globals.vitest,
      },
    },
  },
);