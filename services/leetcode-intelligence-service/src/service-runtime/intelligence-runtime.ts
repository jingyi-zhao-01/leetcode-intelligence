import type { FocusRecommendationResult, IntelligenceConfig, PromptTransport } from '../core/types.ts';
import { createLogger } from '../logger.ts';
import type { IntelligenceService } from './contracts.ts';
import type { RuntimeComposition } from './composition.ts';

const logger = createLogger('service-runtime/runtime');

export class IntelligenceRuntimeService implements IntelligenceService {
  constructor(
    private readonly composition: RuntimeComposition,
    private readonly config: IntelligenceConfig,
  ) {
    logger.info(
      {
        model: this.config.MODEL,
        openRouterKeyPresent: Boolean(this.config.OPEN_ROUTER_API_KEY),
        promptChannelConfigured: Boolean(this.config.PROMPT_DISCORD_CHANNEL_ID),
        recommendChannelConfigured: Boolean(this.config.RECOMMEND_DISCORD_CHANNEL_ID),
      },
      'initializing service runtime',
    );
  }

  async start(): Promise<void> {
    logger.info('intelligence service runtime ready');
  }

  async stop(): Promise<void> {
    logger.info('intelligence service runtime stopped');
  }

  async health(): Promise<Record<string, unknown>> {
    return {
      status: 'ok',
      service: 'leetcode-intelligence-service',
    };
  }

  async triggerPrompt(triggerSource = 'manual', transport?: PromptTransport): Promise<Record<string, unknown>> {
    return this.composition.domainServices.promptGenerator.generate(triggerSource, transport);
  }

  async attachPromptMessage(promptEventId: string, messageId: string): Promise<void> {
    await this.composition.persistence.prisma.intelligencePromptEvent.update({
      where: { id: promptEventId },
      data: {
        discordMessageId: messageId,
      },
    });
  }

  async scorePromptReply(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    return this.composition.domainServices.responseService.accept(promptEventId, rawReply);
  }

  async scorePromptReplyByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    return this.composition.domainServices.responseService.acceptByMessageId(messageId, rawReply);
  }

  async recommendFocus(limit?: number): Promise<FocusRecommendationResult> {
    const resolvedLimit = limit ?? this.config.INTELLIGENCE_RECOMMEND_TOP_K;
    return this.composition.domainServices.recommendationService.recommend(resolvedLimit);
  }
}
