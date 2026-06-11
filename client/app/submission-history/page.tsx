import { getTagWorkbenchData } from '../../lib/data';
import { isWriteAllowed } from '../../lib/access-control';
import { TagWorkbench } from '../tag-workbench';

export const dynamic = 'force-dynamic';

export default async function SubmissionHistoryPage() {
  const [data, canWrite] = await Promise.all([getTagWorkbenchData(), isWriteAllowed()]);
  return <TagWorkbench submissions={data.submissions} tags={data.tags} canWrite={canWrite} />;
}
