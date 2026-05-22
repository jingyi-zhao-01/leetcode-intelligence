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
    await this.service.start();
    this.discord.once("ready", () => {
      console.error(`🧠 Prompt scheduler ready as ${this.discord.user?.tag ?? "unknown"}`);
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

    const channel = await resolveTextChannel(this.discord, this.config.channelId);
    const sentMessage = await channel.send({ content: prompt.promptText });
    await this.service.attachPromptMessage(prompt.promptEventId, sentMessage.id);
  }
}
