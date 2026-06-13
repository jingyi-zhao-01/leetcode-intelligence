import { createLogger } from "../../logger.ts";

type AsyncMethod<TArgs extends unknown[] = unknown[], TResult = unknown> = (...args: TArgs) => Promise<TResult>;
type AsyncOperation<TResult = unknown> = () => Promise<TResult>;
type OperationMeta = Record<string, unknown>;
type OperationMetaBuilder<TArgs extends unknown[] = unknown[]> = (...args: TArgs) => OperationMeta;

type LoggedOperationOptions<TArgs extends unknown[]> = {
  scope: string;
  operation: string;
  args: TArgs;
  buildMeta?: OperationMetaBuilder<TArgs>;
};

export async function runLoggedOperation<TArgs extends unknown[], TResult>(
  options: LoggedOperationOptions<TArgs>,
  operationFn: AsyncOperation<TResult>,
): Promise<TResult> {
  const { scope, operation, args, buildMeta } = options;
  const logger = createLogger(scope);
  const startedAt = Date.now();
  const meta = {
    operation,
    ...(buildMeta ? buildMeta(...args) : {}),
  };

  logger.info(meta, "operation started");

  try {
    const result = await operationFn();
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
}

export function LogOperation(
  scope: string,
  operation: string,
  buildMeta?: OperationMetaBuilder,
): MethodDecorator {
  return (
    _target: object,
    _propertyKey: string | symbol,
    descriptor: PropertyDescriptor,
  ): PropertyDescriptor => {
    const original = descriptor.value as AsyncMethod;

    descriptor.value = async function (...args: unknown[]): Promise<unknown> {
      return runLoggedOperation(
        {
          scope,
          operation,
          args,
          buildMeta,
        },
        () => original.apply(this, args),
      );
    };

    return descriptor;
  };
}
