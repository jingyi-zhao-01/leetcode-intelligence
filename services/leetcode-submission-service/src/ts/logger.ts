import { createServiceLogger } from "../../../shared/logger.ts";

const serviceLogger = createServiceLogger({
  service: "leetcode-submission-service",
});

export const createLogger = serviceLogger.createLogger;
export const logger = serviceLogger.logger;