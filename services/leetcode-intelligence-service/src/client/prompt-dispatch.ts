import cron from "node-cron";
import { GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../core.ts";
import { createLogger } from "../logger.ts";
import { DiscordClient } from "./discord-client.ts";
import { dispatchPrompt } from "./prompt-flow.ts";

const logger = createLogger("client/prompt-dispatch");

export type PromptDispatchClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  timezone?: string;
};

export const runPromptDispatchOnce = async (
  service: IntelligenceService,
  config: Omit<PromptDispatchClientConfig, "cronSchedule">,
): Promise<void> => {
  const discord = new DiscordClient({
    scope: "client/prompt-dispatch-once",
    botToken: config.botToken,
    channelId: config.channelId,
    intents: [GatewayIntentBits.Guilds],
  });

  logger.info({ channelId: config.channelId }, "starting one-shot client");
  await service.start();

  try {
    await discord.start({ waitUntilReady: true });
    const prompt = await dispatchPrompt(service, discord, "scheduled-once");
    if (prompt.ok === true) {
      logger.info(
        {
          channelId: config.channelId,
          messageId: prompt.messageId ?? null,
          promptEventId: prompt.promptEventId,
        },
        "sent prompt message",
      );
    }
  } finally {
    await discord.stop();
    await service.stop();
    logger.info("one-shot client stopped");
  }
};

export class PromptDispatchClient {
  private readonly discord: DiscordClient;
  private cronTask: ReturnType<typeof cron.schedule> | null = null;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: PromptDispatchClientConfig,
  ) {
    this.discord = new DiscordClient({
      scope: "client/prompt-dispatch",
      botToken: config.botToken,
      channelId: config.channelId,
      intents: [GatewayIntentBits.Guilds],
    });
  }

  async start(): Promise<void> {
    logger.info("starting client");
    await this.service.start();

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

  private async dispatchPrompt(): Promise<void> {
    logger.info({ channelId: this.config.channelId }, "cron tick: dispatching prompt");
    try {
      const prompt = await dispatchPrompt(this.service, this.discord, "scheduled");
      if (prompt.ok === true) {
        logger.info(
          {
            channelId: this.config.channelId,
            messageId: prompt.messageId ?? null,
            promptEventId: prompt.promptEventId,
          },
          "sent prompt message",
        );
      }
    } catch (error) {
      logger.error({ err: error }, "dispatch failed");
    }
  }
}
