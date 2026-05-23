import { runRecommendationDispatchOnce } from "./client/recommendation-dispatch.ts";
import { createIntelligenceService } from "./intelligence.ts";
import { loadIntelligenceConfig } from "./intelligence/env.ts";
import { createLogger } from "./logger.ts";

const logger = createLogger("recommender-once");

async function main(): Promise<void> {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.RECOMMEND_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and RECOMMEND_DISCORD_CHANNEL_ID are required for one-shot recommendation mode.");
  }

  const service = await createIntelligenceService();
  await runRecommendationDispatchOnce(service, {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.RECOMMEND_DISCORD_CHANNEL_ID,
    topK: config.INTELLIGENCE_RECOMMEND_TOP_K,
  });
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled error");
  process.exit(1);
}
