import { pathToFileURL } from "node:url";

import { RecommendationDispatchClient } from "../client/index.ts";
import { runRecommendationDispatchOnce } from "../client/recommendation-dispatch.ts";
import { createLogger } from "../logger.ts";
import { createIntelligenceService, loadIntelligenceConfig } from "../service-runtime/index.ts";

const createRecommendationConfig = () => {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.RECOMMEND_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and RECOMMEND_DISCORD_CHANNEL_ID are required for recommendation mode.");
  }

  return {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.RECOMMEND_DISCORD_CHANNEL_ID,
    cronSchedule: config.INTELLIGENCE_RECOMMEND_CRON,
    topK: config.INTELLIGENCE_RECOMMEND_TOP_K,
    timezone: process.env.TZ ?? "UTC",
  };
};

export const runRecommender = async (mode: "scheduled" | "once"): Promise<void> => {
  const clientConfig = createRecommendationConfig();
  const service = await createIntelligenceService();

  if (mode === "once") {
    await runRecommendationDispatchOnce(service, {
      botToken: clientConfig.botToken,
      channelId: clientConfig.channelId,
      topK: clientConfig.topK,
    });
    return;
  }

  const client = new RecommendationDispatchClient(service, clientConfig);
  await client.start();
};

export const runRecommenderCli = async (
  scope: "recommender" | "recommender-once",
  mode: "scheduled" | "once",
): Promise<void> => {
  const logger = createLogger(scope);

  try {
    await runRecommender(mode);
  } catch (error) {
    logger.fatal({ err: error }, "unhandled error");
    process.exit(1);
  }
};

const parseMode = (value: string | undefined): "scheduled" | "once" => {
  if (value === undefined || value === "scheduled") {
    return "scheduled";
  }
  if (value === "once") {
    return "once";
  }

  throw new Error(`Unsupported recommender mode: ${value}`);
};

const isMainModule = process.argv[1] !== undefined && import.meta.url === pathToFileURL(process.argv[1]).href;

if (isMainModule) {
  const mode = parseMode(process.argv[2]);
  const scope = mode === "once" ? "recommender-once" : "recommender";
  await runRecommenderCli(scope, mode);
}
