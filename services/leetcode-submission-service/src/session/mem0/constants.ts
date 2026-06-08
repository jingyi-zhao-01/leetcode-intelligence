import { createLogger } from '../../logger.ts';

export const logger = createLogger('session-mem0');

export const DEFAULT_MEM0_APP_ID = 'leetcode-qa';
export const DEFAULT_MEM0_AGENT_ID = 'leetcode-submission-service';
export const DEFAULT_MEM0_BASE_URL = 'https://api.mem0.ai';

export const MAX_TEXT_SECTION_CHARS = 6_000;
export const MAX_JSON_SECTION_CHARS = 4_000;
export const MAX_MESSAGE_CHARS = 1_200;
export const MAX_COMPANION_TURNS = 12;
export const MAX_SERVICE_UPDATES = 8;
export const MAX_RECALLED_SESSION_RECORDS = 12;
export const MAX_RECALLED_CODE_CHARS = 600;
export const MAX_RECALLED_ANALYSIS_CHARS = 1_200;
export const MAX_RECALLED_FAILURE_CHARS = 900;
export const MAX_MOUNT_SUMMARY_RECORDS = 3;
export const MAX_MOUNT_SUMMARY_CHARS = 1_600;
export const MIN_INTERACTIONS_TO_PERSIST = 5;
