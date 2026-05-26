import { GatewayIntentBits, type Message } from "discord.js";

import type { IntelligenceService } from "../core.ts";
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
  message?: string;
  promptEventId?: string;
  questionSlug?: string;
  score?: number;
  previousWeight?: number;
  nextWeight?: number;
  tags?: string[];
  reason?: string;
  recommendedAnswer?: string;
};

const isTargetConversation = (message: Message, channelId: string): boolean =>
  message.channel.isThread?.() === true && message.channel.parentId === channelId;

const resolvePromptMessageId = (message: Message): string | null => {
  if (message.reference?.messageId) {
    return message.reference.messageId;
  }

  if (message.channel.isThread?.() === true) {
    return message.channel.id;
  }

  return null;
};

const formatScoreReply = (scored: DiscordScoreResult): string => {
  if (!scored.ok) {
    return `Evaluation finished but was not accepted: ${scored.message ?? "unknown reason"}`;
  }

  const parts = [
    `Evaluation result for \`${scored.questionSlug ?? "unknown"}\``,
    `Score: ${scored.score ?? "n/a"}`,
  ];

  if (typeof scored.previousWeight === "number" && typeof scored.nextWeight === "number") {
    parts.push(`Weight: ${scored.previousWeight.toFixed(2)} -> ${scored.nextWeight.toFixed(2)}`);
  }
  if (Array.isArray(scored.tags) && scored.tags.length > 0) {
    parts.push(`Tags: ${scored.tags.join(", ")}`);
  }
  if (scored.reason) {
    parts.push(`Reason: ${scored.reason}`);
  }
  if (scored.recommendedAnswer) {
    parts.push(`Recommended answer:\n${scored.recommendedAnswer}`);
  }

  return parts.join("\n");
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
      if (!isTargetConversation(message, this.config.channelId)) {
        logger.info({ messageId: message.id, channelId: message.channel.id }, "ignored non-target channel message");
        return;
      }

      const promptMessageId = resolvePromptMessageId(message);
      if (!promptMessageId) {
        logger.info({ messageId: message.id }, "ignored message without prompt message id");
        return;
      }

      await this.discord.ensureTargetChannel();
      const scored = (await scorePromptReply(this.service, {
        referenceMessageId: promptMessageId,
        rawReply: message.content,
      })) as DiscordScoreResult | null;
      if (!scored) {
        logger.warn({ messageId: message.id, promptMessageId }, "no score generated");
        return;
      }

      const feedback = formatScoreReply(scored);
      if (message.channel.isThread?.() === true) {
        if (!("send" in message.channel) || typeof message.channel.send !== "function") {
          throw new Error(`Thread channel ${message.channel.id} is not sendable.`);
        }
        await message.channel.send({ content: feedback });
      } else {
        await this.discord.replyToMessage(message, feedback);
      }

      logger.info(
        {
          questionSlug: scored.questionSlug ?? "unknown",
          score: scored.score ?? null,
          messageId: message.id,
          promptMessageId,
        },
        "scored reply",
      );
    } catch (error) {
      logger.error({ err: error }, "failed handling messageCreate");
    }
  }
}
