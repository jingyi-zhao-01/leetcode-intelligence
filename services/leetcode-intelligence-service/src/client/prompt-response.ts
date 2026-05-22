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
    await this.service.start();
    this.discord.on("messageCreate", (message: Message) => void this.handleMessage(message));
    this.discord.once("ready", () => {
      console.error(`🧠 Prompt response listener ready as ${this.discord.user?.tag ?? "unknown"}`);
    });
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
  }

  private async handleMessage(message: Message): Promise<void> {
    if (message.author.bot || message.channel.id !== this.config.channelId) {
      return;
    }

    const referenceMessageId = message.reference?.messageId;
    if (!referenceMessageId) {
      return;
    }

    const channel = await this.discord.channels.fetch(this.config.channelId);
    if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
      throw new Error(`Discord channel ${this.config.channelId} is not a guild text channel.`);
    }

    const scored = (await this.service.scorePromptReplyByMessageId(referenceMessageId, message.content)) as DiscordScoreResult | null;
    if (!scored) {
      return;
    }

    console.error(`🧠 Scored reply for ${scored.questionSlug ?? "unknown"}: ${scored.score ?? "?"}/5`);
  }
}
