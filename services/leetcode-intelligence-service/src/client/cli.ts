import type { IntelligenceService } from "../service-runtime/index.ts";
import { createLogger } from "../logger.ts";
import { CliClient } from "./cli-client.ts";
import { runInteractivePromptSession } from "./prompt-flow.ts";

const logger = createLogger("client/cli");

export async function runCliIntelligenceClient(service: IntelligenceService): Promise<void> {
  const client = new CliClient();
  await service.start();

  try {
    const session = await runInteractivePromptSession(service, client, "cli");
    if (session.ok !== true) {
      logger.error({ message: session.message }, "prompt generation failed");
      return;
    }

    process.stdout.write(`${JSON.stringify(session.scored, null, 2)}\n`);
  } finally {
    await service.stop();
  }
}
