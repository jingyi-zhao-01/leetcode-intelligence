import pino, { type Logger } from "pino";

interface ServiceLoggerOptions {
  service: string;
  level?: string;
}

export const createServiceLogger = (
  options: ServiceLoggerOptions,
): { createLogger: (scope: string) => Logger; logger: Logger } => {
  const serviceLogger = pino({
    level: options.level ?? process.env.LOG_LEVEL ?? "info",
    base: {
      service: options.service,
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

  const createLogger = (scope: string): Logger => {
    return serviceLogger.child({ scope });
  };

  return {
    createLogger,
    logger: createLogger("app"),
  };
};
