import readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

import type { PromptDelivery, PromptDispatchSuccess } from './contracts.ts';

export class CliClient {
  readonly channelId = 'cli';

  async renderPrompt(prompt: PromptDispatchSuccess): Promise<PromptDelivery> {
    const promptBody = prompt.questionSlug
      ? `Question: ${prompt.questionSlug}\n\n${prompt.promptText}\n`
      : `${prompt.promptText}\n`;
    process.stdout.write(promptBody);
    return {};
  }

  async renderText(content: string): Promise<PromptDelivery> {
    process.stdout.write(`${content}\n`);
    return {};
  }

  async requestReply(question = '\nYour reply: '): Promise<string> {
    const rl = readline.createInterface({ input, output });
    try {
      return await rl.question(question);
    } finally {
      rl.close();
    }
  }
}
