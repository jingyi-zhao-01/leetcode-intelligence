import { randomUUID } from "node:crypto";

import { context, SpanKind, SpanStatusCode, trace } from "@opentelemetry/api";
import type { NextFunction, Request, Response } from "express";

import { createLogger } from "../logger.ts";
import { extractContext, getTracer, recordSpanError } from "./tracing.ts";

const logger = createLogger("observability/http");

const requestPathLabel = (req: Request): string => {
  const routePath = typeof req.route?.path === "string" ? req.route.path : "";
  if (routePath) {
    return `${req.baseUrl || ""}${routePath}` || req.path;
  }

  return req.originalUrl || req.path;
};

const routeToOperation = (path: string): string => {
  return path.replace(/^\/+/, "").replace(/[/:{}-]+/g, "_").replace(/_+/g, "_").replace(/^_+|_+$/g, "") || "root";
};

export const createHttpTracingMiddleware = (serviceName: string, serviceClass: string) => {
  const tracer = getTracer(serviceName);

  return (req: Request, res: Response, next: NextFunction) => {
    const startTime = process.hrtime.bigint();
    const requestIdHeader = req.header("x-request-id");
    const requestId = requestIdHeader?.trim() || randomUUID();
    const initialPath = req.baseUrl ? `${req.baseUrl}${req.path}` : req.path;
    const extractedContext = extractContext(req.headers);
    const spanName = `${req.method} ${initialPath}`;
    const operation = routeToOperation(initialPath);
    const span = tracer.startSpan(
      spanName,
      {
        kind: SpanKind.SERVER,
        attributes: {
          "http.request.method": req.method,
          "url.path": req.path,
          "leetcode_intelligence.request_id": requestId,
          "leetcode_intelligence.service_class": serviceClass,
          "leetcode_intelligence.operation": operation,
        },
      },
      extractedContext,
    );
    const spanContext = trace.setSpan(extractedContext, span);
    let finalized = false;

    res.locals.requestId = requestId;
    res.setHeader("x-request-id", requestId);

    const finalize = (error?: unknown) => {
      if (finalized) {
        return;
      }
      finalized = true;

      const durationMs = Number(process.hrtime.bigint() - startTime) / 1_000_000;
      const routePath = requestPathLabel(req);
      const routeOperation = routeToOperation(routePath);

      span.setAttribute("http.response.status_code", res.statusCode);
      span.setAttribute("http.route", routePath);
      span.setAttribute("url.path", routePath);
      span.setAttribute("leetcode_intelligence.operation", routeOperation);
      span.setAttribute("leetcode_intelligence.duration_ms", durationMs);

      if (error) {
        recordSpanError(span, error);
      } else if (res.statusCode >= 500) {
        span.setStatus({ code: SpanStatusCode.ERROR });
      } else {
        span.setStatus({ code: SpanStatusCode.OK });
      }

      const log = res.statusCode >= 400 || error ? logger.error.bind(logger) : logger.info.bind(logger);
      log(
        {
          event: "request",
          service: serviceName,
          service_class: serviceClass,
          operation: routeOperation,
          request_id: requestId,
          method: req.method,
          path: routePath,
          status_code: res.statusCode,
          duration_ms: Number(durationMs.toFixed(2)),
        },
        "request complete",
      );

      span.end();
    };

    res.on("finish", () => {
      finalize();
    });

    res.on("close", () => {
      if (!res.writableEnded) {
        finalize(new Error("request closed before response finished"));
      }
    });

    return context.with(spanContext, () => {
      next();
    });
  };
};
