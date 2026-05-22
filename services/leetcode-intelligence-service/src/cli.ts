import { createIntelligenceService } from "./intelligence.js";
import { runCliIntelligenceClient } from "./client/index.js";

async function main(): Promise<void> {
  const service = await createIntelligenceService();
  await runCliIntelligenceClient(service);
}

try {
  await main();
} catch (error) {
  console.error(error);
  process.exit(1);
}
