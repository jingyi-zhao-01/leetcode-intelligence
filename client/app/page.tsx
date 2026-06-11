import { getTagWorkbenchData } from "../lib/data";
import { TagWorkbench } from "./tag-workbench";

export const dynamic = "force-dynamic";

export default async function Page() {
  const data = await getTagWorkbenchData();
  return <TagWorkbench submissions={data.submissions} tags={data.tags} />;
}
