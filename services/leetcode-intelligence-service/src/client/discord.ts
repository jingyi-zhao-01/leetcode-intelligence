import cron from "node-cron";
import { Client, ChannelType, GatewayIntentBits, Message } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";

type DiscordScoreResult = {
  ok: boolean;
  questionSlug?: string;
  score?: number;
};

export type DiscordIntelligenceClientConfig = {
  botToken: string;
  channelId: string;
  cronSchedule: string;
  timezone?: string;
};

export class DiscordIntelligenceClient {
  private readonly discord = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
  });
  private cronTask: any = null;

  constructor(
    private readonly service: IntelligenceService,
    private readonly config: DiscordIntelligenceClientConfig,
  ) {}

  async start(): Promise<void> {
    await this.service.start();
    this.discord.on("messageCreate", (message: Message) => void this.handleMessage(message));
    this.discord.once("ready", () => {
      console.error(`🧠 Intelligence bot ready as ${this.discord.user?.tag ?? "unknown"}`);
    });
    this.cronTask = cron.schedule(this.config.cronSchedule, () => void this.dispatchPrompt(), {
      timezone: this.config.timezone ?? process.env.TZ ?? "UTC",
    });
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    this.cronTask?.stop();
    this.cronTask = null;
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
  }

  private async dispatchPrompt(): Promise<void> {
    const prompt = await this.service.triggerPrompt("scheduled", { channelId: this.config.channelId });
    if (prompt.ok !== true || typeof prompt.promptText !== "string" || typeof prompt.promptEventId !== "string") {
      return;
    }

    const channel = await this.resolveChannel();
    const sentMessage = await channel.send({ content: prompt.promptText });
    await this.service.attachPromptMessage(prompt.promptEventId, sentMessage.id);
  }

  private async resolveChannel(): Promise<any> {
    const channel = await this.discord.channels.fetch(this.config.channelId);
    if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
      throw new Error(`Discord channel ${this.config.channelId} is not a guild text channel.`);
    }
    return channel;
  }

  private async handleMessage(message: Message): Promise<void> {
    if (message.author.bot || message.channel.id !== this.config.channelId) {
      return;
    }

    const referenceMessageId = message.reference?.messageId;
    if (!referenceMessageId) {
      return;
    }

    const scored = (await this.service.scorePromptReplyByMessageId(referenceMessageId, message.content)) as DiscordScoreResult | null;
    if (!scored) {
      return;
    }

    console.error(`🧠 Scored reply for ${scored.questionSlug ?? "unknown"}: ${scored.score ?? "?"}/5`);
  }
}
