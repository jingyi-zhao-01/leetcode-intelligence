import pino, { type Logger } from "pino";

const serviceLogger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  base: {
    service: "leetcode-intelligence-service",
  },
  timestamp: pino.stdTimeFunctions.isoTime,
  serializers: {
    err: pino.stdSerializers.err,
  },
});

export const createLogger = (scope: string): Logger => {
  return serviceLogger.child({ scope });
};

export const logger = createLogger("app");