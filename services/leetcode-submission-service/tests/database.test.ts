import assert from "node:assert/strict";
import { describe, it } from "vitest";

import { getDatabaseDiagnostics, resolveDatabaseUrl } from "../src/ts/database.ts";

describe("database url normalization", () => {
  it("adds pooler-safe defaults for Neon pooler URLs", () => {
    const resolved = resolveDatabaseUrl(
      "postgresql://user:pass@ep-demo-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require",
    );

    assert.ok(resolved);

    const parsed = new URL(resolved);
    assert.equal(parsed.searchParams.get("pgbouncer"), "true");
    assert.equal(parsed.searchParams.get("connection_limit"), "1");
    assert.equal(parsed.searchParams.get("pool_timeout"), "30");
  });

  it("preserves explicit pooler tuning from the input URL", () => {
    const resolved = resolveDatabaseUrl(
      "postgresql://user:pass@ep-demo-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&connection_limit=5&pool_timeout=12&pgbouncer=false",
    );

    assert.ok(resolved);

    const parsed = new URL(resolved);
    assert.equal(parsed.searchParams.get("connection_limit"), "5");
    assert.equal(parsed.searchParams.get("pool_timeout"), "12");
    assert.equal(parsed.searchParams.get("pgbouncer"), "false");
  });

  it("leaves direct Postgres URLs unchanged", () => {
    const original = "postgresql://user:pass@db.example.com/neondb?sslmode=require";
    assert.equal(resolveDatabaseUrl(original), original);
  });

  it("reports diagnostics from the effective URL", () => {
    const diagnostics = getDatabaseDiagnostics(
      "postgresql://user:pass@ep-demo-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require",
    );

    assert.deepEqual(diagnostics, {
      configured: true,
      protocol: "postgresql",
      host: "ep-demo-pooler.c-2.us-east-1.aws.neon.tech",
      database: "neondb",
      usesPooler: true,
      sslmode: "require",
      channelBinding: undefined,
      connectionLimit: "1",
      poolTimeout: "30",
      pgbouncer: "true",
    });
  });
});
