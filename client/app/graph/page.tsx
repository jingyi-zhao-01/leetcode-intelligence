import { GraphWorkbench } from '../graph-workbench';
import { getTagWorkbenchData } from '../../lib/data';
import { buildSubmissionGraph } from '../../lib/submission-graph';

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
  const data = await getTagWorkbenchData();
  const graph = buildSubmissionGraph(data.submissions);

  return <GraphWorkbench submissions={data.submissions} graph={graph} initialSelectedSlug={readSlug(resolvedSearchParams)} />;
}
