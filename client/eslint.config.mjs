import { createNextClientLintConfig, moduleDir } from "../config/eslint/shared.mjs";

export default createNextClientLintConfig(moduleDir(import.meta.url));
