import { PageLoadingScreen } from '../components/page-loading-screen';

export default function SubmissionHistoryLoading() {
  return (
    <PageLoadingScreen
      kind="submissions"
      returnTo="/submission-history"
      title="Submission Taxonomy"
      description="Loading accepted submissions, taxonomy tags, code, and problem statements."
    />
  );
}
