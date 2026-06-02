import { once } from "node:events";

import { ChannelType, Client, EmbedBuilder, GatewayIntentBits, type Message, type TextChannel } from "discord.js";
import type { Logger } from "pino";

import { createLogger } from "../logger.ts";
import type { PromptDelivery, PromptDispatchSuccess } from "./contracts.ts";

const baseLogger = createLogger("client/discord");
const PROMPT_EMBED_COLOR = 0x5865F2;

const buildPromptEmbed = (promptText: string): EmbedBuilder => {
  const [firstLine, ...rest] = promptText.split("\n");
  const title = (firstLine?.trim() || "LeetCode Prompt").slice(0, 256);
  const description = rest.join("\n").trim().slice(0, 4096) || promptText.slice(0, 4096);

  return new EmbedBuilder()
    .setColor(PROMPT_EMBED_COLOR)
    .setTitle(title)
    .setDescription(description);
};

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

  async renderPrompt(prompt: PromptDispatchSuccess): Promise<PromptDelivery> {
    const channel = await this.resolveTextChannel();
    const sentMessage = await channel.send({ embeds: [buildPromptEmbed(prompt.promptText)] });
    return { messageId: sentMessage.id };
  }

  async renderText(content: string): Promise<PromptDelivery> {
    const channel = await this.resolveTextChannel();
    const sentMessage = await channel.send({ content });
    return { messageId: sentMessage.id };
  }

  async replyToMessage(message: Message, content: string): Promise<PromptDelivery> {
    const sentMessage = await message.reply({ content });
    return { messageId: sentMessage.id };
  }

  async addReaction(messageId: string, emoji: string): Promise<void> {
    const channel = await this.resolveTextChannel();
    const targetMessage = await channel.messages.fetch(messageId);
    await targetMessage.react(emoji);
  }

  async ensureTargetChannel(): Promise<void> {
    await this.resolveTextChannel();
  }

  private async resolveTextChannel(): Promise<TextChannel> {
    const channel = await this.discord.channels.fetch(this.channelId);
    if (!(channel?.isTextBased()) || channel.type !== ChannelType.GuildText) {
      throw new Error(`Discord channel ${this.channelId} is not a guild text channel.`);
    }
    return channel;
  }
}
