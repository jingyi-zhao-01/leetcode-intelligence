import cron from "node-cron";
import { Client, ChannelType, GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("client/recommendation-dispatch");

export type RecommendationDispatchClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  topK: number;
  timezone?: string;
};

const resolveTextChannel = async (client: Client, channelId: string): Promise<any> => {
  const channel = await client.channels.fetch(channelId);
  if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
    throw new Error(`Discord channel ${channelId} is not a guild text channel.`);
  }
  return channel;
};

const formatRecommendations = (recommendations: Array<{ questionSlug: string; title: string; difficulty: string; priority: number; reason: string }>): string => {
  if (recommendations.length === 0) {
    return "No recommendations available right now.";
  }

  return recommendations
    .map((item, index) => `${index + 1}. ${item.title} [${item.questionSlug}] (${item.difficulty})\n   priority=${item.priority.toFixed(3)}\n   ${item.reason}`)
    .join("\n");
};

export class RecommendationDispatchClient {
  private readonly discord = new Client({
    intents: [GatewayIntentBits.Guilds],
  });
  private cronTask: ReturnType<typeof cron.schedule> | null = null;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: RecommendationDispatchClientConfig,
  ) {}

  async start(): Promise<void> {
    logger.info("starting client");
    await this.service.start();
    this.discord.on("error", (error) => {
      logger.error({ err: error }, "discord client error");
    });
    this.discord.once("ready", () => {
      logger.info(
        {
          userTag: this.discord.user?.tag ?? "unknown",
          channelId: this.config.channelId,
        },
        "ready",
      );
    });

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

    logger.info("logging in bot");
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    logger.info("stopping client");
    this.cronTask?.stop();
    this.cronTask = null;
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
    logger.info("client stopped");
  }

  private async dispatchRecommendation(): Promise<void> {
    logger.info({ channelId: this.config.channelId, topK: this.config.topK }, "cron tick: dispatching recommendations");
    try {
      const result = await this.service.recommendFocus(this.config.topK);
      const channel = await resolveTextChannel(this.discord, this.config.channelId);
      const body = [
        "Focus recommendation",
        "",
        result.narrative,
        "",
        formatRecommendations(result.recommendations),
      ].join("\n");

      const sentMessage = await channel.send({ content: body.slice(0, 1800) });
      logger.info(
        {
          messageId: sentMessage.id,
          channelId: this.config.channelId,
          count: result.recommendations.length,
        },
        "sent recommendations message",
      );
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
