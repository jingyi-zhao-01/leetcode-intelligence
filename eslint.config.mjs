import { createServiceLintConfig } from "./config/eslint/shared.mjs";

const trackedServiceFiles = [
  "services/**/*.{js,mjs,cjs,ts,mts,cts}",
];

const trackedTestFiles = [
  "services/**/__test__/**/*.{js,mjs,cjs,ts,mts,cts}",
  "services/**/tests/**/*.{js,mjs,cjs,ts,mts,cts}",
];

export default createServiceLintConfig({
  serviceFiles: trackedServiceFiles,
  testFiles: trackedTestFiles,
});
