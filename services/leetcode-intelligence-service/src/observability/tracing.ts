import {
  context,
  propagation,
  SpanKind,
  SpanStatusCode,
  trace,
  type Attributes,
  type Context,
  type Tracer,
} from '@opentelemetry/api';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';
import { defaultResource, resourceFromAttributes } from '@opentelemetry/resources';
import { NodeSDK } from '@opentelemetry/sdk-node';

import { createLogger } from '../logger.ts';

const OBSERVABILITY_NAMESPACE = 'homelab-cloud';
const logger = createLogger('observability/tracing');

let sdk: NodeSDK | null = null;
let configuredServiceName: string | null = null;

const parseOtelHeaders = (headerValue: string): Record<string, string> | undefined => {
  const headers = Object.fromEntries(
    headerValue
      .split(',')
      .map((entry) => entry.trim())
      .filter(Boolean)
      .map((entry) => {
        const separatorIndex = entry.indexOf('=');
        if (separatorIndex === -1) {
          return [entry, ''];
        }

        return [entry.slice(0, separatorIndex).trim(), entry.slice(separatorIndex + 1).trim()];
      })
      .filter(([key]) => Boolean(key)),
  );

  return Object.keys(headers).length > 0 ? headers : undefined;
};

const buildResource = (serviceName: string) => {
  return defaultResource().merge(
    resourceFromAttributes({
      'service.name': process.env.OTEL_SERVICE_NAME?.trim() || serviceName,
      'service.namespace': process.env.OTEL_SERVICE_NAMESPACE?.trim() || OBSERVABILITY_NAMESPACE,
    }),
  );
};

const createTraceExporter = () => {
  const endpoint =
    process.env.OTEL_EXPORTER_OTLP_TRACES_ENDPOINT?.trim() || process.env.OTEL_EXPORTER_OTLP_ENDPOINT?.trim() || '';

  if (!endpoint) {
    logger.warn('OTLP trace exporter endpoint is not configured; spans will stay local only');
    return null;
  }

  const protocol = process.env.OTEL_EXPORTER_OTLP_PROTOCOL?.trim() || 'http/protobuf';
  if (protocol !== 'http/protobuf') {
    logger.warn({ protocol }, 'unsupported OTLP protocol configured; falling back to http/protobuf');
  }

  return new OTLPTraceExporter({
    url: endpoint,
    headers: parseOtelHeaders(process.env.OTEL_EXPORTER_OTLP_HEADERS?.trim() || ''),
  });
};

export const configureTracing = async (serviceName: string): Promise<void> => {
  if (sdk) {
    if (configuredServiceName && configuredServiceName !== serviceName) {
      logger.warn({ configuredServiceName, requestedServiceName: serviceName }, 'tracing already configured');
    }
    return;
  }

  sdk = new NodeSDK({
    autoDetectResources: true,
    resource: buildResource(serviceName),
    traceExporter: createTraceExporter() ?? undefined,
  });
  sdk.start();
  configuredServiceName = serviceName;
  logger.info({ serviceName }, 'tracing configured');
};

export const shutdownTracing = async (): Promise<void> => {
  if (!sdk) {
    return;
  }

  const activeSdk = sdk;
  sdk = null;
  configuredServiceName = null;
  await activeSdk.shutdown();
  logger.info('tracing shutdown complete');
};

export const getTracer = (name: string): Tracer => {
  return trace.getTracer(name);
};

export const extractContext = (headers: Record<string, string | string[] | undefined>): Context => {
  return propagation.extract(context.active(), headers);
};

export const recordSpanError = (
  span: {
    recordException: (error: Error) => void;
    setStatus: (status: { code: SpanStatusCode; message?: string }) => void;
    setAttribute: (key: string, value: string | number | boolean) => void;
  },
  error: unknown,
) => {
  const normalizedError = error instanceof Error ? error : new Error(String(error));
  span.recordException(normalizedError);
  span.setAttribute('error', true);
  span.setStatus({
    code: SpanStatusCode.ERROR,
    message: normalizedError.message,
  });
};

export const startActiveSpan = async <T>(
  tracerName: string,
  spanName: string,
  options: {
    attributes?: Attributes;
    context?: Context;
    kind?: SpanKind;
  },
  callback: () => Promise<T>,
): Promise<T> => {
  const tracer = getTracer(tracerName);
  return tracer.startActiveSpan(
    spanName,
    {
      attributes: options.attributes,
      kind: options.kind,
      root: false,
    },
    options.context ?? context.active(),
    async (span) => {
      try {
        return await callback();
      } catch (error) {
        recordSpanError(span, error);
        throw error;
      } finally {
        span.end();
      }
    },
  );
};
