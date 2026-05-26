import assert from "node:assert/strict";
import { afterEach, describe, it } from "vitest";

import { ChannelType, Client, GatewayIntentBits } from "discord.js";

import { DiscordClient } from "../src/client/discord-client.ts";
import { PromptResponseClient } from "../src/client/prompt-response.ts";
import { dispatchPrompt, scorePromptReply } from "../src/client/prompt-flow.ts";

type FakePromptService = {
  triggerPromptCalls: Array<{ triggerSource: string; transport: { channelId: string } }>;
  attachPromptMessageCalls: Array<{ promptEventId: string; messageId: string }>;
  scorePromptReplyCalls: Array<{ promptEventId: string; rawReply: string }>;
  scorePromptReplyByMessageIdCalls: Array<{ messageId: string; rawReply: string }>;
  triggerPrompt: (triggerSource: string, transport: { channelId: string }) => Promise<Record<string, unknown>>;
  attachPromptMessage: (promptEventId: string, messageId: string) => Promise<void>;
  scorePromptReply: (promptEventId: string, rawReply: string) => Promise<Record<string, unknown>>;
  scorePromptReplyByMessageId: (messageId: string, rawReply: string) => Promise<Record<string, unknown> | null>;
};

const originalLogin = Client.prototype.login;
const originalIsReady = Client.prototype.isReady;
const originalDestroy = Client.prototype.destroy;

let sentMessages: Array<{
  channelId: string;
  content: string;
  embeds?: unknown[];
}> = [];
let startedThreads: Array<{
  messageId: string;
  name: string;
}> = [];
let stubChannelType = ChannelType.GuildText;
let stubIsTextBased = true;

const resetStubs = (): void => {
  Client.prototype.login = originalLogin;
  Client.prototype.isReady = originalIsReady;
  Client.prototype.destroy = originalDestroy;
  sentMessages = [];
  startedThreads = [];
  stubChannelType = ChannelType.GuildText;
  stubIsTextBased = true;
};

const installDiscordStub = (): void => {
  Client.prototype.login = (async function loginStub(this: Client) {
    (this as Client & { channels: { fetch: (channelId: string) => Promise<unknown> } }).channels = {
      fetch: async (channelId: string) => ({
        type: stubChannelType,
        isTextBased: () => stubIsTextBased,
        send: async ({ content, embeds }: { content?: string; embeds?: Array<{ toJSON?: () => unknown }> }) => {
          const messageId = `message-${sentMessages.length + 1}`;
          sentMessages.push({
            channelId,
            content: content ?? "",
            embeds: Array.isArray(embeds)
              ? embeds.map((embed) => (typeof embed?.toJSON === "function" ? embed.toJSON() : embed))
              : undefined,
          });
          return {
            id: messageId,
            startThread: async ({ name }: { name: string }) => {
              startedThreads.push({ messageId, name });
              return { id: `thread-${startedThreads.length}` };
            },
          };
        },
      }),
    };
    this.emit("clientReady", this);
    return "stub-token";
  }) as typeof Client.prototype.login;

  Client.prototype.isReady = (() => true) as typeof Client.prototype.isReady;
  Client.prototype.destroy = (async () => undefined) as typeof Client.prototype.destroy;
};

const createFakePromptService = (): FakePromptService => {
  const service: FakePromptService = {
    triggerPromptCalls: [],
    attachPromptMessageCalls: [],
    scorePromptReplyCalls: [],
    scorePromptReplyByMessageIdCalls: [],
    triggerPrompt: async (triggerSource, transport) => {
      service.triggerPromptCalls.push({ triggerSource, transport });
      return {
        ok: true,
        promptEventId: "prompt-event-1",
        promptText: "Solve two-sum",
        questionSlug: "two-sum",
      };
    },
    attachPromptMessage: async (promptEventId, messageId) => {
      service.attachPromptMessageCalls.push({ promptEventId, messageId });
    },
    scorePromptReply: async (promptEventId, rawReply) => {
      service.scorePromptReplyCalls.push({ promptEventId, rawReply });
      return { ok: true, promptEventId, score: 0.82 };
    },
    scorePromptReplyByMessageId: async (messageId, rawReply) => {
      service.scorePromptReplyByMessageIdCalls.push({ messageId, rawReply });
      return { ok: true, messageId, score: 0.91 };
    },
  };

  return service;
};

afterEach(() => {
  resetStubs();
});

describe("prompt-flow", () => {
  it("dispatchPrompt sends prompt text and links the returned message id", async () => {
    const service = createFakePromptService();
    const sentPromptBodies: string[] = [];

    const result = await dispatchPrompt(
      service as never,
      {
        channelId: "prompt-channel",
        sendPrompt: async (promptText: string) => {
          sentPromptBodies.push(promptText);
          return { messageId: "discord-message-1" };
        },
      },
      "scheduled",
    );

    assert.equal(result.ok, true);
    assert.equal(result.ok && result.messageId, "discord-message-1");
    assert.deepEqual(sentPromptBodies, ["Solve two-sum"]);
    assert.deepEqual(service.triggerPromptCalls, [
      {
        triggerSource: "scheduled",
        transport: { channelId: "prompt-channel" },
      },
    ]);
    assert.deepEqual(service.attachPromptMessageCalls, [
      {
        promptEventId: "prompt-event-1",
        messageId: "discord-message-1",
      },
    ]);
  });

  it("dispatchPrompt returns prompt generation failures without sending anything", async () => {
    const service = createFakePromptService();
    const sentPromptBodies: string[] = [];
    service.triggerPrompt = async (triggerSource, transport) => {
      service.triggerPromptCalls.push({ triggerSource, transport });
      return {
        ok: false,
        message: "No candidate submissions found.",
      };
    };

    const result = await dispatchPrompt(
      service as never,
      {
        channelId: "prompt-channel",
        sendPrompt: async (promptText: string) => {
          sentPromptBodies.push(promptText);
          return { messageId: "should-not-send" };
        },
      },
      "scheduled",
    );

    assert.deepEqual(result, {
      ok: false,
      message: "No candidate submissions found.",
    });
    assert.deepEqual(sentPromptBodies, []);
    assert.deepEqual(service.attachPromptMessageCalls, []);
  });

  it("scorePromptReply routes promptEventId requests to scorePromptReply", async () => {
    const service = createFakePromptService();

    const result = await scorePromptReply(service as never, {
      promptEventId: "prompt-event-1",
      rawReply: "Use a hash map.",
    });

    assert.deepEqual(result, { ok: true, promptEventId: "prompt-event-1", score: 0.82 });
    assert.deepEqual(service.scorePromptReplyCalls, [
      {
        promptEventId: "prompt-event-1",
        rawReply: "Use a hash map.",
      },
    ]);
    assert.deepEqual(service.scorePromptReplyByMessageIdCalls, []);
  });

  it("scorePromptReply routes referenceMessageId requests to scorePromptReplyByMessageId", async () => {
    const service = createFakePromptService();

    const result = await scorePromptReply(service as never, {
      referenceMessageId: "discord-message-1",
      rawReply: "Use two pointers.",
    });

    assert.deepEqual(result, { ok: true, messageId: "discord-message-1", score: 0.91 });
    assert.deepEqual(service.scorePromptReplyCalls, []);
    assert.deepEqual(service.scorePromptReplyByMessageIdCalls, [
      {
        messageId: "discord-message-1",
        rawReply: "Use two pointers.",
      },
    ]);
  });
});

describe("DiscordClient", () => {
  it("sendPrompt sends content to the configured text channel and starts a thread", async () => {
    installDiscordStub();
    const client = new DiscordClient({
      scope: "client/test",
      botToken: "bot-token",
      channelId: "prompt-channel",
      intents: [GatewayIntentBits.Guilds],
    });

    await client.start({ waitUntilReady: true });
    const delivery = await client.sendPrompt("Solve two-sum");
    await client.stop();

    assert.deepEqual(delivery, { messageId: "message-1" });
    assert.deepEqual(sentMessages, [
      {
        channelId: "prompt-channel",
        content: "",
        embeds: [
          {
            color: 5793266,
            title: "Solve two-sum",
            description: "Solve two-sum",
          },
        ],
      },
    ]);
    assert.deepEqual(startedThreads, [
      {
        messageId: "message-1",
        name: "Solve two-sum",
      },
    ]);
  });

  it("ensureTargetChannel rejects non-guild-text channels", async () => {
    installDiscordStub();
    stubChannelType = ChannelType.DM;
    stubIsTextBased = true;

    const client = new DiscordClient({
      scope: "client/test",
      botToken: "bot-token",
      channelId: "prompt-channel",
      intents: [GatewayIntentBits.Guilds],
    });

    await client.start({ waitUntilReady: true });
    await assert.rejects(
      () => client.ensureTargetChannel(),
      /Discord channel prompt-channel is not a guild text channel\./,
    );
    await client.stop();
  });
});

describe("PromptResponseClient", () => {
  it("treats a plain thread message as a reply to the thread starter prompt", async () => {
    const service = createFakePromptService();
    const client = new PromptResponseClient(service as never, {
      botToken: "bot-token",
      channelId: "prompt-channel",
    });

    (client as any).discord = {
      ensureTargetChannel: async () => undefined,
      stop: async () => undefined,
      start: async () => undefined,
    };

    const sentReplies: string[] = [];
    await (client as any).handleMessage({
      id: "user-message-1",
      content: "Use BFS level by level.",
      author: { id: "user-1", bot: false },
      reference: null,
      channel: {
        id: "prompt-message-1",
        parentId: "prompt-channel",
        isThread: () => true,
        send: async ({ content }: { content: string }) => {
          sentReplies.push(content);
        },
      },
    });

    assert.deepEqual(service.scorePromptReplyByMessageIdCalls, [
      {
        messageId: "prompt-message-1",
        rawReply: "Use BFS level by level.",
      },
    ]);
    assert.equal(sentReplies.length, 1);
  });
});
