import { PrismaClient } from "@prisma/client";
import { OpenRouter } from "@openrouter/sdk";

import {
  type FocusRecommendationResult,
  type IntelligenceConfig,
  type PromptTransport,
} from "./types.ts";
import { loadIntelligenceConfig } from "./env.ts";
import { FallbackScoringAlgorithm, OpenRouterScoringAlgorithm, ReplyScorer } from "./scoring.ts";
import { PromptGenerator } from "./prompt.ts";
import { PromptResponseService } from "./response.ts";
import { FocusRecommendationService } from "./recommendation.ts";

export class IntelligenceService {
  private readonly prisma: any = new PrismaClient();
  private readonly openRouter: OpenRouter | null;
  private readonly promptGenerator: PromptGenerator;
  private readonly responseService: PromptResponseService;
  private readonly recommendationService: FocusRecommendationService;

  constructor(private readonly config: IntelligenceConfig) {
    const apiKey = this.config.OPEN_ROUTER_API_KEY ?? this.config.API_KEY;
    this.openRouter = apiKey
      ? new OpenRouter({
          apiKey,
          httpReferer: "https://github.com/kawre/leetcode.nvim",
          appTitle: "leetcode-intelligence-service",
        })
      : null;

    const primaryAlgorithm = this.openRouter ? new OpenRouterScoringAlgorithm(this.openRouter, this.config.MODEL) : null;
    const scorer = new ReplyScorer(primaryAlgorithm, new FallbackScoringAlgorithm());
    this.promptGenerator = new PromptGenerator(this.prisma, this.config);
    this.responseService = new PromptResponseService(this.prisma, scorer, this.config);
    this.recommendationService = new FocusRecommendationService(this.prisma, this.openRouter, this.config);
  }

  async start(): Promise<void> {
    await this.prisma.$connect();
  }

  async stop(): Promise<void> {
    await this.prisma.$disconnect().catch(() => undefined);
  }

  async health(): Promise<Record<string, unknown>> {
    const count = await this.prisma.intelligencePromptEvent.count();
    return {
      status: "ok",
      service: "leetcode-intelligence-service",
      prompts: count,
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

export const createIntelligenceService = async (): Promise<IntelligenceService> => {
  return new IntelligenceService(loadIntelligenceConfig());
};