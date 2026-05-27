import { LogOperation } from "../core/decorators/logging.ts";
import type { FocusRecommendationResult, PromptTransport } from "../core/types.ts";
import { createLogger } from "../logger.ts";
import type { IntelligenceService } from "./contracts.ts";
import type { PersistenceServices } from "./composition.ts";

const databaseLogger = createLogger("service-runtime/database-boundary");

type DatabaseOperationMeta = {
  operation: string;
  promptEventId?: string;
  messageId?: string;
  triggerSource?: string;
  channelId?: string;
  limit?: number;
  rawReplyChars?: number;
};

export class DatabaseBoundIntelligenceService implements IntelligenceService {
  private dbQueue: Promise<void> = Promise.resolve();

  constructor(
    private readonly inner: IntelligenceService,
    private readonly persistence: PersistenceServices,
  ) {}

  async start(): Promise<void> {
    await this.inner.start();
  }

  async stop(): Promise<void> {
    await this.inner.stop();
    await this.persistence.prisma.$disconnect().catch(() => undefined);
  }

  async health(): Promise<Record<string, unknown>> {
    return this.inner.health();
  }

  @LogOperation("service-runtime/database-boundary", "triggerPrompt", (triggerSource = "manual", transport?: PromptTransport) => ({
    triggerSource,
    channelId: transport?.channelId,
  }))
  async triggerPrompt(triggerSource = "manual", transport?: PromptTransport): Promise<Record<string, unknown>> {
    return this.withDatabase(
      () => this.inner.triggerPrompt(triggerSource, transport),
      {
        operation: "triggerPrompt",
        triggerSource,
        channelId: transport?.channelId,
      },
    );
  }

  @LogOperation("service-runtime/database-boundary", "attachPromptMessage", (promptEventId: string, messageId: string) => ({
    promptEventId,
    messageId,
  }))
  async attachPromptMessage(promptEventId: string, messageId: string): Promise<void> {
    await this.withDatabase(
      () => this.inner.attachPromptMessage(promptEventId, messageId),
      {
        operation: "attachPromptMessage",
        promptEventId,
        messageId,
      },
    );
  }

  @LogOperation("service-runtime/database-boundary", "scorePromptReply", (promptEventId: string, rawReply: string) => ({
    promptEventId,
    rawReplyChars: rawReply.length,
  }))
  async scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    return this.withDatabase(
      () => this.inner.scorePromptReply(promptEventId, rawReply),
      {
        operation: "scorePromptReply",
        promptEventId,
        rawReplyChars: rawReply.length,
      },
    );
  }

  @LogOperation("service-runtime/database-boundary", "scorePromptReplyByMessageId", (messageId: string, rawReply: string) => ({
    messageId,
    rawReplyChars: rawReply.length,
  }))
  async scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    return this.withDatabase(
      () => this.inner.scorePromptReplyByMessageId(messageId, rawReply),
      {
        operation: "scorePromptReplyByMessageId",
        messageId,
        rawReplyChars: rawReply.length,
      },
    );
  }

  @LogOperation("service-runtime/database-boundary", "recommendFocus", (limit?: number) => ({
    limit,
  }))
  async recommendFocus(limit?: number): Promise<FocusRecommendationResult> {
    return this.withDatabase(
      () => this.inner.recommendFocus(limit),
      {
        operation: "recommendFocus",
        limit,
      },
    );
  }

  private async withDatabase<T>(operation: () => Promise<T>, meta: DatabaseOperationMeta): Promise<T> {
    const previous = this.dbQueue;
    let release: () => void = () => undefined;
    const queuedAt = Date.now();

    this.dbQueue = new Promise<void>((resolve) => {
      release = resolve;
    });

    databaseLogger.info(meta, "database interaction queued");

    await previous;
    const waitMs = Date.now() - queuedAt;
    const connectStartedAt = Date.now();
    databaseLogger.info({ ...meta, queueWaitMs: waitMs }, "connecting prisma client");
    await this.persistence.prisma.$connect();
    const connectMs = Date.now() - connectStartedAt;
    const operationStartedAt = Date.now();
    databaseLogger.info({ ...meta, queueWaitMs: waitMs, connectMs }, "prisma client connected");

    try {
      const result = await operation();
      databaseLogger.info(
        {
          ...meta,
          queueWaitMs: waitMs,
          connectMs,
          operationMs: Date.now() - operationStartedAt,
          totalDbMs: Date.now() - queuedAt,
        },
        "database interaction completed",
      );
      return result;
    } catch (error) {
      databaseLogger.warn(
        {
          ...meta,
          queueWaitMs: waitMs,
          connectMs,
          operationMs: Date.now() - operationStartedAt,
          totalDbMs: Date.now() - queuedAt,
          err: error,
        },
        "database interaction failed",
      );
      throw error;
    } finally {
      await this.persistence.prisma.$disconnect().catch(() => undefined);
      release();
    }
  }
}
