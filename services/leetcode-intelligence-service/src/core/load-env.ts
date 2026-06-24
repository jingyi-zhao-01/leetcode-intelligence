import path from 'node:path';

import { config as loadDotenv } from 'dotenv';

const candidateEnvPaths = [path.resolve(process.cwd(), '.env'), path.resolve(process.cwd(), '../../.env')];

let loaded = false;

export function ensureServiceEnvLoaded() {
  if (loaded) {
    return;
  }

  for (const envPath of candidateEnvPaths) {
    loadDotenv({ path: envPath, override: false });
  }

  loaded = true;
}
