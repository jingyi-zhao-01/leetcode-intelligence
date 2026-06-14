import { getTemplatesPageData } from '../../lib/data';
import { isWriteAllowed } from '../../lib/access-control';
import { WorkspaceShell } from '../components/workspace-shell';
import { TemplateGroupsWorkbench } from '../template-groups-workbench';
import { buildTemplateCatalog } from '../../lib/template-catalog';

export const dynamic = 'force-dynamic';

export default async function TemplatesPage() {
  const [{ tags, submissions }, canWrite] = await Promise.all([getTemplatesPageData(), isWriteAllowed()]);
  const clusters = buildTemplateCatalog(tags, submissions);

  return (
    <WorkspaceShell activeRoute="templates" canWrite={canWrite} returnTo="/templates" title="Template Groups">
      <TemplateGroupsWorkbench clusters={clusters} canWrite={canWrite} />
    </WorkspaceShell>
  );
}
