import { expect, test } from '@playwright/test';

test('tag workbench keeps the inspector visible on desktop', async ({ page }) => {
  await page.goto('/playwright/tag-workbench-fixture');

  const workspace = page.locator('.workspace-with-inspector');
  const inspector = page.locator('.template-plane-inspector');
  const noteCard = page.locator('.submission-thought-card');
  const contextCard = page.locator('.submission-context-card');

  await expect(workspace).toBeVisible();
  await expect(inspector).toBeVisible();
  await expect(noteCard).toBeVisible();
  await expect(contextCard).toBeVisible();

  const viewport = page.viewportSize();
  const inspectorBox = await inspector.boundingBox();
  const noteBox = await noteCard.boundingBox();
  const contextBox = await contextCard.boundingBox();

  if (!viewport || !inspectorBox || !noteBox || !contextBox) {
    throw new Error('Missing viewport or layout bounds');
  }

  expect(inspectorBox.x + inspectorBox.width).toBeLessThanOrEqual(viewport.width);
  expect(inspectorBox.width).toBeLessThanOrEqual(340);
  expect(contextBox.y).toBeGreaterThanOrEqual(noteBox.y + noteBox.height - 1);
  expect(Math.abs(contextBox.x - noteBox.x)).toBeLessThanOrEqual(1);

  const scrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
  expect(scrollWidth).toBeLessThanOrEqual(viewport.width + 1);

  await expect(workspace).toHaveScreenshot('tag-workbench-desktop.png');
});
