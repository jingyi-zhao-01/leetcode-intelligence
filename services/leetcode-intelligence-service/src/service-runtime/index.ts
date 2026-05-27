import { loadIntelligenceConfig } from "../core/env.ts";
import { createRuntimeComposition } from "./composition.ts";
import { DatabaseBoundIntelligenceService } from "./database-boundary.ts";
import { IntelligenceRuntimeService } from "./intelligence-runtime.ts";

export type { IntelligenceService } from "./contracts.ts";
export type { DomainServices, ExternalServices, PersistenceServices, RuntimeComposition } from "./composition.ts";
export { loadIntelligenceConfig } from "../core/env.ts";

export const createIntelligenceService = async () => {
  const config = loadIntelligenceConfig();
  const composition = createRuntimeComposition(config);
  const runtime = new IntelligenceRuntimeService(composition, config);
  return new DatabaseBoundIntelligenceService(runtime, composition.persistence);
};
