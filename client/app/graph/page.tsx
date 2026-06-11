import { GraphWorkbench } from '../graph-workbench';
import { getGraphPageData, getTemplatesPageData } from '../../lib/data';
import { buildSubmissionGraph } from '../../lib/submission-graph';
import { buildTemplateCatalog } from '../../lib/template-catalog';

export const dynamic = 'force-dynamic';

type SearchParams = {
  slug?: string | string[];
};

function readSlug(searchParams: SearchParams | undefined) {
  const raw = searchParams?.slug;
  if (Array.isArray(raw)) {
    return raw[0] ?? null;
  }
  return raw ?? null;
}

export default async function GraphPage({
  searchParams,
}: {
  searchParams: Promise<SearchParams>;
}) {
  const resolvedSearchParams = await searchParams;
  const [submissions, templateData] = await Promise.all([getGraphPageData(), getTemplatesPageData()]);
  const graph = buildSubmissionGraph(submissions);
  const templateCatalog = buildTemplateCatalog(templateData.tags, templateData.submissions);

  return <GraphWorkbench graph={graph} templateCatalog={templateCatalog} initialSelectedSlug={readSlug(resolvedSearchParams)} />;
}
