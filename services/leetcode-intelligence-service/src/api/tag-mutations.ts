import type { ApiContext } from './context.ts';
import { slugify } from './shared.ts';

export function createTagMutationsApi({ prisma }: ApiContext) {
  const saveSubmissionTags = async (submissionId: string, patternTagIds: string[]) => {
    const submission = await prisma.submission.findFirst({
      where: { id: submissionId, status: 'Accepted' },
      select: { id: true },
    });

    if (!submission) {
      return { status: 'not_found' as const };
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
      const uniqueTagIds = [...new Set(patternTagIds.filter((patternTagId) => allowedTagIds.has(patternTagId)))];
      await tx.submissionPatternTag.deleteMany({ where: { submissionId } });

      if (uniqueTagIds.length > 0) {
        await tx.submissionPatternTag.createMany({
          data: uniqueTagIds.map((patternTagId) => ({ submissionId, patternTagId })),
          skipDuplicates: true,
        });
      }
    });

    return { status: 'updated' as const };
  };

  const createTemplateGroup = async (input: { label: string; key?: string; description?: string }) => {
    const label = input.label.trim();
    const description = input.description?.trim() || null;
    const requestedKey = input.key?.trim() || label;
    const baseKey = slugify(requestedKey);

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

    return prisma.patternTag.create({
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
  };

  const moveTemplateToGroup = async (input: { templateId: string; targetGroupId: string }) => {
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

    if (
      !targetGroup ||
      !targetGroup.isActive ||
      targetGroup.dimension !== 'template' ||
      targetGroup.kind !== 'template_group'
    ) {
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

    return {
      status: 'moved' as const,
      template: { id: template.id, key: template.key, label: template.label },
      group: { id: targetGroup.id, key: targetGroup.key, label: targetGroup.label },
    };
  };

  const deleteNonSeededTemplate = async (patternTagId: string) => {
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
    return { status: 'deleted' as const, key: tag.key };
  };

  const updateSubmissionThought = async (submissionId: string, thought: string) => {
    const submission = await prisma.submission.findFirst({
      where: { id: submissionId, status: 'Accepted' },
      select: { id: true },
    });

    if (!submission) {
      return { status: 'not_found' as const };
    }

    const normalizedThought = thought.trim();
    await prisma.submission.update({
      where: { id: submissionId },
      data: {
        thought: normalizedThought.length > 0 ? normalizedThought : null,
      },
    });

    return {
      status: 'updated' as const,
      thought: normalizedThought.length > 0 ? normalizedThought : null,
    };
  };

  return {
    saveSubmissionTags,
    updateSubmissionThought,
    createTemplateGroup,
    moveTemplateToGroup,
    deleteNonSeededTemplate,
  };
}
