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

function slugifyTemplateKey(value: string) {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
}

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

  const allowedTags = await prisma.patternTag.findMany({
    where: {
      id: { in: [...new Set(patternTagIds)] },
      isActive: true,
      kind: 'tag',
    },
    select: { id: true },
  });

  const allowedTagIds = new Set(allowedTags.map((tag) => tag.id));

  await prisma.$transaction(async (tx) => {
    await replaceTagsForSubmission(
      submissionId,
      patternTagIds.filter((patternTagId) => allowedTagIds.has(patternTagId)),
      tx,
    );
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

export async function createTemplateGroup(input: {
  label: string;
  key?: string;
  description?: string;
}) {
  await assertWriteAccess();

  const label = input.label.trim();
  const description = input.description?.trim() || null;
  const requestedKey = input.key?.trim() || label;
  const baseKey = slugifyTemplateKey(requestedKey);

  if (!label) {
    throw new Error('Template group label is required.');
  }

  if (!baseKey) {
    throw new Error('Template group key is invalid.');
  }

  let key = baseKey;
  for (let suffix = 2; await prisma.patternTag.findUnique({ where: { key } }); suffix += 1) {
    key = `${baseKey}-${suffix}`;
  }

  const maxSortOrder = await prisma.patternTag.aggregate({
    where: { dimension: 'template', kind: 'template_group' },
    _max: { sortOrder: true },
  });

  const group = await prisma.patternTag.create({
    data: {
      key,
      label,
      description,
      dimension: 'template',
      kind: 'template_group',
      source: 'manually_created',
      isActive: true,
      parentId: null,
      sortOrder: (maxSortOrder._max.sortOrder ?? 0) + 100,
    },
    select: { id: true, key: true, label: true },
  });

  revalidatePath('/');
  revalidatePath('/templates');
  revalidatePath('/graph');
  revalidatePath('/submission-history');
  return group;
}

export async function moveTemplateToGroup(input: {
  templateId: string;
  targetGroupId: string;
}) {
  await assertWriteAccess();

  const [template, targetGroup] = await Promise.all([
    prisma.patternTag.findUnique({
      where: { id: input.templateId },
      select: {
        id: true,
        key: true,
        label: true,
        dimension: true,
        kind: true,
        parentId: true,
        isActive: true,
      },
    }),
    prisma.patternTag.findUnique({
      where: { id: input.targetGroupId },
      select: {
        id: true,
        key: true,
        label: true,
        dimension: true,
        kind: true,
        isActive: true,
      },
    }),
  ]);

  if (!template || !template.isActive || template.dimension !== 'template' || template.kind !== 'tag') {
    return { status: 'invalid_template' as const };
  }

  if (!targetGroup || !targetGroup.isActive || targetGroup.dimension !== 'template' || targetGroup.kind !== 'template_group') {
    return { status: 'invalid_target_group' as const };
  }

  if (template.id === targetGroup.id) {
    return { status: 'invalid_target_group' as const };
  }

  if (template.parentId === targetGroup.id) {
    return {
      status: 'unchanged' as const,
      template: { id: template.id, key: template.key, label: template.label },
      group: { id: targetGroup.id, key: targetGroup.key, label: targetGroup.label },
    };
  }

  await prisma.patternTag.update({
    where: { id: template.id },
    data: { parentId: targetGroup.id },
  });

  revalidatePath('/');
  revalidatePath('/templates');
  revalidatePath('/graph');
  revalidatePath('/submission-history');
  return {
    status: 'moved' as const,
    template: { id: template.id, key: template.key, label: template.label },
    group: { id: targetGroup.id, key: targetGroup.key, label: targetGroup.label },
  };
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
      kind: true,
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

  if (!tag || tag.dimension !== 'template' || tag.kind !== 'tag' || tag.source === 'seeded') {
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
  const returnTo = String(formData.get('returnTo') ?? '/submission-history');
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
