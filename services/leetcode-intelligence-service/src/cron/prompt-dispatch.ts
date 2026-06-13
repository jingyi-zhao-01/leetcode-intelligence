import { pathToFileURL } from "node:url";

import { PromptDispatchClient } from "../client/index.ts";
import { runPromptDispatchOnce } from "../client/prompt-dispatch.ts";
import { createLogger } from "../logger.ts";
import { createIntelligenceService, loadIntelligenceConfig } from "../service-runtime/index.ts";

const createPromptDispatchConfig = () => {
  const config = loadIntelligenceConfig();
  if (!config.DISCORD_BOT_TOKEN || !config.PROMPT_DISCORD_CHANNEL_ID) {
    throw new Error("DISCORD_BOT_TOKEN and PROMPT_DISCORD_CHANNEL_ID are required for prompt dispatch mode.");
  }

  return {
    botToken: config.DISCORD_BOT_TOKEN,
    channelId: config.PROMPT_DISCORD_CHANNEL_ID,
    cronSchedule: config.INTELLIGENCE_PROMPT_CRON,
    timezone: process.env.TZ ?? "UTC",
  };
};

export const runPromptDispatchCli = async (
  scope: "prompt-dispatch" | "prompt-dispatch-once",
  mode: "scheduled" | "once",
): Promise<void> => {
  const logger = createLogger(scope);

  try {
    const clientConfig = createPromptDispatchConfig();
    const service = await createIntelligenceService();

    if (mode === "once") {
      await runPromptDispatchOnce(service, {
        botToken: clientConfig.botToken,
        channelId: clientConfig.channelId,
      });
      return;
    }

    const client = new PromptDispatchClient(service, clientConfig);
    await client.start();
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

  throw new Error(`Unsupported prompt dispatch mode: ${value}`);
};

const isMainModule = process.argv[1] !== undefined && import.meta.url === pathToFileURL(process.argv[1]).href;

if (isMainModule) {
  const mode = parseMode(process.argv[2]);
  const scope = mode === "once" ? "prompt-dispatch-once" : "prompt-dispatch";
  await runPromptDispatchCli(scope, mode);
}
