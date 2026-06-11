import { getTagWorkbenchData } from "../lib/data";
import { isWriteAllowed } from "../lib/access-control";
import { TagWorkbench } from "./tag-workbench";

export const dynamic = "force-dynamic";

export default async function Page() {
  const data = await getTagWorkbenchData();
  const canWrite = await isWriteAllowed();
  return <TagWorkbench submissions={data.submissions} tags={data.tags} canWrite={canWrite} />;
}
