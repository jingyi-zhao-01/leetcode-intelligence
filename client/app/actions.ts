'use server';

import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';
import { prisma } from '../lib/prisma';
import { analyzeSubmissionTemplates } from '../lib/template-analyzer';
import {
  assertWriteAccess,
  clearWriteSession,
  isWriteConfigured,
  setWriteSession,
} from '../lib/access-control';
import {
  createGeneratedTemplate as createGeneratedTemplateRecord,
  generateTemplateDraft as generateTemplateDraftFromLlm,
  type GeneratedTemplateDraft,
} from '../lib/template-generator';

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
  await assertWriteAccess();
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
  await assertWriteAccess();
  const submission = await prisma.submission.findFirst({
    where: { id: submissionId, status: 'Accepted' },
    select: { templateBenchmarkOptOut: true },
  });

  if (!submission) {
    throw new Error('Submission not found or not accepted.');
  }

  if (submission.templateBenchmarkOptOut) {
    throw new Error('Submission is opted out from templating.');
  }

  return analyzeSubmissionTemplates(submissionId, excludedGroupKeys);
}

export async function setSubmissionTemplateOptOut(submissionId: string, templateBenchmarkOptOut: boolean) {
  await assertWriteAccess();
  const submission = await prisma.submission.findFirst({
    where: { id: submissionId, status: 'Accepted' },
    select: { id: true },
  });

  if (!submission) {
    return { status: 'not_found' as const };
  }

  await prisma.submission.update({
    where: { id: submissionId },
    data: { templateBenchmarkOptOut },
  });

  revalidatePath('/');
  return { status: 'updated' as const, templateBenchmarkOptOut };
}

export async function generateTemplateDraft(input: {
  groupKey: string;
  submissionId: string;
  prompt: string;
  model?: string;
}) {
  await assertWriteAccess();
  return generateTemplateDraftFromLlm(input);
}

export async function createGeneratedTemplate(groupKey: string, draft: GeneratedTemplateDraft) {
  await assertWriteAccess();
  const template = await createGeneratedTemplateRecord(groupKey, draft);
  revalidatePath('/');
  return template;
}

export async function deleteNonSeededTemplate(patternTagId: string) {
  await assertWriteAccess();
  const tag = await prisma.patternTag.findUnique({
    where: { id: patternTagId },
    select: {
      id: true,
      key: true,
      label: true,
      source: true,
      dimension: true,
      SubmissionPatternTag: {
        take: 12,
        orderBy: { createdAt: 'desc' },
        select: {
          Submission: {
            select: {
              id: true,
              titleSlug: true,
              status: true,
              createdAt: true,
            },
          },
        },
      },
      _count: { select: { SubmissionPatternTag: true } },
    },
  });

  if (!tag || tag.dimension !== 'template' || tag.source === 'seeded') {
    return { status: 'not_allowed' as const };
  }

  if (tag._count.SubmissionPatternTag > 0) {
    return {
      status: 'blocked' as const,
      tag: { key: tag.key, label: tag.label },
      assignmentCount: tag._count.SubmissionPatternTag,
      submissions: tag.SubmissionPatternTag.map((entry) => ({
        id: entry.Submission.id,
        titleSlug: entry.Submission.titleSlug,
        status: entry.Submission.status,
        createdAt: entry.Submission.createdAt.toISOString(),
      })),
    };
  }

  await prisma.patternTag.delete({ where: { id: tag.id } });
  revalidatePath('/');
  return { status: 'deleted' as const, key: tag.key };
}

export async function loginAdmin(formData: FormData) {
  const password = String(formData.get('password') ?? '').trim();
  const returnTo = String(formData.get('returnTo') ?? '/');
  if (!isWriteConfigured()) {
    redirect('/admin/login?error=config');
  }

  if (password !== process.env.ADMIN_PASSWORD) {
    redirect('/admin/login?error=invalid');
  }

  await setWriteSession();
  const cleanReturnTo = returnTo.startsWith('/') ? returnTo : '/';
  redirect(cleanReturnTo);
}

export async function logoutAdmin() {
  await clearWriteSession();
  redirect('/admin/login');
}
