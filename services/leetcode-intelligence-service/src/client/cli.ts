import type { IntelligenceService } from "../core.ts";
import { createLogger } from "../logger.ts";
import { CliClient } from "./cli-client.ts";
import { dispatchPrompt, scorePromptReply } from "./prompt-flow.ts";

const logger = createLogger("client/cli");

export async function runCliIntelligenceClient(service: IntelligenceService): Promise<void> {
  const client = new CliClient();
  await service.start();

  try {
    const result = await dispatchPrompt(service, client, "cli");
    if (result.ok !== true) {
      logger.error({ message: result.message }, "prompt generation failed");
      return;
    }

    const promptBody = result.questionSlug ? `Question: ${result.questionSlug}\n\n${result.promptText}\n` : `${result.promptText}\n`;
    process.stdout.write(promptBody);
    const reply = await client.promptReply();
    const scored = await scorePromptReply(service, {
      promptEventId: result.promptEventId,
      rawReply: reply,
    });
    process.stdout.write(`${JSON.stringify(scored, null, 2)}\n`);
  } finally {
    await service.stop();
  }
}
