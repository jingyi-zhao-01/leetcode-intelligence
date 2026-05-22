import { Client, ChannelType, GatewayIntentBits, type Message } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";

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
    console.error(`[discord][prompt-response] starting client for channel ${this.config.channelId}`);
    await this.service.start();
    this.discord.on("error", (error) => {
      console.error("[discord][prompt-response] discord client error", error);
    });
    this.discord.on("messageCreate", (message: Message) => void this.handleMessage(message));
    this.discord.once("ready", () => {
      console.error(`🧠 Prompt response listener ready as ${this.discord.user?.tag ?? "unknown"} for channel ${this.config.channelId}`);
    });
    console.error("[discord][prompt-response] logging in bot");
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    console.error("[discord][prompt-response] stopping client");
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
    console.error("[discord][prompt-response] client stopped");
  }

  private async handleMessage(message: Message): Promise<void> {
    try {
      console.error(
        `[discord][prompt-response] messageCreate messageId=${message.id} channelId=${message.channel.id} authorId=${message.author.id} bot=${message.author.bot}`,
      );

      if (message.author.bot) {
        console.error(`[discord][prompt-response] ignored bot message messageId=${message.id}`);
        return;
      }
      if (message.channel.id !== this.config.channelId) {
        console.error(
          `[discord][prompt-response] ignored non-target channel message messageId=${message.id} channelId=${message.channel.id}`,
        );
        return;
      }

      const referenceMessageId = message.reference?.messageId;
      if (!referenceMessageId) {
        console.error(`[discord][prompt-response] ignored message without reference messageId=${message.id}`);
        return;
      }

      const channel = await this.discord.channels.fetch(this.config.channelId);
      if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
        throw new Error(`Discord channel ${this.config.channelId} is not a guild text channel.`);
      }

      const scored = (await this.service.scorePromptReplyByMessageId(referenceMessageId, message.content)) as DiscordScoreResult | null;
      if (!scored) {
        console.error(
          `[discord][prompt-response] no score generated for messageId=${message.id} referenceMessageId=${referenceMessageId}`,
        );
        return;
      }

      console.error(
        `🧠 Scored reply for ${scored.questionSlug ?? "unknown"}: ${scored.score ?? "?"}/5 (messageId=${message.id}, referenceMessageId=${referenceMessageId})`,
      );
    } catch (error) {
      console.error("[discord][prompt-response] failed handling messageCreate", error);
    }
  }
}
