import cron from "node-cron";
import { Client, ChannelType, GatewayIntentBits } from "discord.js";

import type { IntelligenceService } from "../intelligence.ts";

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
    console.error("[discord][prompt-dispatch] starting client");
    await this.service.start();
    this.discord.on("error", (error) => {
      console.error("[discord][prompt-dispatch] discord client error", error);
    });
    this.discord.once("ready", () => {
      console.error(`🧠 Prompt scheduler ready as ${this.discord.user?.tag ?? "unknown"} for channel ${this.config.channelId}`);
    });

    this.cronTask = cron.schedule(this.config.cronSchedule, () => void this.dispatchPrompt(), {
      timezone: this.config.timezone ?? process.env.TZ ?? "UTC",
    });
    console.error(
      `[discord][prompt-dispatch] cron scheduled channel=${this.config.channelId} schedule="${this.config.cronSchedule}" timezone=${this.config.timezone ?? process.env.TZ ?? "UTC"}`,
    );

    console.error("[discord][prompt-dispatch] logging in bot");
    await this.discord.login(this.config.botToken);
  }

  async stop(): Promise<void> {
    console.error("[discord][prompt-dispatch] stopping client");
    this.cronTask?.stop();
    this.cronTask = null;
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    await this.service.stop();
    console.error("[discord][prompt-dispatch] client stopped");
  }

  private async dispatchPrompt(): Promise<void> {
    console.error(`[discord][prompt-dispatch] cron tick: dispatching prompt to channel ${this.config.channelId}`);
    try {
      const prompt = await this.service.triggerPrompt("scheduled", { channelId: this.config.channelId });
      if (prompt.ok !== true || typeof prompt.promptText !== "string" || typeof prompt.promptEventId !== "string") {
        console.error("[discord][prompt-dispatch] no prompt dispatched (service returned non-ready payload)");
        return;
      }

      const channel = await resolveTextChannel(this.discord, this.config.channelId);
      const sentMessage = await channel.send({ content: prompt.promptText });
      console.error(
        `[discord][prompt-dispatch] sent prompt message channel=${this.config.channelId} messageId=${sentMessage.id} promptEventId=${prompt.promptEventId}`,
      );
      await this.service.attachPromptMessage(prompt.promptEventId, sentMessage.id);
      console.error(`[discord][prompt-dispatch] linked messageId=${sentMessage.id} to promptEventId=${prompt.promptEventId}`);
    } catch (error) {
      console.error("[discord][prompt-dispatch] dispatch failed", error);
    }
  }
}
