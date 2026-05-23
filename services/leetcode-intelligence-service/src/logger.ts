import pino, { type Logger } from "pino";

const serviceLogger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  base: {
    service: "leetcode-intelligence-service",
  },
  formatters: {
    // Preserve pino's numeric `level` field for log collectors, while also
    // emitting explicit text fields that are easy to query in dashboards.
    level(label, number) {
      return {
        level: number,
        level_num: number,
        severity: label.toUpperCase(),
        severity_text: label.toUpperCase(),
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
