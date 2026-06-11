'use server';

import { revalidatePath } from 'next/cache';
import { prisma } from '../lib/prisma';
import { analyzeSubmissionTemplates } from '../lib/template-analyzer';

type PatternTagWriter = Pick<typeof prisma, 'submissionPatternTag'>;

async function replaceTagsForSubmission(
  submissionId: string,
  patternTagIds: string[],
  client: PatternTagWriter = prisma,
) {
  const uniqueTagIds = [...new Set(patternTagIds)];

  await client.submissionPatternTag.deleteMany({ where: { submissionId } });

  if (uniqueTagIds.length > 0) {
    await client.submissionPatternTag.createMany({
      data: uniqueTagIds.map((patternTagId) => ({ submissionId, patternTagId })),
      skipDuplicates: true,
    });
  }
}

export async function saveSubmissionTags(submissionId: string, patternTagIds: string[]) {
  const submission = await prisma.submission.findFirst({
    where: { id: submissionId, status: 'Accepted' },
    select: { id: true },
  });

  if (!submission) {
    return;
  }

  await prisma.$transaction(async (tx) => {
    await replaceTagsForSubmission(submissionId, patternTagIds, tx);
  });
  revalidatePath('/');
}

export async function benchmarkSubmissionTemplates(submissionId: string, excludedGroupKeys: string[] = []) {
  return analyzeSubmissionTemplates(submissionId, excludedGroupKeys);
}
