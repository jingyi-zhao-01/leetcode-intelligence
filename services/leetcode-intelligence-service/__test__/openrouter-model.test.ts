import path from "node:path";

import { config as loadDotenv } from "dotenv";
import { OpenRouter } from "@openrouter/sdk";

const tryLoadDotenv = (): void => {
  const candidates = [
    path.resolve(process.cwd(), ".env"),
    path.resolve(process.cwd(), "../../.env"),
    path.resolve(process.cwd(), "../../../.env"),
  ];

  for (const envPath of candidates) {
    loadDotenv({ path: envPath, override: false });
  }
};

const requireEnv = (name: string): string => {
  const value = process.env[name]?.trim();
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
};

const main = async (): Promise<void> => {
  tryLoadDotenv();

  const apiKey = requireEnv("OPEN_ROUTER_API_KEY");
  const model = requireEnv("MODEL");

  console.error(`[openrouter-test] starting model probe model=${model} keyPresent=${Boolean(apiKey)}`);

  const client = new OpenRouter({
    apiKey,
    httpReferer: "https://github.com/kawre/leetcode.nvim",
    appTitle: "leetcode-intelligence-service-openrouter-test",
  });

  const models = await client.models.list();
  const modelIds = new Set((models.data ?? []).map((item) => item.id));

  if (!modelIds.has(model)) {
    const alternatives = [...modelIds].filter((id) => id.startsWith("deepseek/")).slice(0, 10);
    throw new Error(
      `[openrouter-test] model not found in models.list: ${model}. Example available deepseek models: ${alternatives.join(", ")}`,
    );
  }

  console.error(`[openrouter-test] model exists in catalog: ${model}`);

  const completion = await client.chat.send({
    chatRequest: {
      model,
      temperature: 0,
      maxTokens: 20,
      messages: [{ role: "user", content: "Reply with exactly: ok" }],
    },
  });

  const content = completion.choices?.[0]?.message?.content?.trim() ?? "";
  console.error(`[openrouter-test] chat completion succeeded content=${JSON.stringify(content)}`);
  console.log("PASS");
};

try {
  await main();
} catch (error) {
  console.error("[openrouter-test] FAILED", error);
  process.exit(1);
}
