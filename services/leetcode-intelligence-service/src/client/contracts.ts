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

export type PromptDelivery = {
  messageId?: string;
};

export type TextRenderClient = {
  channelId: string;
  renderText: (content: string) => Promise<PromptDelivery>;
};

export type PromptRenderClient = {
  channelId: string;
  renderPrompt: (prompt: PromptDispatchSuccess) => Promise<PromptDelivery>;
};

export type InteractivePromptClient = PromptRenderClient & {
  requestReply: (question?: string) => Promise<string>;
};
