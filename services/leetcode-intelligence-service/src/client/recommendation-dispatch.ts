import cron from "node-cron";
import { GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../service-runtime/index.ts";
import type { FocusRecommendation } from "../core/types.ts";
import { createLogger } from "../logger.ts";
import { DiscordClient } from "./discord-client.ts";

const logger = createLogger("client/recommendation-dispatch");
const DISCORD_MESSAGE_MAX_LENGTH = 2000;

export type RecommendationDispatchClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  topK: number;
  timezone?: string;
};

const formatScore = (avgScore: number | null): string => (avgScore === null ? "n/a" : avgScore.toFixed(2));
const formatRecentSubmission = (days: number | null): string => (days === null ? "n/a" : `${days.toFixed(1)}d ago`);

const formatRecommendations = (recommendations: FocusRecommendation[]): string => {
  if (recommendations.length === 0) {
    return "No recommendations available right now.";
  }

  return recommendations
    .map(
      (item, index) =>
        [
          `### ${index + 1}. **${item.title}**`,
          `- Slug: \`${item.questionSlug}\``,
          `- Difficulty: **${item.difficulty}**`,
          `- Priority: \`${item.priority.toFixed(3)}\``,
          `- Signals: weight \`${item.signals.weight.toFixed(2)}\` | failure \`${Math.round(item.signals.failureRate * 100)}%\` | staleness \`${item.signals.stalenessDays}d\` | avg score \`${formatScore(item.signals.avgScore)}\``,
          `- Recent submissions: attempts \`${item.signals.recentAttemptCount}\` | failure streak \`${item.signals.recentFailureStreak}\` | last submit \`${formatRecentSubmission(item.signals.recentSubmissionDays)}\``,
          `- Why: ${item.reason}`,
        ].join("\n"),
    )
    .join("\n");
};

const splitDiscordMessage = (body: string): string[] => {
  if (body.length <= DISCORD_MESSAGE_MAX_LENGTH) {
    return [body];
  }

  const chunks: string[] = [];
  let remaining = body;

  while (remaining.length > DISCORD_MESSAGE_MAX_LENGTH) {
    const preferredBreak = remaining.lastIndexOf("\n### ", DISCORD_MESSAGE_MAX_LENGTH);
    const fallbackBreak = remaining.lastIndexOf("\n", DISCORD_MESSAGE_MAX_LENGTH);
    const splitAt =
      preferredBreak > 0 ? preferredBreak : fallbackBreak > 0 ? fallbackBreak : DISCORD_MESSAGE_MAX_LENGTH;

    chunks.push(remaining.slice(0, splitAt).trimEnd());
    remaining = remaining.slice(splitAt).trimStart();
  }

  if (remaining.length > 0) {
    chunks.push(remaining);
  }

  return chunks;
};

const dispatchRecommendationMessage = async (
  service: IntelligenceService,
  discord: DiscordClient,
  topK: number,
): Promise<void> => {
  const result = await service.recommendFocus(topK);
  const body = [
    "## Focus Recommendation",
    "",
    "**Summary**",
    result.narrative,
    "",
    "**Recommended Problems**",
    formatRecommendations(result.recommendations),
  ].join("\n");

  const chunks = splitDiscordMessage(body);
  const sentMessages = [];
  for (const chunk of chunks) {
    sentMessages.push(await discord.sendMessage(chunk));
  }

  logger.info(
    {
      messageId: sentMessages[0]?.messageId ?? null,
      channelId: discord.channelId,
      count: result.recommendations.length,
      chunkCount: sentMessages.length,
    },
    "sent recommendations message",
  );
};

export const runRecommendationDispatchOnce = async (
  service: IntelligenceService,
  config: Omit<RecommendationDispatchClientConfig, "cronSchedule">,
): Promise<void> => {
  const discord = new DiscordClient({
    scope: "client/recommendation-dispatch-once",
    botToken: config.botToken,
    channelId: config.channelId,
    intents: [GatewayIntentBits.Guilds],
  });

  logger.info({ channelId: config.channelId, topK: config.topK }, "starting one-shot client");
  await service.start();

  try {
    await discord.start({ waitUntilReady: true });
    await dispatchRecommendationMessage(service, discord, config.topK);
  } finally {
    await discord.stop();
    await service.stop();
    logger.info("one-shot client stopped");
  }
};

export class RecommendationDispatchClient {
  private readonly discord: DiscordClient;
  private cronTask: ReturnType<typeof cron.schedule> | null = null;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: RecommendationDispatchClientConfig,
  ) {
    this.discord = new DiscordClient({
      scope: "client/recommendation-dispatch",
      botToken: config.botToken,
      channelId: config.channelId,
      intents: [GatewayIntentBits.Guilds],
    });
  }

  async start(): Promise<void> {
    logger.info("starting client");
    await this.service.start();

    this.cronTask = cron.schedule(this.config.cronSchedule, () => void this.dispatchRecommendation(), {
      timezone: this.config.timezone ?? process.env.TZ ?? "UTC",
    });
    logger.info(
      {
        channelId: this.config.channelId,
        schedule: this.config.cronSchedule,
        timezone: this.config.timezone ?? process.env.TZ ?? "UTC",
      },
      "cron scheduled",
    );

    await this.discord.start();
  }

  async stop(): Promise<void> {
    logger.info("stopping client");
    this.cronTask?.stop();
    this.cronTask = null;
    await this.discord.stop();
    await this.service.stop();
    logger.info("client stopped");
  }

  private async dispatchRecommendation(): Promise<void> {
    logger.info({ channelId: this.config.channelId, topK: this.config.topK }, "cron tick: dispatching recommendations");
    try {
      await dispatchRecommendationMessage(this.service, this.discord, this.config.topK);
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
