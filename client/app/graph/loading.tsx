import { PageLoadingScreen } from '../components/page-loading-screen';

export default function GraphLoading() {
  return (
    <PageLoadingScreen
      kind="graph"
      returnTo="/graph"
      title="Problem Graph"
      description="Loading solved-question relationships and template graph clusters."
    />
  );
}
