import cron from "node-cron";
import { Client, ChannelType, GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";

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
    console.error("[discord][recommendation-dispatch] starting client");
    await this.service.start();
    this.discord.on("error", (error) => {
      console.error("[discord][recommendation-dispatch] discord client error", error);
    });
    this.discord.once("ready", () => {
      console.error(`🧠 Recommendation scheduler ready as ${this.discord.user?.tag ?? "unknown"} for channel ${this.config.channelId}`);
    });

    this.cronTask = cron.schedule(this.config.cronSchedule, () => void this.dispatchRecommendation(), {
      timezone: this.config.timezone ?? process.env.TZ ?? "UTC",
    });
    console.error(
      `[discord][recommendation-dispatch] cron scheduled channel=${this.config.channelId} schedule="${this.config.cronSchedule}" timezone=${this.config.timezone ?? process.env.TZ ?? "UTC"}`,
    );

    console.error("[discord][recommendation-dispatch] logging in bot");
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    console.error("[discord][recommendation-dispatch] stopping client");
    this.cronTask?.stop();
    this.cronTask = null;
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
    console.error("[discord][recommendation-dispatch] client stopped");
  }

  private async dispatchRecommendation(): Promise<void> {
    console.error(
      `[discord][recommendation-dispatch] cron tick: dispatching recommendations to channel=${this.config.channelId} topK=${this.config.topK}`,
    );
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
      console.error(
        `[discord][recommendation-dispatch] sent recommendations messageId=${sentMessage.id} channel=${this.config.channelId} count=${result.recommendations.length}`,
      );
    } catch (error) {
      console.error("[discord][recommendation-dispatch] dispatch failed", error);
    }
  }
}
