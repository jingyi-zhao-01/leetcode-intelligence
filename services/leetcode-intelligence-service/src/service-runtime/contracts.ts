import type { FocusRecommendationResult, PromptTransport } from "../core/types.ts";

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
