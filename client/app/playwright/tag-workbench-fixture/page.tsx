import { WorkspaceShell } from '../../components/workspace-shell';
import { TagWorkbench } from '../../tag-workbench';
import { makeTagWorkbenchSubmissions, makeTagWorkbenchTags } from '../../../lib/tag-workbench.fixture';

export default function TagWorkbenchFixturePage() {
  return (
    <WorkspaceShell
      activeRoute="submission-history"
      canWrite
      returnTo="/playwright/tag-workbench-fixture"
      title="Submission Taxonomy"
      description="Fixture page for visual regression coverage."
    >
      <TagWorkbench submissions={makeTagWorkbenchSubmissions()} tags={makeTagWorkbenchTags()} canWrite />
    </WorkspaceShell>
  );
}
