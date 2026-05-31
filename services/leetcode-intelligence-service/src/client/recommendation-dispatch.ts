import cron from "node-cron";
import { GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../service-runtime/index.ts";
import { createLogger } from "../logger.ts";
import { DiscordClient } from "./discord-client.ts";
import { dispatchRecommendation } from "./recommendation-flow.ts";

const logger = createLogger("client/recommendation-dispatch");

export type RecommendationDispatchClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  topK: number;
  timezone?: string;
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
    await dispatchRecommendation(service, discord, config.topK);
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
      await dispatchRecommendation(this.service, this.discord, this.config.topK);
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
