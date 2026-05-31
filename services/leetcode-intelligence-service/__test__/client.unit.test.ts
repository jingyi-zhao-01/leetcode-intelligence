import assert from "node:assert/strict";
import { afterEach, describe, it } from "vitest";

import { ChannelType, Client, GatewayIntentBits } from "discord.js";

import { CliClient } from "../src/client/cli-client.ts";
import { DiscordClient } from "../src/client/discord-client.ts";
import { dispatchPrompt, runInteractivePromptSession, scorePromptReply } from "../src/client/prompt-flow.ts";
import { PromptResponseClient } from "../src/client/prompt-response.ts";
import { dispatchRecommendation, splitRenderedMessage } from "../src/client/recommendation-flow.ts";

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
let stubChannelType = ChannelType.GuildText;
let stubIsTextBased = true;

const resetStubs = (): void => {
  Client.prototype.login = originalLogin;
  Client.prototype.isReady = originalIsReady;
  Client.prototype.destroy = originalDestroy;
  sentMessages = [];
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
          return { id: messageId };
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
          renderPrompt: async (prompt) => {
            sentPromptBodies.push(prompt.promptText);
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
          renderPrompt: async (prompt) => {
            sentPromptBodies.push(prompt.promptText);
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

  it("runInteractivePromptSession reuses the shared prompt lifecycle for cli clients", async () => {
    const service = createFakePromptService();
    const originalWrite = process.stdout.write.bind(process.stdout);
    const writes: string[] = [];

    process.stdout.write = ((chunk: string | Uint8Array) => {
      writes.push(typeof chunk === "string" ? chunk : Buffer.from(chunk).toString("utf8"));
      return true;
    }) as typeof process.stdout.write;

    try {
      const client = new CliClient();
      client.requestReply = async () => "Use a hash map.";

      const result = await runInteractivePromptSession(service as never, client, "cli");

      assert.equal(result.ok, true);
      assert.deepEqual(service.scorePromptReplyCalls, [
        {
          promptEventId: "prompt-event-1",
          rawReply: "Use a hash map.",
        },
      ]);
      assert.match(writes.join(""), /Question: two-sum/);
      assert.match(writes.join(""), /Solve two-sum/);
    } finally {
      process.stdout.write = originalWrite;
    }
  });
});

describe("DiscordClient", () => {
  it("renderPrompt sends content to the configured text channel", async () => {
    installDiscordStub();
    const client = new DiscordClient({
      scope: "client/test",
      botToken: "bot-token",
      channelId: "prompt-channel",
      intents: [GatewayIntentBits.Guilds],
    });

    await client.start({ waitUntilReady: true });
    const delivery = await client.renderPrompt({
      ok: true,
      promptEventId: "prompt-event-1",
      promptText: "Solve two-sum",
    });
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
  });

  it("renderText sends plain content to the configured text channel", async () => {
    installDiscordStub();
    const client = new DiscordClient({
      scope: "client/test",
      botToken: "bot-token",
      channelId: "prompt-channel",
      intents: [GatewayIntentBits.Guilds],
    });

    await client.start({ waitUntilReady: true });
    const delivery = await client.renderText("plain message");
    await client.stop();

    assert.deepEqual(delivery, { messageId: "message-1" });
    assert.deepEqual(sentMessages, [
      {
        channelId: "prompt-channel",
        content: "plain message",
        embeds: undefined,
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
  it("scores direct replies in the prompt channel", async () => {
    const service = createFakePromptService();
    const client = new PromptResponseClient(service as never, {
      botToken: "bot-token",
      channelId: "prompt-channel",
    });

    const sentReplies: string[] = [];
    (client as any).discord = {
      ensureTargetChannel: async () => undefined,
      replyToMessage: async (_message: unknown, content: string) => {
        sentReplies.push(content);
        return { messageId: "feedback-1" };
      },
      stop: async () => undefined,
      start: async () => undefined,
    };

    await (client as any).handleMessage({
      id: "user-message-1",
      content: "Use BFS level by level.",
      author: { id: "user-1", bot: false },
      reference: { messageId: "prompt-message-1" },
      channel: {
        id: "prompt-channel",
        isThread: () => false,
      },
    });

    assert.deepEqual(service.scorePromptReplyByMessageIdCalls, [
      {
        messageId: "prompt-message-1",
        rawReply: "Use BFS level by level.",
      },
    ]);
    assert.equal(sentReplies.length, 1);
    assert.match(sentReplies[0] ?? "", /Score: 0.91/);
  });

  it("ignores thread messages that are not direct replies", async () => {
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

    assert.deepEqual(service.scorePromptReplyByMessageIdCalls, []);
    assert.equal(sentReplies.length, 0);
  });
});

describe("recommendation-flow", () => {
  it("dispatchRecommendation uses the shared text render client", async () => {
    const service = createFakePromptService() as FakePromptService & {
      recommendFocus: (topK: number) => Promise<Record<string, unknown>>;
      recommendFocusCalls: number[];
    };
    service.recommendFocusCalls = [];
    service.recommendFocus = async (topK: number) => {
      service.recommendFocusCalls.push(topK);
      return {
        generatedAt: "2026-05-31T00:00:00.000Z",
        lookbackDays: 14,
        narrative: "Practice array problems first.",
        recommendations: [
          {
            questionSlug: "two-sum",
            title: "Two Sum",
            difficulty: "Easy",
            priority: 0.91,
            signals: {
              weight: 0.75,
              failureRate: 0.5,
              stalenessDays: 3,
              promptCount: 1,
              avgScore: 0.82,
              recentAttemptCount: 2,
              recentFailureStreak: 1,
              recentSubmissionDays: 1.5,
            },
            reason: "High leverage refresher.",
          },
        ],
      };
    };

    const rendered: string[] = [];
    const result = await dispatchRecommendation(
      service as never,
      {
        channelId: "cli",
        renderText: async (content) => {
          rendered.push(content);
          return {};
        },
      },
      3,
    );

    assert.deepEqual(service.recommendFocusCalls, [3]);
    assert.equal(result.deliveries.length, 1);
    assert.match(rendered[0] ?? "", /## Focus Recommendation/);
    assert.match(rendered[0] ?? "", /Two Sum/);
    assert.match(rendered[0] ?? "", /High leverage refresher/);
  });

  it("splitRenderedMessage preserves recommendation boundaries when chunking", () => {
    const body = ["## Focus Recommendation", "", "### 1. **Two Sum**", "x".repeat(1940), "### 2. **Three Sum**"].join(
      "\n",
    );

    const chunks = splitRenderedMessage(body, 2000);

    assert.equal(chunks.length, 2);
    assert.match(chunks[0] ?? "", /### 1\. \*\*Two Sum\*\*/);
    assert.match(chunks[1] ?? "", /### 2\. \*\*Three Sum\*\*/);
  });
});
