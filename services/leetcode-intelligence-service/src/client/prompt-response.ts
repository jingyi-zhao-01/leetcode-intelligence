import { GatewayIntentBits, type Message } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";
import { createLogger } from "../logger.ts";
import { DiscordClient } from "./discord-client.ts";
import { scorePromptReply } from "./prompt-flow.ts";

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
  private readonly discord: DiscordClient;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: PromptResponseClientConfig,
  ) {
    this.discord = new DiscordClient({
      scope: "client/prompt-response",
      botToken: config.botToken,
      channelId: config.channelId,
      intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
    });
  }

  async start(): Promise<void> {
    await this.discord.start({
      onMessage: (message: Message) => this.handleMessage(message),
    });
  }

  async stop(): Promise<void> {
    await this.discord.stop();
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

      await this.discord.ensureTargetChannel();
      const scored = (await scorePromptReply(this.service, {
        referenceMessageId,
        rawReply: message.content,
      })) as DiscordScoreResult | null;
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
