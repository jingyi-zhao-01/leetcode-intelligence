import path from "node:path";

import { config as loadDotenv } from "dotenv";
import { z } from "zod";

import type { IntelligenceConfig } from "./types.ts";

loadDotenv({ path: path.resolve(process.cwd(), ".env") });

export const envSchema = z.object({
  DATABASE_URL: z.string().min(1),
  OPEN_ROUTER_API_KEY: z.string().min(1).optional(),
  DISCORD_BOT_TOKEN: z.string().min(1).optional(),
  PROMPT_DISCORD_CHANNEL_ID: z.string().min(1).optional(),
  RECOMMEND_DISCORD_CHANNEL_ID: z.string().min(1).optional(),
  MODEL: z.string().min(1).default("openai/gpt-4o-mini"),
  INTELLIGENCE_PORT: z.coerce.number().int().positive().default(8030),
  INTELLIGENCE_HOST: z.string().min(1).default("0.0.0.0"),
  INTELLIGENCE_PROMPT_CRON: z.string().min(1).optional(),
  INTELLIGENCE_RECOMMEND_CRON: z.string().min(1).default("0 20 * * *"),
  INTELLIGENCE_RECOMMEND_TOP_K: z.coerce.number().int().positive().default(10),
  INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS: z.coerce.number().int().positive().default(30),
  INTELLIGENCE_MAX_CANDIDATES: z.coerce.number().int().positive().default(500),
  INTELLIGENCE_SELECTION_WINDOW: z.coerce.number().int().positive().default(200),
  INTELLIGENCE_MIN_WEIGHT: z.coerce.number().positive().default(0.25),
  INTELLIGENCE_MAX_WEIGHT: z.coerce.number().positive().default(5),
});

export const loadIntelligenceConfig = (): IntelligenceConfig => {
  const parsed = envSchema.safeParse(process.env);
  if (!parsed.success) {
    const issues = parsed.error.issues.map((issue) => `${issue.path.join(".")}: ${issue.message}`).join("; ");
    throw new Error(`Invalid intelligence service environment: ${issues}`);
  }

  return {
    ...parsed.data,
    INTELLIGENCE_PROMPT_CRON: parsed.data.INTELLIGENCE_PROMPT_CRON ?? "0 9 * * *",
  };
};
