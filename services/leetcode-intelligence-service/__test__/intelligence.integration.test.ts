import assert from 'node:assert/strict';
import { afterEach, describe, it } from 'vitest';

import cron from 'node-cron';
import { ChannelType, Client } from 'discord.js';

import { PromptDispatchClient, runPromptDispatchOnce } from '../src/client/prompt-dispatch.ts';
import { RecommendationDispatchClient, runRecommendationDispatchOnce } from '../src/client/recommendation-dispatch.ts';

type PromptResult = {
  ok: true;
  promptEventId: string;
  promptText: string;
};

type RecommendationResult = {
  narrative: string;
  recommendations: Array<{
    questionSlug: string;
    title: string;
    difficulty: string;
    priority: number;
    signals: {
      weight: number;
      failureRate: number;
      stalenessDays: number;
      promptCount: number;
      avgScore: number | null;
      recentAttemptCount: number;
      recentFailureStreak: number;
      recentSubmissionDays: number | null;
    };
    reason: string;
  }>;
};

type FakeService = {
  startCalls: number;
  stopCalls: number;
  triggerPromptCalls: Array<{ triggerSource: string; transport: { channelId: string } }>;
  attachPromptMessageCalls: Array<{ promptEventId: string; messageId: string }>;
  recommendFocusCalls: number[];
  start: () => Promise<void>;
  stop: () => Promise<void>;
  triggerPrompt: (triggerSource: string, transport: { channelId: string }) => Promise<PromptResult>;
  attachPromptMessage: (promptEventId: string, messageId: string) => Promise<void>;
  recommendFocus: (topK: number) => Promise<RecommendationResult>;
};

const originalSchedule = cron.schedule;
const originalLogin = Client.prototype.login;
const originalIsReady = Client.prototype.isReady;
const originalDestroy = Client.prototype.destroy;

let scheduleCalls = 0;
let sentMessages: Array<{
  channelId: string;
  content?: string;
  embeds?: unknown[];
}> = [];

const resetStubs = (): void => {
  cron.schedule = originalSchedule;
  Client.prototype.login = originalLogin;
  Client.prototype.isReady = originalIsReady;
  Client.prototype.destroy = originalDestroy;
  scheduleCalls = 0;
  sentMessages = [];
};

const installCronStub = (): void => {
  cron.schedule = ((..._args: unknown[]) => {
    scheduleCalls += 1;
    return {
      stop() {
        return undefined;
      },
    };
  }) as typeof cron.schedule;
};

const installDiscordStub = (): void => {
  Client.prototype.login = async function loginStub(this: Client) {
    (this as Client & { channels: { fetch: (channelId: string) => Promise<unknown> } }).channels = {
      fetch: async (channelId: string) => ({
        type: ChannelType.GuildText,
        isTextBased: () => true,
        send: async ({ content, embeds }: { content?: string; embeds?: Array<{ toJSON?: () => unknown }> }) => {
          const messageId = `message-${sentMessages.length + 1}`;
          sentMessages.push({
            channelId,
            content,
            embeds: Array.isArray(embeds)
              ? embeds.map((embed) => (typeof embed?.toJSON === 'function' ? embed.toJSON() : embed))
              : undefined,
          });
          return { id: messageId };
        },
      }),
    };
    this.emit('clientReady', this);
    return 'stub-token';
  } as typeof Client.prototype.login;

  Client.prototype.isReady = (() => true) as typeof Client.prototype.isReady;
  Client.prototype.destroy = (async () => undefined) as typeof Client.prototype.destroy;
};

const createFakeService = (): FakeService => {
  const service: FakeService = {
    startCalls: 0,
    stopCalls: 0,
    triggerPromptCalls: [],
    attachPromptMessageCalls: [],
    recommendFocusCalls: [],
    start: async () => {
      service.startCalls += 1;
    },
    stop: async () => {
      service.stopCalls += 1;
    },
    triggerPrompt: async (triggerSource, transport) => {
      service.triggerPromptCalls.push({ triggerSource, transport });
      return {
        ok: true,
        promptEventId: 'prompt-event-1',
        promptText: 'Solve two-sum',
      };
    },
    attachPromptMessage: async (promptEventId, messageId) => {
      service.attachPromptMessageCalls.push({ promptEventId, messageId });
    },
    recommendFocus: async (topK) => {
      service.recommendFocusCalls.push(topK);
      return {
        narrative: 'Focus on array review first.',
        recommendations: [
          {
            questionSlug: 'two-sum',
            title: 'Two Sum',
            difficulty: 'Easy',
            priority: 1.25,
            signals: {
              weight: 1.25,
              failureRate: 0,
              stalenessDays: 2,
              promptCount: 1,
              avgScore: 4,
              recentAttemptCount: 3,
              recentFailureStreak: 1,
              recentSubmissionDays: 0.5,
            },
            reason: 'weight=1.25',
          },
        ],
      };
    },
  };

  return service;
};

afterEach(() => {
  resetStubs();
});

describe('intelligence integration modes', () => {
  it('runPromptDispatchOnce sends one prompt and never schedules node-cron', async () => {
    installCronStub();
    installDiscordStub();
    const service = createFakeService();

    await runPromptDispatchOnce(service as never, {
      botToken: 'bot-token',
      channelId: 'prompt-channel',
    });

    assert.equal(service.startCalls, 1);
    assert.equal(service.stopCalls, 1);
    assert.deepEqual(service.triggerPromptCalls, [
      {
        triggerSource: 'scheduled-once',
        transport: { channelId: 'prompt-channel' },
      },
    ]);
    assert.deepEqual(service.attachPromptMessageCalls, [
      {
        promptEventId: 'prompt-event-1',
        messageId: 'message-1',
      },
    ]);
    assert.equal(scheduleCalls, 0);
    assert.deepEqual(sentMessages, [
      {
        channelId: 'prompt-channel',
        content: undefined,
        embeds: [
          {
            color: 5793266,
            title: 'Solve two-sum',
            description: 'Solve two-sum',
          },
        ],
      },
    ]);
  });

  it('PromptDispatchClient schedules node-cron in long-running mode', async () => {
    installCronStub();
    installDiscordStub();
    const service = createFakeService();
    const client = new PromptDispatchClient(service as never, {
      botToken: 'bot-token',
      channelId: 'prompt-channel',
      cronSchedule: '*/2 * * * *',
      timezone: 'UTC',
    });

    await client.start();
    await client.stop();

    assert.equal(scheduleCalls, 1);
    assert.equal(service.startCalls, 1);
    assert.equal(service.stopCalls, 1);
  });

  it('runRecommendationDispatchOnce sends one recommendation message and never schedules node-cron', async () => {
    installCronStub();
    installDiscordStub();
    const service = createFakeService();

    await runRecommendationDispatchOnce(service as never, {
      botToken: 'bot-token',
      channelId: 'recommend-channel',
      topK: 3,
    });

    assert.equal(service.startCalls, 1);
    assert.equal(service.stopCalls, 1);
    assert.deepEqual(service.recommendFocusCalls, [3]);
    assert.equal(scheduleCalls, 0);
    assert.equal(sentMessages.length, 1);
    assert.equal(sentMessages[0]?.channelId, 'recommend-channel');
    assert.match(sentMessages[0]?.content ?? '', /## Focus Recommendation/);
    assert.match(sentMessages[0]?.content ?? '', /\*\*Summary\*\*/);
    assert.match(sentMessages[0]?.content ?? '', /\*\*Recommended Problems\*\*/);
    assert.match(sentMessages[0]?.content ?? '', /### 1\. \*\*Two Sum\*\*/);
    assert.match(sentMessages[0]?.content ?? '', /`two-sum`/);
    assert.match(sentMessages[0]?.content ?? '', /Recent submissions/);
  });

  it('RecommendationDispatchClient schedules node-cron in long-running mode', async () => {
    installCronStub();
    installDiscordStub();
    const service = createFakeService();
    const client = new RecommendationDispatchClient(service as never, {
      botToken: 'bot-token',
      channelId: 'recommend-channel',
      cronSchedule: '0 19 * * *',
      topK: 5,
      timezone: 'UTC',
    });

    await client.start();
    await client.stop();

    assert.equal(scheduleCalls, 1);
    assert.equal(service.startCalls, 1);
    assert.equal(service.stopCalls, 1);
  });
});
