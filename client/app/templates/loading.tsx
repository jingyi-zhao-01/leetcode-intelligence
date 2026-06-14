import { PageLoadingScreen } from '../components/page-loading-screen';

export default function TemplatesLoading() {
  return (
    <PageLoadingScreen
      kind="templates"
      returnTo="/templates"
      title="Template Groups"
      description="Loading canonical templates, groups, and associated submissions."
    />
  );
}
