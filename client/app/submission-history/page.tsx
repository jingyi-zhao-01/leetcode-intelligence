import { getTagWorkbenchData } from '../../lib/data';
import { isWriteAllowed } from '../../lib/access-control';
import { WorkspaceShell } from '../components/workspace-shell';
import { TagWorkbench } from '../tag-workbench';

export const dynamic = 'force-dynamic';

export default async function SubmissionHistoryPage() {
  const [data, canWrite] = await Promise.all([getTagWorkbenchData(), isWriteAllowed()]);
  return (
    <WorkspaceShell
      activeRoute="submission-history"
      canWrite={canWrite}
      returnTo="/submission-history"
      title="Submission Taxonomy"
    >
      <TagWorkbench submissions={data.submissions} tags={data.tags} canWrite={canWrite} />
    </WorkspaceShell>
  );
}
