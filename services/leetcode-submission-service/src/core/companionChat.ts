import { Agent, OpenAIProvider, Runner, assistant, user, type AgentInputItem } from '@openai/agents';
import OpenAI from 'openai';
import { createLogger } from '../logger.ts';

export type CompanionChatMessage = {
  role: 'system' | 'user' | 'assistant';
  content: string;
};

export type CompanionChatRequest = {
  messages: CompanionChatMessage[];
  model?: string;
  temperature?: number;
};

export type CompanionChatResult = {
  model: string;
  content: string;
  finishReason: string | null;
  usage?: Record<string, number | null | undefined>;
};

export type CompanionChatStreamChunk = {
  id: string;
  object: string;
  created: number;
  model: string;
  choices: Array<{
    index: number;
    finishReason: string | null;
    logprobs?: unknown;
    delta: {
      role?: string;
      content?: string | null;
      refusal?: string | null;
      reasoning?: string | null;
      toolCalls?: Array<{
        index?: number;
        id?: string;
        type?: string;
        function?: {
          name?: string;
          arguments?: string;
        };
      }>;
    };
  }>;
  usage?: {
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
  };
};

export type CompanionChatService = {
  chat(request: CompanionChatRequest): Promise<CompanionChatResult>;
  stream(request: CompanionChatRequest): Promise<AsyncIterable<CompanionChatStreamChunk>>;
};

const DEFAULT_COMPANION_SYSTEM_PROMPT = `
You are LeetCode Companion, the LLM runtime owned by leetcode-submission-service.

You help the user reason about LeetCode problems using the context provided from the editor.
Prioritize:
- explaining the current bug or gap clearly
- giving the next concrete step
- preserving the user's current approach when reasonable

Rules:
- Be honest about uncertainty.
- Prefer hints and diagnosis over dumping a full solution unless the user explicitly asks for it.
- When code is provided, reason from that code instead of giving a generic answer.
- Keep answers concise but useful.
- Default to answering in Simplified Chinese.
- If the user explicitly asks for another language, follow the user's request.
`.trim();

const logger = createLogger('companion-chat');

const toText = (value: unknown): string => (typeof value === 'string' ? value : '');

export function sanitizeCompanionMessages(messages: unknown): CompanionChatMessage[] {
  if (!Array.isArray(messages)) {
    return [];
  }

  return messages.flatMap((message) => {
    if (!message || typeof message !== 'object' || Array.isArray(message)) {
      return [];
    }

    const role = (message as { role?: unknown }).role;
    const content = toText((message as { content?: unknown }).content).trim();
    if ((role !== 'system' && role !== 'user' && role !== 'assistant') || content.length === 0) {
      return [];
    }

    return [{ role, content }];
  });
}

function toAgentInput(messages: CompanionChatMessage[]): AgentInputItem[] {
  return messages
    .filter((message) => message.role !== 'system')
    .map((message) => {
      if (message.role === 'assistant') {
        return assistant(message.content);
      }

      return user(message.content);
    });
}

function extractFinalText(output: unknown): string {
  if (typeof output === 'string') {
    return output;
  }

  if (Array.isArray(output)) {
    return output
      .map((item) => {
        if (typeof item === 'string') {
          return item;
        }

        if (item && typeof item === 'object' && 'text' in item && typeof item.text === 'string') {
          return item.text;
        }

        return '';
      })
      .join('')
      .trim();
  }

  if (output && typeof output === 'object' && 'text' in output && typeof output.text === 'string') {
    return output.text;
  }

  return '';
}

function summarizeMessages(
  messages: CompanionChatMessage[],
): Array<{ role: CompanionChatMessage['role']; chars: number; preview: string }> {
  return messages.map((message) => ({
    role: message.role,
    chars: message.content.length,
    preview: message.content.slice(0, 160),
  }));
}

class AgentsSdkCompanionChatService implements CompanionChatService {
  private readonly openaiClient: OpenAI;
  private readonly modelProvider: OpenAIProvider;

  constructor(
    private readonly apiKey: string,
    private readonly defaultModel: string,
    private readonly systemPrompt: string,
    private readonly baseUrl: string,
    private readonly appTitle: string,
    private readonly httpReferer: string,
  ) {
    this.openaiClient = new OpenAI({
      apiKey: this.apiKey,
      baseURL: this.baseUrl,
      defaultHeaders: {
        'HTTP-Referer': this.httpReferer,
        'X-Title': this.appTitle,
      },
    });
    this.modelProvider = new OpenAIProvider({
      // The Agents SDK and this workspace resolve the OpenAI client type through
      // slightly different module paths, but they are the same runtime client.
      openAIClient: this.openaiClient as never,
      useResponses: false,
    });
  }

  private createAgent(request: CompanionChatRequest): Agent {
    const model = request.model?.trim() || this.defaultModel;

    return new Agent({
      name: 'LeetCode Companion',
      instructions: this.systemPrompt,
      model,
    });
  }

  async chat(request: CompanionChatRequest): Promise<CompanionChatResult> {
    const messages = sanitizeCompanionMessages(request.messages);
    if (messages.length === 0) {
      throw new Error('At least one user or assistant message is required.');
    }

    const model = request.model?.trim() || this.defaultModel;
    const temperature = Number.isFinite(request.temperature) ? request.temperature : 0.2;
    const agent = this.createAgent(request);
    const startedAt = Date.now();

    logger.info(
      {
        model,
        stream: false,
        messageCount: messages.length,
        messages: summarizeMessages(messages),
      },
      'Companion chat request started',
    );

    const runner = new Runner({
      modelProvider: this.modelProvider,
      modelSettings: {
        temperature,
      },
      tracingDisabled: true,
      workflowName: 'companion-service',
    });

    const result = await runner.run(agent, toAgentInput(messages), {
      maxTurns: 1,
    });

    const content = extractFinalText(result.finalOutput);

    logger.info(
      {
        model,
        stream: false,
        durationMs: Date.now() - startedAt,
        outputChars: content.length,
        outputPreview: content.slice(0, 200),
      },
      'Companion chat request completed',
    );

    return {
      model,
      content,
      finishReason: 'stop',
    };
  }

  async stream(request: CompanionChatRequest): Promise<AsyncIterable<CompanionChatStreamChunk>> {
    const messages = sanitizeCompanionMessages(request.messages);
    if (messages.length === 0) {
      throw new Error('At least one user or assistant message is required.');
    }

    const model = request.model?.trim() || this.defaultModel;
    const temperature = Number.isFinite(request.temperature) ? request.temperature : 0.2;
    const agent = this.createAgent(request);
    const startedAt = Date.now();

    logger.info(
      {
        model,
        stream: true,
        messageCount: messages.length,
        messages: summarizeMessages(messages),
      },
      'Companion chat stream started',
    );

    const runner = new Runner({
      modelProvider: this.modelProvider,
      modelSettings: {
        temperature,
      },
      tracingDisabled: true,
      workflowName: 'companion-service',
    });
    const result = await runner.run(agent, toAgentInput(messages), { maxTurns: 1, stream: true });

    const chunkId = `chatcmpl_agents_${Date.now()}`;
    const created = Math.floor(Date.now() / 1000);

    async function* iterate(): AsyncIterable<CompanionChatStreamChunk> {
      let sentRole = false;
      let outputChars = 0;
      let outputPreview = '';
      const textStream = result.toTextStream({ compatibleWithNodeStreams: true });

      for await (const piece of textStream) {
        const content = typeof piece === 'string' ? piece : String(piece ?? '');
        if (content.length === 0) {
          continue;
        }

        outputChars += content.length;
        if (outputPreview.length < 200) {
          outputPreview = (outputPreview + content).slice(0, 200);
        }

        yield {
          id: chunkId,
          object: 'chat.completion.chunk',
          created,
          model,
          choices: [
            {
              index: 0,
              finishReason: null,
              delta: {
                role: sentRole ? undefined : 'assistant',
                content,
              },
            },
          ],
        };

        sentRole = true;
      }

      await result.completed;

      logger.info(
        {
          model,
          stream: true,
          durationMs: Date.now() - startedAt,
          outputChars,
          outputPreview,
        },
        'Companion chat stream completed',
      );

      yield {
        id: chunkId,
        object: 'chat.completion.chunk',
        created,
        model,
        choices: [
          {
            index: 0,
            finishReason: 'stop',
            delta: {},
          },
        ],
      };
    }

    return iterate();
  }
}

export const createDefaultCompanionChatService = (
  apiKey: string,
  model: string,
  options?: {
    systemPrompt?: string;
    baseUrl?: string;
    appTitle?: string;
    httpReferer?: string;
  },
): CompanionChatService => {
  return new AgentsSdkCompanionChatService(
    apiKey,
    model,
    options?.systemPrompt ?? process.env.LEETCODE_COMPANION_SYSTEM_PROMPT ?? DEFAULT_COMPANION_SYSTEM_PROMPT,
    options?.baseUrl ?? process.env.OPEN_ROUTER_BASE_URL ?? 'https://openrouter.ai/api/v1',
    options?.appTitle ?? 'companion-service',
    options?.httpReferer ?? 'https://github.com/kawre/leetcode.nvim',
  );
};
