import { expect, test } from '@playwright/test';

test('tag workbench keeps the inspector visible on desktop', async ({ page }) => {
  await page.goto('/playwright/tag-workbench-fixture');

  const workspace = page.locator('.workspace-with-inspector');
  const inspector = page.locator('.template-plane-inspector');

  await expect(workspace).toBeVisible();
  await expect(inspector).toBeVisible();

  const viewport = page.viewportSize();
  const inspectorBox = await inspector.boundingBox();

  if (!viewport || !inspectorBox) {
    throw new Error('Missing viewport or inspector bounds');
  }

  expect(inspectorBox.x + inspectorBox.width).toBeLessThanOrEqual(viewport.width);

  const scrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
  expect(scrollWidth).toBeLessThanOrEqual(viewport.width + 1);

  await expect(workspace).toHaveScreenshot('tag-workbench-desktop.png');
});
