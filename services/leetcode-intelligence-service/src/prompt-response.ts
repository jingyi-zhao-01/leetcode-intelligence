import { createIntelligenceService } from "./intelligence.ts";
import { loadIntelligenceConfig } from "./intelligence/env.ts";
import { PromptResponseClient } from "./client/index.ts";

async function main(): Promise<void> {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.PROMPT_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and PROMPT_DISCORD_CHANNEL_ID are required for prompt response mode.");
  }

  const service = await createIntelligenceService();
  const client = new PromptResponseClient(service, {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.PROMPT_DISCORD_CHANNEL_ID,
  });

  await client.start();
}

try {
  await main();
} catch (error) {
  console.error(error);
  process.exit(1);
}
