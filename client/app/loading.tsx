import { PageLoadingScreen } from './components/page-loading-screen';

export default function RootLoading() {
  return (
    <PageLoadingScreen
      kind="submissions"
      returnTo="/submission-history"
      title="LeetCode Intelligence"
      description="Preparing the workbench shell and route data."
    />
  );
}
