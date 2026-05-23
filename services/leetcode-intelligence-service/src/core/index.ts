import { PrismaClient } from "@prisma/client";
import { OpenRouter } from "@openrouter/sdk";

import {
  type FocusRecommendationResult,
  type IntelligenceConfig,
  type PromptTransport,
} from "./types.ts";
import { loadIntelligenceConfig } from "./env.ts";
import { FallbackScoringAlgorithm, OpenRouterScoringAlgorithm, PromptGenerator, PromptResponseService, ReplyScorer } from "./scoring/index.ts";
import { FocusRecommendationService } from "./recommendation/index.ts";
import { LinearWeightCalculator } from "./shared/weight.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("intelligence");

export class IntelligenceService {
  private readonly prisma: any = new PrismaClient();
  private readonly openRouter: OpenRouter | null;
  private readonly promptGenerator: PromptGenerator;
  private readonly responseService: PromptResponseService;
  private readonly recommendationService: FocusRecommendationService;
  private dbQueue: Promise<void> = Promise.resolve();

  constructor(private readonly config: IntelligenceConfig) {
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
    return this.withDatabase(() => this.promptGenerator.generate(triggerSource, transport));
  }

  async attachPromptMessage(promptEventId: string, messageId: string): Promise<void> {
    await this.withDatabase(async () => {
      await this.prisma.intelligencePromptEvent.update({
        where: { id: promptEventId },
        data: {
          discordMessageId: messageId,
        },
      });
    });
  }

  async scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    return this.withDatabase(() => this.responseService.accept(promptEventId, rawReply));
  }

  async scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    return this.withDatabase(() => this.responseService.acceptByMessageId(messageId, rawReply));
  }

  async recommendFocus(limit?: number): Promise<FocusRecommendationResult> {
    return this.withDatabase(async () => {
      const resolvedLimit = limit ?? this.config.INTELLIGENCE_RECOMMEND_TOP_K;
      return this.recommendationService.recommend(resolvedLimit);
    });
  }

  private async withDatabase<T>(operation: () => Promise<T>): Promise<T> {
    const previous = this.dbQueue;
    let release: () => void = () => undefined;

    this.dbQueue = new Promise<void>((resolve) => {
      release = resolve;
    });

    await previous;
    await this.prisma.$connect();

    try {
      return await operation();
    } finally {
      await this.prisma.$disconnect().catch(() => undefined);
      release();
    }
  }
}

export const createIntelligenceService = async (): Promise<IntelligenceService> => {
  return new IntelligenceService(loadIntelligenceConfig());
};
