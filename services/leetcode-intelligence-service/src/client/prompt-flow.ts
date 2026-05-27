import type { IntelligenceService } from "../service-runtime/index.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("client/prompt-flow");

export type PromptDispatchFailure = {
  ok: false;
  message: string;
};

export type PromptDispatchSuccess = {
  ok: true;
  promptEventId: string;
  promptText: string;
  questionSlug?: string;
  submissionId?: string;
  weightBefore?: number;
};

export type PromptDispatchOutcome = PromptDispatchFailure | (PromptDispatchSuccess & { messageId?: string });

export type PromptReplyOutcome = Record<string, unknown> | null;

export type PromptDispatchTransport = {
  channelId: string;
  sendPrompt: (promptText: string) => Promise<{ messageId?: string }>;
};

export type PromptReplyRequest =
  | {
      promptEventId: string;
      rawReply: string;
    }
  | {
      referenceMessageId: string;
      rawReply: string;
    };

function isPromptDispatchSuccess(result: Record<string, unknown>): result is PromptDispatchSuccess {
  return result.ok === true && typeof result.promptEventId === "string" && typeof result.promptText === "string";
}

function isPromptDispatchFailure(result: Record<string, unknown>): result is PromptDispatchFailure {
  return result.ok === false && typeof result.message === "string";
}

export async function dispatchPrompt(
  service: IntelligenceService,
  transport: PromptDispatchTransport,
  triggerSource: string,
): Promise<PromptDispatchOutcome> {
  const result = await service.triggerPrompt(triggerSource, { channelId: transport.channelId });

  if (isPromptDispatchFailure(result)) {
    logger.warn({ channelId: transport.channelId, triggerSource, message: result.message }, "prompt generation skipped");
    return result;
  }

  if (!isPromptDispatchSuccess(result)) {
    throw new Error("Unexpected prompt result shape.");
  }

  const delivery = await transport.sendPrompt(result.promptText);
  if (delivery.messageId) {
    await service.attachPromptMessage(result.promptEventId, delivery.messageId);
    logger.info(
      {
        channelId: transport.channelId,
        messageId: delivery.messageId,
        promptEventId: result.promptEventId,
      },
      "linked prompt message",
    );
  }

  return {
    ...result,
    messageId: delivery.messageId,
  };
}

export async function scorePromptReply(
  service: IntelligenceService,
  request: PromptReplyRequest,
): Promise<PromptReplyOutcome> {
  if ("promptEventId" in request) {
    return service.scorePromptReply(request.promptEventId, request.rawReply);
  }

  return service.scorePromptReplyByMessageId(request.referenceMessageId, request.rawReply);
}
