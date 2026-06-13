import type { ApiContext } from "./context.ts";
import { createReadModelsApi } from "./read-models.ts";
import { createTagMutationsApi } from "./tag-mutations.ts";
import { createTemplateBenchmarkApi } from "./template-benchmark.ts";
import { createTemplateGenerationApi } from "./template-generation.ts";

export * from "./types.ts";
export type { ApiContext } from "./context.ts";

export function createBffApi(context: ApiContext) {
  return {
    ...createReadModelsApi(context),
    ...createTemplateBenchmarkApi(context),
    ...createTemplateGenerationApi(context),
    ...createTagMutationsApi(context),
  };
}
