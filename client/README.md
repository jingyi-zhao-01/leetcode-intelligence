# LeetCode QA Client Deployment

This Next.js client is a thin BFF. It owns UI, admin session state, middleware, and request adaptation, while all database access and OpenRouter calls live in `services/leetcode-intelligence-service`.

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
   - `BFF_SERVICE_URL` (required)
   - `BFF_TOKEN` (required)
   - `ADMIN_PASSWORD` (required)
   - `ADMIN_SESSION_TOKEN` (recommended, separate from `ADMIN_PASSWORD`)
   - `ADMIN_COOKIE_NAME` (optional, default `leetcode-qa-admin`)
   - `ADMIN_COOKIE_MAX_AGE_SECONDS` (optional, default `28800`)
   - `UPSTASH_REDIS_REST_URL` (required for prod non-admin IP rate limiting)
   - `UPSTASH_REDIS_REST_TOKEN` (required for prod non-admin IP rate limiting)
   - `NON_ADMIN_RATE_LIMIT_MAX_REQUESTS` (optional, default `120`)
   - `NON_ADMIN_RATE_LIMIT_WINDOW_SECONDS` (optional, default `60`)
3. Deploy.

The client no longer reads `DATABASE_URL` or `OPEN_ROUTER_API_KEY` directly on Vercel.

## Production rate limiting

- In production, all non-admin requests are rate-limited by client IP in middleware.
- Admin sessions bypass the limiter.
- Optional local write bypass is available only when `ENABLE_LOCAL_WRITE_BYPASS=true`.
- Vercel Preview deployments are not treated as production for this limiter.

## First write authentication

- Visit `/admin/login`.
- Enter `ADMIN_PASSWORD` once to create the session.
- After that, UI shows `Write enabled` and write buttons are active.
- Sign out via top-right button or `/admin/logout`.

## Run as systemd service on reboot

To keep the client running across reboots, use the provided service unit and installer:

- `client/leetcode-qa-client.service`
- `client/install-systemd-service.sh`

From repo root:

```bash
cd /home/jingyi/PycharmProjects/leetcode-qa/client
sudo ./install-systemd-service.sh
```

This script:

- Copies `leetcode-qa-client.service` into `/etc/systemd/system/`
- Reloads systemd unit definitions
- Enables the service on boot
- Starts/refreshes the service now

Useful commands:

```bash
sudo systemctl status leetcode-qa-client.service
sudo systemctl restart leetcode-qa-client.service
sudo systemctl stop leetcode-qa-client.service
sudo systemctl disable leetcode-qa-client.service
```

If you prefer, run the service unit directly:

- Working directory: `/home/jingyi/PycharmProjects/leetcode-qa/client`
- Command: `npm run start -- --hostname 0.0.0.0 --port 3005`
- Auto-restart: on crash/exit, with 5s backoff
