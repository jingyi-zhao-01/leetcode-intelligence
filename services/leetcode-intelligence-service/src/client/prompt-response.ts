import { Client, ChannelType, GatewayIntentBits, type Message } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("client/prompt-response");

export type PromptResponseClientConfig = {
  botToken: string;
  channelId: string;
};

type DiscordScoreResult = {
  ok: boolean;
  questionSlug?: string;
  score?: number;
};

export class PromptResponseClient {
  private readonly discord = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
  });

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: PromptResponseClientConfig,
  ) {}

  async start(): Promise<void> {
    logger.info({ channelId: this.config.channelId }, "starting client");
    this.discord.on("error", (error) => {
      logger.error({ err: error }, "discord client error");
    });
    this.discord.on("messageCreate", (message: Message) => void this.handleMessage(message));
    this.discord.once("ready", () => {
      logger.info(
        {
          userTag: this.discord.user?.tag ?? "unknown",
          channelId: this.config.channelId,
        },
        "ready",
      );
    });
    logger.info("logging in bot");
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    logger.info("stopping client");
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    logger.info("client stopped");
  }

  private async handleMessage(message: Message): Promise<void> {
    try {
      logger.info(
        {
          messageId: message.id,
          channelId: message.channel.id,
          authorId: message.author.id,
          bot: message.author.bot,
        },
        "messageCreate",
      );

      if (message.author.bot) {
        logger.info({ messageId: message.id }, "ignored bot message");
        return;
      }
      if (message.channel.id !== this.config.channelId) {
        logger.info({ messageId: message.id, channelId: message.channel.id }, "ignored non-target channel message");
        return;
      }

      const referenceMessageId = message.reference?.messageId;
      if (!referenceMessageId) {
        logger.info({ messageId: message.id }, "ignored message without reference");
        return;
      }

      const channel = await this.discord.channels.fetch(this.config.channelId);
      if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
        throw new Error(`Discord channel ${this.config.channelId} is not a guild text channel.`);
      }

      const scored = (await this.service.scorePromptReplyByMessageId(referenceMessageId, message.content)) as DiscordScoreResult | null;
      if (!scored) {
        logger.warn({ messageId: message.id, referenceMessageId }, "no score generated");
        return;
      }

      logger.info(
        {
          questionSlug: scored.questionSlug ?? "unknown",
          score: scored.score ?? null,
          messageId: message.id,
          referenceMessageId,
        },
        "scored reply",
      );
    } catch (error) {
      logger.error({ err: error }, "failed handling messageCreate");
    }
  }
}
