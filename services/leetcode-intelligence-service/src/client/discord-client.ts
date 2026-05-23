import { once } from "node:events";

import { ChannelType, Client, GatewayIntentBits, type Message } from "discord.js";
import type { Logger } from "pino";

import { createLogger } from "../logger.ts";

const baseLogger = createLogger("client/discord");

export type DiscordClientConfig = {
  scope: string;
  botToken: string;
  channelId: string;
  intents: GatewayIntentBits[];
};

export type DiscordStartOptions = {
  onMessage?: (message: Message) => Promise<void> | void;
  waitUntilReady?: boolean;
};

export class DiscordClient {
  readonly channelId: string;

  private readonly discord: Client;
  private readonly logger: Logger;

  constructor(private readonly config: DiscordClientConfig) {
    this.channelId = config.channelId;
    this.discord = new Client({
      intents: config.intents,
    });
    this.logger = baseLogger.child({ clientScope: config.scope });
  }

  async start(options: DiscordStartOptions = {}): Promise<void> {
    this.logger.info({ channelId: this.channelId }, "starting client");
    this.discord.on("error", (error) => {
      this.logger.error({ err: error }, "discord client error");
    });
    if (options.onMessage) {
      this.discord.on("messageCreate", (message) => void options.onMessage?.(message));
    }
    this.discord.once("clientReady", () => {
      this.logger.info(
        {
          userTag: this.discord.user?.tag ?? "unknown",
          channelId: this.channelId,
        },
        "ready",
      );
    });

    this.logger.info("logging in bot");
    await this.discord.login(this.config.botToken);
    if (options.waitUntilReady && !this.discord.isReady()) {
      await once(this.discord, "clientReady");
    }
  }

  async stop(): Promise<void> {
    this.logger.info("stopping client");
    this.discord.removeAllListeners();
    await this.discord.destroy().catch(() => undefined);
    this.logger.info("client stopped");
  }

  async sendPrompt(promptText: string): Promise<{ messageId?: string }> {
    const channel = await this.resolveTextChannel();
    const sentMessage = await channel.send({ content: promptText });
    return { messageId: sentMessage.id };
  }

  async sendMessage(content: string): Promise<{ messageId?: string }> {
    const channel = await this.resolveTextChannel();
    const sentMessage = await channel.send({ content });
    return { messageId: sentMessage.id };
  }

  async ensureTargetChannel(): Promise<void> {
    await this.resolveTextChannel();
  }

  private async resolveTextChannel(): Promise<any> {
    const channel = await this.discord.channels.fetch(this.channelId);
    if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
      throw new Error(`Discord channel ${this.channelId} is not a guild text channel.`);
    }
    return channel;
  }
}
