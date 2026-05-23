import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

export class CliClient {
  readonly channelId = "cli";

  async sendPrompt(promptText: string): Promise<{ messageId?: string }> {
    void promptText;
    return {};
  }

  async promptReply(question = "\nYour reply: "): Promise<string> {
    const rl = readline.createInterface({ input, output });
    try {
      return await rl.question(question);
    } finally {
      rl.close();
    }
  }
}
