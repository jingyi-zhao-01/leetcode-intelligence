import { createLogger } from "../../logger.ts";

type AsyncMethod = (...args: unknown[]) => Promise<unknown>;
type OperationMeta = Record<string, unknown>;
type OperationMetaBuilder = (...args: any[]) => OperationMeta;

export function LogOperation(
  scope: string,
  operation: string,
  buildMeta?: OperationMetaBuilder,
): MethodDecorator {
  const logger = createLogger(scope);

  return (
    _target: object,
    _propertyKey: string | symbol,
    descriptor: PropertyDescriptor,
  ): PropertyDescriptor => {
    const original = descriptor.value as AsyncMethod;

    descriptor.value = async function (...args: unknown[]): Promise<unknown> {
      const startedAt = Date.now();
      const meta = {
        operation,
        ...(buildMeta ? buildMeta(...args) : {}),
      };

      logger.info(meta, "operation started");

      try {
        const result = await original.apply(this, args);
        logger.info(
          {
            ...meta,
            durationMs: Date.now() - startedAt,
          },
          "operation completed",
        );
        return result;
      } catch (error) {
        logger.warn(
          {
            ...meta,
            durationMs: Date.now() - startedAt,
            err: error,
          },
          "operation failed",
        );
        throw error;
      }
    };

    return descriptor;
  };
}
