import cron from "node-cron";
import { Client, ChannelType, GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("client/prompt-dispatch");

export type PromptDispatchClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  timezone?: string;
};

const resolveTextChannel = async (client: Client, channelId: string): Promise<any> => {
  const channel = await client.channels.fetch(channelId);
  if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
    throw new Error(`Discord channel ${channelId} is not a guild text channel.`);
  }
  return channel;
};

export class PromptDispatchClient {
  private readonly discord = new Client({
    intents: [GatewayIntentBits.Guilds],
  });
  private cronTask: ReturnType<typeof cron.schedule> | null = null;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: PromptDispatchClientConfig,
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

    this.cronTask = cron.schedule(this.config.cronSchedule, () => void this.dispatchPrompt(), {
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

  private async dispatchPrompt(): Promise<void> {
    logger.info({ channelId: this.config.channelId }, "cron tick: dispatching prompt");
    try {
      const prompt = await this.service.triggerPrompt("scheduled", { channelId: this.config.channelId });
      if (prompt.ok !== true || typeof prompt.promptText !== "string" || typeof prompt.promptEventId !== "string") {
        logger.warn("no prompt dispatched (service returned non-ready payload)");
        return;
      }

      const channel = await resolveTextChannel(this.discord, this.config.channelId);
      const sentMessage = await channel.send({ content: prompt.promptText });
      logger.info(
        {
          channelId: this.config.channelId,
          messageId: sentMessage.id,
          promptEventId: prompt.promptEventId,
        },
        "sent prompt message",
      );
      await this.service.attachPromptMessage(prompt.promptEventId, sentMessage.id);
      logger.info({ messageId: sentMessage.id, promptEventId: prompt.promptEventId }, "linked prompt message");
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
