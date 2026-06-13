import { trace } from "@opentelemetry/api";
import pino, { type Logger } from "pino";

const serviceLogger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  base: {
    service: "leetcode-intelligence-service",
  },
  mixin() {
    const spanContext = trace.getActiveSpan()?.spanContext();
    if (!spanContext?.traceId || !spanContext?.spanId) {
      return {};
    }

    return {
      trace_id: spanContext.traceId,
      span_id: spanContext.spanId,
    };
  },
  formatters: {
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
