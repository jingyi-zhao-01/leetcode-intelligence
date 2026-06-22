'use server';

import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';
import {
  type GeneratedTemplateDraft,
  type TemplateBenchmarkResult,
} from '../lib/data';
import { getIntelligenceServiceJson } from '../lib/intelligence-service';
import {
  assertWriteAccess,
  clearWriteSession,
  isWriteConfigured,
  setWriteSession,
} from '../lib/access-control';

export async function saveSubmissionTags(submissionId: string, patternTagIds: string[]) {
  await assertWriteAccess();
  await getIntelligenceServiceJson<{ status: 'updated' | 'not_found' }>(`/bff/submissions/${submissionId}/tags`, {
    method: 'POST',
    body: { patternTagIds },
  });
  revalidatePath('/');
}

export async function updateSubmissionThought(submissionId: string, thought: string) {
  await assertWriteAccess();
  const result = await getIntelligenceServiceJson<
    { status: 'not_found' } | { status: 'updated'; thought: string | null }
  >(`/bff/submissions/${submissionId}/thought`, {
    method: 'POST',
    body: { thought },
  });
  revalidatePath('/');
  return result;
}

export async function benchmarkSubmissionTemplates(submissionId: string, excludedGroupKeys: string[] = []) {
  await assertWriteAccess();
  return getIntelligenceServiceJson<TemplateBenchmarkResult>(`/bff/submissions/${submissionId}/template-benchmark`, {
    method: 'POST',
    body: { excludedGroupKeys },
  });
}

export async function setSubmissionTemplateOptOut(submissionId: string, templateBenchmarkOptOut: boolean) {
  await assertWriteAccess();
  const result = await getIntelligenceServiceJson<
    { status: 'not_found' } | { status: 'updated'; templateBenchmarkOptOut: boolean }
  >(`/bff/submissions/${submissionId}/template-benchmark-opt-out`, {
    method: 'POST',
    body: { templateBenchmarkOptOut },
  });

  revalidatePath('/');
  return result;
}

export async function generateTemplateDraft(input: {
  groupKey: string;
  submissionId: string;
  prompt: string;
  model?: string;
}) {
  await assertWriteAccess();
  return getIntelligenceServiceJson<{ model: string; draft: GeneratedTemplateDraft }>('/bff/templates/draft', {
    method: 'POST',
    body: input,
  });
}

export async function createGeneratedTemplate(groupKey: string, draft: GeneratedTemplateDraft) {
  await assertWriteAccess();
  const template = await getIntelligenceServiceJson<{ id: string; key: string }>('/bff/templates/generated', {
    method: 'POST',
    body: { groupKey, draft },
  });
  revalidatePath('/');
  return template;
}

export async function createTemplateGroup(input: {
  label: string;
  key?: string;
  description?: string;
}) {
  await assertWriteAccess();
  const group = await getIntelligenceServiceJson<{ id: string; key: string; label: string }>('/bff/template-groups', {
    method: 'POST',
    body: input,
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
  const result = await getIntelligenceServiceJson<
    | { status: 'invalid_template' }
    | { status: 'invalid_target_group' }
    | { status: 'unchanged'; template: { id: string; key: string; label: string }; group: { id: string; key: string; label: string } }
    | { status: 'moved'; template: { id: string; key: string; label: string }; group: { id: string; key: string; label: string } }
  >('/bff/templates/move', {
    method: 'POST',
    body: input,
  });

  revalidatePath('/');
  revalidatePath('/templates');
  revalidatePath('/graph');
  revalidatePath('/submission-history');
  return result;
}

export async function deleteNonSeededTemplate(patternTagId: string) {
  await assertWriteAccess();
  const result = await getIntelligenceServiceJson<
    | { status: 'not_allowed' }
    | {
        status: 'blocked';
        tag: { key: string; label: string };
        assignmentCount: number;
        submissions: Array<{
          id: string;
          titleSlug: string | null;
          status: string;
          createdAt: string;
        }>;
      }
    | { status: 'deleted'; key: string }
  >(`/bff/templates/${patternTagId}`, {
    method: 'DELETE',
  });

  if (result.status === 'deleted') {
    revalidatePath('/');
  }

  return result;
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
