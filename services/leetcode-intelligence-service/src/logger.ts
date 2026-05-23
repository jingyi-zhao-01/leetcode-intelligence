import { createServiceLogger } from "@leetcode-qa/shared/logger";

const serviceLogger = createServiceLogger({
  service: "leetcode-intelligence-service",
});

export const createLogger = serviceLogger.createLogger;
export const logger = serviceLogger.logger;
