import { once } from "node:events";

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

const dispatchPromptMessage = async (
  service: IntelligenceService,
  discord: Client,
  channelId: string,
  triggerSource: string,
): Promise<void> => {
  const prompt = await service.triggerPrompt(triggerSource, { channelId });
  if (prompt.ok !== true || typeof prompt.promptText !== "string" || typeof prompt.promptEventId !== "string") {
    logger.warn("no prompt dispatched (service returned non-ready payload)");
    return;
  }

  const channel = await resolveTextChannel(discord, channelId);
  const sentMessage = await channel.send({ content: prompt.promptText });
  logger.info(
    {
      channelId,
      messageId: sentMessage.id,
      promptEventId: prompt.promptEventId,
    },
    "sent prompt message",
  );
  await service.attachPromptMessage(prompt.promptEventId, sentMessage.id);
  logger.info({ messageId: sentMessage.id, promptEventId: prompt.promptEventId }, "linked prompt message");
};

export const runPromptDispatchOnce = async (
  service: IntelligenceService,
  config: Omit<PromptDispatchClientConfig, "cronSchedule">,
): Promise<void> => {
  const discord = new Client({
    intents: [GatewayIntentBits.Guilds],
  });

  logger.info({ channelId: config.channelId }, "starting one-shot client");
  await service.start();

  try {
    discord.on("error", (error) => {
      logger.error({ err: error }, "discord client error");
    });
    discord.once("clientReady", () => {
      logger.info(
        {
          userTag: discord.user?.tag ?? "unknown",
          channelId: config.channelId,
        },
        "ready",
      );
    });

    logger.info("logging in bot");
    await discord.login(config.botToken);
    if (!discord.isReady()) {
      await once(discord, "clientReady");
    }

    await dispatchPromptMessage(service, discord, config.channelId, "scheduled-once");
  } finally {
    discord.removeAllListeners();
    await discord.destroy().catch(() => undefined);
    await service.stop();
    logger.info("one-shot client stopped");
  }
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
    this.discord.once("clientReady", () => {
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
      await dispatchPromptMessage(this.service, this.discord, this.config.channelId, "scheduled");
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
