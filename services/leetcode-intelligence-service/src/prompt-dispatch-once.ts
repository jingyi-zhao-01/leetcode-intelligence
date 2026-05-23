import { runPromptDispatchOnce } from "./client/prompt-dispatch.ts";
import { createIntelligenceService } from "./intelligence.ts";
import { loadIntelligenceConfig } from "./intelligence/env.ts";
import { createLogger } from "./logger.ts";

const logger = createLogger("prompt-dispatch-once");

async function main(): Promise<void> {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.PROMPT_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and PROMPT_DISCORD_CHANNEL_ID are required for one-shot prompt dispatch mode.");
  }

  const service = await createIntelligenceService();
  await runPromptDispatchOnce(service, {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.PROMPT_DISCORD_CHANNEL_ID,
  });
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled error");
  process.exit(1);
}
