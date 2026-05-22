import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

import type { IntelligenceService } from "../intelligence.ts";

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
      console.error(result.message);
      return;
    }

    if (!isCliPromptResult(result)) {
      throw new Error("Unexpected prompt result shape.");
    }

    console.log(`Question: ${result.questionSlug}`);
    console.log("");
    console.log(result.promptText);

    const rl = readline.createInterface({ input, output });
    const reply = await rl.question("\nYour reply: ");
    rl.close();

    const scored = await service.scorePromptReply(result.promptEventId, reply);
    console.log(JSON.stringify(scored, null, 2));
  } finally {
    await service.stop();
  }
}
