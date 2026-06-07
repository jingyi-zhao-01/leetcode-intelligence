import { OpenRouter } from "@openrouter/sdk";

export type CompanionChatMessage = {
  role: "system" | "user" | "assistant";
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

export type CompanionChatService = {
  chat(request: CompanionChatRequest): Promise<CompanionChatResult>;
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
- Match the user's language when practical.
`.trim();

const toText = (value: unknown): string => (typeof value === "string" ? value : "");

export function sanitizeCompanionMessages(messages: unknown): CompanionChatMessage[] {
  if (!Array.isArray(messages)) {
    return [];
  }

  return messages.flatMap((message) => {
    if (!message || typeof message !== "object" || Array.isArray(message)) {
      return [];
    }

    const role = (message as { role?: unknown }).role;
    const content = toText((message as { content?: unknown }).content).trim();
    if ((role !== "system" && role !== "user" && role !== "assistant") || content.length === 0) {
      return [];
    }

    return [{ role, content }];
  });
}

function buildChatMessages(systemPrompt: string, messages: CompanionChatMessage[]): CompanionChatMessage[] {
  const nonSystemMessages = messages.filter((message) => message.role !== "system");

  return [
    {
      role: "system",
      content: systemPrompt,
    },
    ...nonSystemMessages,
  ];
}

class DefaultCompanionChatService implements CompanionChatService {
  constructor(
    private readonly openRouter: OpenRouter,
    private readonly defaultModel: string,
    private readonly systemPrompt: string,
  ) {}

  async chat(request: CompanionChatRequest): Promise<CompanionChatResult> {
    const messages = sanitizeCompanionMessages(request.messages);
    if (messages.length === 0) {
      throw new Error("At least one user or assistant message is required.");
    }

    const model = request.model?.trim() || this.defaultModel;
    const temperature = Number.isFinite(request.temperature) ? request.temperature : 0.2;

    const response = await this.openRouter.chat.send({
      chatRequest: {
        model,
        temperature,
        messages: buildChatMessages(this.systemPrompt, messages),
      },
    });

    return {
      model,
      content: response.choices?.[0]?.message?.content ?? "",
      finishReason: response.choices?.[0]?.finishReason ?? null,
      usage: response.usage
        ? {
            prompt_tokens: response.usage.promptTokens,
            completion_tokens: response.usage.completionTokens,
            total_tokens: response.usage.totalTokens,
          }
        : undefined,
    };
  }
}

export const createDefaultCompanionChatService = (
  openRouter: OpenRouter,
  model: string,
  systemPrompt = process.env.LEETCODE_COMPANION_SYSTEM_PROMPT ?? DEFAULT_COMPANION_SYSTEM_PROMPT,
): CompanionChatService => {
  return new DefaultCompanionChatService(openRouter, model, systemPrompt);
};
