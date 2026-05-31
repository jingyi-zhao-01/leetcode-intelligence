import type { IntelligenceService } from "../service-runtime/index.ts";
import { createLogger } from "../logger.ts";
import type {
  InteractivePromptClient,
  PromptDispatchFailure,
  PromptDispatchOutcome,
  PromptDispatchSuccess,
  PromptRenderClient,
  PromptReplyOutcome,
} from "./contracts.ts";

const logger = createLogger("client/prompt-flow");

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
  client: PromptRenderClient,
  triggerSource: string,
): Promise<PromptDispatchOutcome> {
  const result = await service.triggerPrompt(triggerSource, { channelId: client.channelId });

  if (isPromptDispatchFailure(result)) {
    logger.warn({ channelId: client.channelId, triggerSource, message: result.message }, "prompt generation skipped");
    return result;
  }

  if (!isPromptDispatchSuccess(result)) {
    throw new Error("Unexpected prompt result shape.");
  }

  const delivery = await client.renderPrompt(result);
  if (delivery.messageId) {
    await service.attachPromptMessage(result.promptEventId, delivery.messageId);
    logger.info(
      {
        channelId: client.channelId,
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

export async function runInteractivePromptSession(
  service: IntelligenceService,
  client: InteractivePromptClient,
  triggerSource: string,
  replyQuestion?: string,
): Promise<
  | PromptDispatchFailure
  | {
      ok: true;
      prompt: PromptDispatchOutcome & { ok: true };
      rawReply: string;
      scored: PromptReplyOutcome;
    }
> {
  const prompt = await dispatchPrompt(service, client, triggerSource);
  if (prompt.ok !== true) {
    return prompt;
  }

  const rawReply = await client.requestReply(replyQuestion);
  const scored = await scorePromptReply(service, {
    promptEventId: prompt.promptEventId,
    rawReply,
  });

  return {
    ok: true,
    prompt,
    rawReply,
    scored,
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
