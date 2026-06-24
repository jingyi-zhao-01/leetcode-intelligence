import { SpanKind } from '@opentelemetry/api';
import type { Request, Response } from 'express';

import { createLogger } from '../logger.ts';
import { startActiveSpan } from './tracing.ts';

const logger = createLogger('observability/bff');

const formatError = (error: unknown): string => {
  if (error instanceof Error) {
    return error.message;
  }

  return String(error);
};

export const runBffRoute = async <T>(
  req: Request,
  res: Response,
  operationName: string,
  handler: () => Promise<T>,
): Promise<void> => {
  try {
    const result = await startActiveSpan(
      'leetcode-intelligence-service',
      `bff.${operationName}`,
      {
        kind: SpanKind.INTERNAL,
        attributes: {
          'leetcode_intelligence.request_id': String(res.locals.requestId ?? ''),
          'leetcode_intelligence.operation': operationName,
          'leetcode_intelligence.service_class': 'bff',
          'http.request.method': req.method,
          'http.route': `${req.baseUrl || ''}${req.route?.path || req.path}`,
        },
      },
      handler,
    );

    if (!res.headersSent) {
      res.json(result);
    }
  } catch (error) {
    logger.error(
      {
        err: error,
        operation: operationName,
        request_id: res.locals.requestId,
        method: req.method,
        path: req.originalUrl || req.path,
      },
      'bff route failed',
    );

    if (!res.headersSent) {
      res.status(500).json({ error: formatError(error) });
    }
  }
};
