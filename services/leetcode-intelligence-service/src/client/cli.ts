import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

import type { IntelligenceService } from "../intelligence.ts";
import { createLogger } from "../logger.ts";

const logger = createLogger("client/cli");

type CliPromptResult = {
  ok: true;
  promptEventId: string;
  promptText: string;
  questionSlug: string;
  submissionId: string;
  weightBefore: number;
};

type CliPromptFailure = {
  ok: false;
  message: string;
};

function isCliPromptResult(result: Record<string, unknown>): result is CliPromptResult {
  return result.ok === true && typeof result.promptEventId === "string" && typeof result.promptText === "string";
}

function isCliPromptFailure(result: Record<string, unknown>): result is CliPromptFailure {
  return result.ok === false && typeof result.message === "string";
}

export async function runCliIntelligenceClient(service: IntelligenceService): Promise<void> {
  await service.start();

  try {
    const result = await service.triggerPrompt("cli", { channelId: "cli" });

    if (isCliPromptFailure(result)) {
      logger.error({ message: result.message }, "prompt generation failed");
      return;
    }

    if (!isCliPromptResult(result)) {
      throw new Error("Unexpected prompt result shape.");
    }

    process.stdout.write(`Question: ${result.questionSlug}\n\n${result.promptText}\n`);

    const rl = readline.createInterface({ input, output });
    const reply = await rl.question("\nYour reply: ");
    rl.close();

    const scored = await service.scorePromptReply(result.promptEventId, reply);
    process.stdout.write(`${JSON.stringify(scored, null, 2)}\n`);
  } finally {
    await service.stop();
  }
}
