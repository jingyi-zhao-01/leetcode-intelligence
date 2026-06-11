# LeetCode QA Client Deployment

This Next.js client uses middleware + session-cookie check to enforce write-only access for mutation operations.

## Access Model

- All reads are public.
- All write operations require a valid admin session:
  - `saveSubmissionTags`
  - `benchmarkSubmissionTemplates`
  - `setSubmissionTemplateOptOut`
  - `generateTemplateDraft`
  - `createGeneratedTemplate`
  - `deleteNonSeededTemplate`
- Session is issued by `POST /admin/login` via server action and stored in a cookie named `ADMIN_COOKIE_NAME`.
- `canWrite` is also derived server-side from cookie on the main page so the UI enters read-only mode automatically.

## Vercel setup

1. Point the Vercel project root to `client/`.
2. Set environment variables:
   - `DATABASE_URL`
   - `OPEN_ROUTER_API_KEY`
   - `ADMIN_PASSWORD` (required)
   - `ADMIN_SESSION_TOKEN` (recommended, separate from `ADMIN_PASSWORD`)
   - `ADMIN_COOKIE_NAME` (optional, default `leetcode-qa-admin`)
   - `ADMIN_COOKIE_MAX_AGE_SECONDS` (optional, default `28800`)
3. Deploy.

## First write authentication

- Visit `/admin/login`.
- Enter `ADMIN_PASSWORD` once to create the session.
- After that, UI shows `Write enabled` and write buttons are active.
- Sign out via top-right button or `/admin/logout`.
