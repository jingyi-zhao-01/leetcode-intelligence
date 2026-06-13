import path from "node:path";
import { fileURLToPath } from "node:url";

import { FlatCompat } from "@eslint/eslintrc";
import { defineConfig, globalIgnores } from "eslint/config";

const baseDirectory = path.dirname(fileURLToPath(import.meta.url));
const compat = new FlatCompat({ baseDirectory });

export default defineConfig([
  ...compat.extends("next/core-web-vitals"),
  globalIgnores([
    "**/node_modules/**",
    "**/dist/**",
    "**/build/**",
    ".next/**",
    "out/**",
    "next-env.d.ts",
  ]),
]);
