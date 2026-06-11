import { getTemplatesPageData } from '../../lib/data';
import { isWriteAllowed } from '../../lib/access-control';
import { TemplateGroupsWorkbench } from '../template-groups-workbench';
import { buildTemplateCatalog } from '../../lib/template-catalog';

export const dynamic = 'force-dynamic';

export default async function TemplatesPage() {
  const [{ tags, submissions }, canWrite] = await Promise.all([getTemplatesPageData(), isWriteAllowed()]);
  const clusters = buildTemplateCatalog(tags, submissions);

  return (
    <TemplateGroupsWorkbench clusters={clusters} canWrite={canWrite} />
  );
}
