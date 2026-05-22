import { createIntelligenceService } from "./intelligence.ts";
import { createLogger } from "./logger.ts";
import { loadIntelligenceConfig } from "./intelligence/env.ts";
import { PromptDispatchClient } from "./client/index.ts";

const logger = createLogger("prompt-dispatch");

async function main(): Promise<void> {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.PROMPT_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and PROMPT_DISCORD_CHANNEL_ID are required for prompt dispatch mode.");
  }

  const service = await createIntelligenceService();
  const client = new PromptDispatchClient(service, {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.PROMPT_DISCORD_CHANNEL_ID,
    cronSchedule: config.INTELLIGENCE_PROMPT_CRON,
    timezone: process.env.TZ ?? "UTC",
  });

  await client.start();
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled error");
  process.exit(1);
}
