import { createIntelligenceService, loadIntelligenceConfig } from "./service-runtime/index.ts";
import { createLogger } from "./logger.ts";
import { RecommendationDispatchClient } from "./client/index.ts";

const logger = createLogger("recommender");

const main = async (): Promise<void> => {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.RECOMMEND_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and RECOMMEND_DISCORD_CHANNEL_ID are required for recommendation mode.");
  }

  const service = await createIntelligenceService();
  const client = new RecommendationDispatchClient(service, {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.RECOMMEND_DISCORD_CHANNEL_ID,
    cronSchedule: config.INTELLIGENCE_RECOMMEND_CRON,
    topK: config.INTELLIGENCE_RECOMMEND_TOP_K,
    timezone: process.env.TZ ?? "UTC",
  });

  await client.start();
};

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled error");
  process.exit(1);
}
