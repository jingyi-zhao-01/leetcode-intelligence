import pino, { type Logger } from "pino";

const serviceLogger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  base: {
    service: "leetcode-intelligence-service",
  },
  formatters: {
    // Many log backends map textual severity more reliably than numeric pino levels.
    level(label, number) {
      return {
        level: label,
        level_num: number,
        severity: label.toUpperCase(),
      };
    },
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