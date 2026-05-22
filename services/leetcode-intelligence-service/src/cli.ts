import { createIntelligenceService } from "./intelligence.ts";
import { createLogger } from "./logger.ts";
import { runCliIntelligenceClient } from "./client/index.ts";

const logger = createLogger("cli");

async function main(): Promise<void> {
  const service = await createIntelligenceService();
  await runCliIntelligenceClient(service);
}

try {
  await main();
} catch (error) {
  logger.fatal({ err: error }, "unhandled error");
  process.exit(1);
}
