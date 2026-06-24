#!/usr/bin/env python3
"""Input adapters for the submission AST cluster workflow."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from config import (
    CORPUS_FIXTURES_DIR,
    DEFAULT_LABEL_MODEL,
    DEFAULT_CLUSTER_THRESHOLD,
    DEFAULT_SUBMISSION_LIMIT,
    PYTHON_LANGUAGE_LIKE_PATTERN,
)
import psycopg
from psycopg.rows import dict_row

LOGGER = logging.getLogger("submission_ast_cluster_poc")


@dataclass
class SubmissionRow:
    id: str
    title_slug: str | None
    status: str
    content: str
    created_at: str
    submission_details: Any


@dataclass
class CliOptions:
    limit: int | None = DEFAULT_SUBMISSION_LIMIT
    scan: int | None = None
    slug: str | None = None
    source: str = "db"
    corpus_dir: Path | None = None
    include_statuses: list[str] | None = None
    unique: bool = False
    threshold: float = DEFAULT_CLUSTER_THRESHOLD
    out: str | None = None
    json: bool = False
    label: bool = True
    label_model: str = ""
    verbose: bool = False


def setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )


def resolve_database_url(database_url: str | None = None) -> str | None:
    value = database_url or os.environ.get("DATABASE_URL")
    if not value:
        return None

    try:
        parsed_url = urlparse(value)
    except ValueError:
        return value

    if not parsed_url.hostname:
        return value

    params = dict(parse_qsl(parsed_url.query, keep_blank_values=True))
    for key in ("pgbouncer", "connection_limit", "pool_timeout"):
        params.pop(key, None)
    return urlunparse(parsed_url._replace(query=urlencode(params)))


def parse_args(argv: list[str]) -> CliOptions:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        choices=["db", "corpus"],
        default="db",
        help="Input source for submissions: db (Neon) or corpus (local fixtures)",
    )
    parser.add_argument("--corpus-dir", type=Path, default=CORPUS_FIXTURES_DIR)
    parser.add_argument("--limit", type=int, default=DEFAULT_SUBMISSION_LIMIT)
    parser.add_argument("--scan", type=int)
    parser.add_argument("--slug")
    parser.add_argument("--status")
    parser.add_argument("--threshold", type=float, default=DEFAULT_CLUSTER_THRESHOLD)
    parser.add_argument("--unique", action="store_true", default=False)
    parser.add_argument("--out")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--label", action="store_true", default=True)
    parser.add_argument("--no-label", action="store_false", dest="label")
    parser.add_argument("--label-model")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    return CliOptions(
        limit=args.limit,
        scan=args.scan,
        slug=args.slug,
        source=args.source,
        corpus_dir=args.corpus_dir,
        include_statuses=[value.strip() for value in args.status.split(",") if value.strip()] if args.status else None,
        unique=args.unique,
        threshold=args.threshold,
        out=args.out,
        json=args.json,
        label=args.label,
        label_model=args.label_model or os.environ.get("CLUSTER_LABEL_MODEL") or DEFAULT_LABEL_MODEL,
        verbose=args.verbose,
    )


def load_repo_env() -> None:
    if os.environ.get("DATABASE_URL"):
        LOGGER.debug("DATABASE_URL already present; skipping repo .env load")
        return

    env_path = Path(__file__).resolve().parents[3] / ".env"
    if not env_path.exists():
        LOGGER.debug("repo .env not found at %s", env_path)
        return

    loaded_keys = []
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value[:1] == value[-1:] and value[:1] in {"'", '"'}:
            value = value[1:-1]
        if key not in os.environ:
            os.environ[key] = value
            loaded_keys.append(key)
    LOGGER.debug("loaded repo .env path=%s keys=%s", env_path, ",".join(sorted(loaded_keys)))


def language_of(submission: SubmissionRow) -> str | None:
    details = submission.submission_details
    if not isinstance(details, dict):
        return None
    for key in ("lang", "language", "pretty_lang", "langName"):
        value = details.get(key)
        if isinstance(value, str):
            return value.lower()
    return None


def parse_fixture_metadata(content: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line.startswith("#"):
            break
        if ":" not in line:
            continue
        key, value = line[1:].split(":", 1)
        key = key.strip().lower().replace(" ", "_")
        metadata[key] = value.strip()
    return metadata


def normalize_fixture_id(stub: str, fallback: str) -> str:
    return stub.strip() if stub and stub.strip() else fallback


def fetch_candidate_submissions_from_corpus(options: CliOptions) -> list[SubmissionRow]:
    corpus_dir = options.corpus_dir or CORPUS_FIXTURES_DIR
    if not corpus_dir.exists():
        raise RuntimeError(f"corpus dir not found: {corpus_dir}")

    files = sorted(path for path in corpus_dir.glob("*.py") if path.is_file())
    if not files:
        raise RuntimeError(f"no fixture files found in {corpus_dir}")

    rows: list[SubmissionRow] = []
    for path in files:
        content = path.read_text(encoding="utf-8", errors="replace")
        metadata = parse_fixture_metadata(content)
        title_slug = metadata.get("problem_id")
        submission_id = normalize_fixture_id(metadata.get("submission_id", ""), path.stem)
        row = SubmissionRow(
            id=submission_id,
            title_slug=title_slug,
            status="Accepted",
            content=content,
            created_at=datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat().replace("+00:00", "Z"),
            submission_details={"lang": "python3", "language": "python3"},
        )
        rows.append(row)

    if options.unique:
        rows = dedupe_latest_by_title_slug(rows, options.limit or len(rows))
    if options.scan is not None:
        rows = rows[:options.scan]
    if options.limit is not None:
        rows = rows[: options.limit]
    LOGGER.info("loaded corpus fixtures count=%d path=%s unique=%s", len(rows), corpus_dir, options.unique)
    return rows


def dedupe_latest_by_title_slug(rows: list[SubmissionRow], limit: int) -> list[SubmissionRow]:
    seen: set[str] = set()
    unique_rows: list[SubmissionRow] = []
    for row in rows:
        key = row.title_slug.strip() if row.title_slug else None
        if not key or key in seen:
            continue
        seen.add(key)
        unique_rows.append(row)
        if len(unique_rows) >= limit:
            break
    return unique_rows


def fetch_candidate_submissions_db(options: CliOptions) -> list[SubmissionRow]:
    database_url = resolve_database_url()
    if not database_url:
        raise RuntimeError("DATABASE_URL is required")

    LOGGER.info(
        "fetching candidate submissions unique=%s limit=%s scan=%s slug=%s statuses=%s",
        options.unique,
        options.limit,
        options.scan,
        options.slug or "*",
        options.include_statuses or ["Accepted"],
    )

    language_sql = """
        coalesce(
            "submissionDetails"->>'lang',
            "submissionDetails"->>'language',
            "submissionDetails"->>'pretty_lang',
            "submissionDetails"->>'langName',
            ''
        )
    """
    where = []
    params: list[Any] = []

    if options.slug:
        where.append('"titleSlug" = %s')
        params.append(options.slug)

    if options.include_statuses:
        where.append("status = ANY(%s)")
        params.append(options.include_statuses)
    else:
        where.append("status = %s")
        params.append("Accepted")

    where.append(f"{language_sql} ILIKE %s")
    params.append(PYTHON_LANGUAGE_LIKE_PATTERN)

    where_clause = " AND ".join(where) if where else "TRUE"
    if options.unique:
        query = f"""
            WITH ranked AS (
                SELECT
                    id,
                    "titleSlug" AS title_slug,
                    status,
                    content,
                    "createdAt" AS created_at,
                    "submissionDetails" AS submission_details,
                    row_number() OVER (
                        PARTITION BY "titleSlug"
                        ORDER BY "createdAt" DESC
                    ) AS rn
                FROM "Submission"
                WHERE {where_clause}
                  AND "titleSlug" IS NOT NULL
            )
            SELECT id, title_slug, status, content, created_at, submission_details
            FROM ranked
            WHERE rn = 1
            ORDER BY created_at DESC
        """
        if options.limit is not None:
            query += "\nLIMIT %s"
            params.append(options.limit)
    else:
        query = f"""
            SELECT id, "titleSlug" AS title_slug, status, content, "createdAt" AS created_at, "submissionDetails" AS submission_details
            FROM "Submission"
            WHERE {where_clause}
            ORDER BY "createdAt" DESC
        """
        fetch_limit = options.scan if options.scan is not None else options.limit
        if fetch_limit is not None:
            query += "\nLIMIT %s"
            params.append(fetch_limit)

    with psycopg.connect(database_url, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            rows = [
                SubmissionRow(
                    id=str(row["id"]),
                    title_slug=row["title_slug"],
                    status=row["status"],
                    content=row["content"],
                    created_at=row["created_at"].isoformat(),
                    submission_details=row["submission_details"],
                )
                for row in cur.fetchall()
            ]

    if options.unique or options.scan is None:
        LOGGER.info("fetched submissions count=%d", len(rows))
        return rows

    python_rows = [row for row in rows if (language_of(row) or "").find("python") >= 0]
    limited_rows = python_rows[: options.limit] if options.limit is not None else python_rows
    LOGGER.info("fetched submissions count=%d pythonFiltered=%d", len(rows), len(limited_rows))
    return limited_rows


def fetch_candidate_submissions(options: CliOptions) -> list[SubmissionRow]:
    if options.source == "corpus":
        return fetch_candidate_submissions_from_corpus(options)
    return fetch_candidate_submissions_db(options)
