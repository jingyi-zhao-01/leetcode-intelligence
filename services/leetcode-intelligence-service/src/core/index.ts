import { PrismaClient } from "@prisma/client";
import { OpenRouter } from "@openrouter/sdk";

import {
  type FocusRecommendationResult,
  type IntelligenceConfig,
  type PromptTransport,
} from "./types.ts";
import { loadIntelligenceConfig } from "./env.ts";
import { LogOperation } from "./decorators/logging.ts";
import { FallbackScoringAlgorithm, OpenRouterScoringAlgorithm, PromptGenerator, PromptResponseService, ReplyScorer } from "./scoring/index.ts";
import { FocusRecommendationService } from "./recommendation/index.ts";
import { LinearWeightCalculator } from "./shared/weight.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("intelligence");
const databaseLogger = createLogger("core/database-decorator");

type DatabaseOperationMeta = {
  operation: string;
  promptEventId?: string;
  messageId?: string;
  triggerSource?: string;
  channelId?: string;
  limit?: number;
  rawReplyChars?: number;
};

export interface IntelligenceService {
  start(): Promise<void>;
  stop(): Promise<void>;
  health(): Promise<Record<string, unknown>>;
  triggerPrompt(triggerSource?: string, transport?: PromptTransport): Promise<Record<string, unknown>>;
  attachPromptMessage(promptEventId: string, messageId: string): Promise<void>;
  scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>>;
  scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null>;
  recommendFocus(limit?: number): Promise<FocusRecommendationResult>;
}

class IntelligenceCoreService implements IntelligenceService {
  private readonly openRouter: OpenRouter | null;
  private readonly promptGenerator: PromptGenerator;
  private readonly responseService: PromptResponseService;
  private readonly recommendationService: FocusRecommendationService;

  constructor(
    private readonly prisma: PrismaClient,
    private readonly config: IntelligenceConfig,
  ) {
    const apiKey = this.config.OPEN_ROUTER_API_KEY;
    logger.info(
      {
        model: this.config.MODEL,
        openRouterKeyPresent: Boolean(apiKey),
        promptChannelConfigured: Boolean(this.config.PROMPT_DISCORD_CHANNEL_ID),
        recommendChannelConfigured: Boolean(this.config.RECOMMEND_DISCORD_CHANNEL_ID),
      },
      "initializing service",
    );

    this.openRouter = apiKey
      ? new OpenRouter({
          apiKey,
          httpReferer: "https://github.com/kawre/leetcode.nvim",
          appTitle: "leetcode-intelligence-service",
        })
      : null;

    const primaryAlgorithm = this.openRouter ? new OpenRouterScoringAlgorithm(this.openRouter, this.config.MODEL) : null;
    const scorer = new ReplyScorer(primaryAlgorithm, new FallbackScoringAlgorithm());
    const weightCalculator = new LinearWeightCalculator();
    this.promptGenerator = new PromptGenerator(this.prisma, this.config, weightCalculator);
    this.responseService = new PromptResponseService(this.prisma, scorer, this.config, weightCalculator);
    this.recommendationService = new FocusRecommendationService(this.prisma, this.openRouter, this.config, {
      weightCalculator,
    });
  }

  async start(): Promise<void> {
    logger.info("intelligence service ready");
  }

  async stop(): Promise<void> {
    logger.info("intelligence service stopped");
  }

  async health(): Promise<Record<string, unknown>> {
    return {
      status: "ok",
      service: "leetcode-intelligence-service",
    };
  }

  async triggerPrompt(triggerSource = "manual", transport?: PromptTransport): Promise<Record<string, unknown>> {
    return this.promptGenerator.generate(triggerSource, transport);
  }

  async attachPromptMessage(promptEventId: string, messageId: string): Promise<void> {
    await this.prisma.intelligencePromptEvent.update({
      where: { id: promptEventId },
      data: {
        discordMessageId: messageId,
      },
    });
  }

  async scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    return this.responseService.accept(promptEventId, rawReply);
  }

  async scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    return this.responseService.acceptByMessageId(messageId, rawReply);
  }

  async recommendFocus(limit?: number): Promise<FocusRecommendationResult> {
    const resolvedLimit = limit ?? this.config.INTELLIGENCE_RECOMMEND_TOP_K;
    return this.recommendationService.recommend(resolvedLimit);
  }
}

class DatabaseBoundIntelligenceService implements IntelligenceService {
  private dbQueue: Promise<void> = Promise.resolve();

  constructor(
    private readonly inner: IntelligenceService,
    private readonly prisma: PrismaClient,
  ) {}

  async start(): Promise<void> {
    await this.inner.start();
  }

  async stop(): Promise<void> {
    await this.inner.stop();
    await this.prisma.$disconnect().catch(() => undefined);
  }

  async health(): Promise<Record<string, unknown>> {
    return this.inner.health();
  }

  @LogOperation("core/database-decorator", "triggerPrompt", (triggerSource = "manual", transport?: PromptTransport) => ({
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

  @LogOperation("core/database-decorator", "attachPromptMessage", (promptEventId: string, messageId: string) => ({
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

  @LogOperation("core/database-decorator", "scorePromptReply", (promptEventId: string, rawReply: string) => ({
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

  @LogOperation("core/database-decorator", "scorePromptReplyByMessageId", (messageId: string, rawReply: string) => ({
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

  @LogOperation("core/database-decorator", "recommendFocus", (limit?: number) => ({
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
    await this.prisma.$connect();
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
      await this.prisma.$disconnect().catch(() => undefined);
      release();
    }
  }
}

export const createIntelligenceService = async (): Promise<IntelligenceService> => {
  const config = loadIntelligenceConfig();
  const prisma = new PrismaClient();
  const core = new IntelligenceCoreService(prisma, config);
  return new DatabaseBoundIntelligenceService(core, prisma);
};
