"""
LeetCode Submission Evolution Tools
Provides functionality for analyzing submission evolution and thought progression.
"""

import asyncio
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Tuple

from prisma import Prisma
from util import (
    extract_comments,
    analyze_comment_themes,
    count_complexity_mentions,
    calculate_evolution_metrics,
    analyze_overall_progression,
)


# === REVIEW HELPERS ===


def _parse_date(value: str) -> datetime:
    """
    Parse a single date value into a UTC start-of-day datetime.

    Accepts:
        - "today"      → current calendar day in UTC
        - "yesterday"  → previous calendar day in UTC
        - "YYYY-MM-DD" → that specific day in UTC
    """
    norm = value.strip().lower()
    now_utc = datetime.now(timezone.utc)

    if norm == "today":
        return now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    if norm == "yesterday":
        return (now_utc - timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
    try:
        return datetime.strptime(norm, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        raise ValueError(
            f"Invalid date '{value}'. "
            "Use 'today', 'yesterday', or a date like '2026-02-20'."
        )


def resolve_date_range(
    period: Optional[str],
    start_date: Optional[str],
    end_date: Optional[str],
) -> Tuple[datetime, datetime, str]:
    """
    Resolve the final UTC [start, end) window and a human-readable label.

    Priority:
        1. If *start_date* is given, use explicit range mode:
           - start = start-of-day of start_date
           - end   = start-of-day of end_date + 1 day  (i.e. end_date is *inclusive*)
                     defaults to start_date when end_date is omitted
        2. Otherwise fall back to the *period* shorthand
           ('today', 'yesterday', or 'YYYY-MM-DD' for a single day).

    Returns:
        (start datetime, end datetime, label str)
    """
    if start_date:
        start = _parse_date(start_date)
        end_base = _parse_date(end_date) if end_date else start
        end = end_base + timedelta(days=1)
        label = (
            start_date
            if (not end_date or start_date == end_date)
            else f"{start_date} to {end_date}"
        )
    else:
        resolved_period = period or "today"
        start = _parse_date(resolved_period)
        end = start + timedelta(days=1)
        label = resolved_period

    return start, end, label


async def fetch_submissions_in_range(
    db: Prisma, start: datetime, end: datetime
) -> Tuple[List[Any], Dict[str, Any]]:
    """
    Fetch all submissions in [start, end) and enrich with Question metadata.

    Returns:
        (submissions list ordered by createdAt asc,
         questions_map {titleSlug: Question})
    """
    submissions = await db.submission.find_many(
        where={"createdAt": {"gte": start, "lt": end}},
        order=[{"createdAt": "asc"}],
    )

    slugs = list({s.titleSlug for s in submissions if s.titleSlug})

    question_results = await asyncio.gather(
        *[db.question.find_unique(where={"titleSlug": slug}) for slug in slugs]
    )

    questions_map = {
        slug: q for slug, q in zip(slugs, question_results) if q is not None
    }

    return submissions, questions_map


def _build_problem_entry(slug: str, subs: List[Any], q: Any) -> Dict[str, Any]:
    """Build a single problem entry dict from its submissions and Question row."""
    tags: List[str] = q.topicTags if q else []
    statuses = [s.status for s in subs]
    total_time = sum(s.timeSpentMinutes or 0 for s in subs)
    return {
        "title_slug": slug,
        "title": q.title if q else slug,
        "difficulty": q.difficulty if q else "Unknown",
        "topic_tags": tags,
        "attempts": len(subs),
        "statuses": statuses,
        "final_status": statuses[-1],
        "total_time_spent_minutes": total_time,
        "first_attempt_at": subs[0].createdAt.isoformat(),
        "final_submission_code": subs[-1].content,
    }


def structure_review_data(
    submissions: List[Any], questions_map: Dict[str, Any]
) -> Dict[str, Any]:
    """Group submissions by problem and compute per-problem details + aggregate stats."""
    grouped: Dict[str, List[Any]] = defaultdict(list)
    for s in submissions:
        grouped[s.titleSlug or "unknown"].append(s)

    problems: List[Dict[str, Any]] = []
    error_type_counts: Dict[str, int] = defaultdict(int)
    total_accepted = 0
    topics_covered: set = set()

    for slug, subs in grouped.items():
        entry = _build_problem_entry(slug, subs, questions_map.get(slug))
        problems.append(entry)

        topics_covered.update(entry["topic_tags"])
        if entry["final_status"] == "Accepted":
            total_accepted += 1
        for status in entry["statuses"]:
            if status != "Accepted":
                error_type_counts[status] += 1

    n_problems = len(problems)
    return {
        "problems": problems,
        "summary_stats": {
            "total_problems_attempted": n_problems,
            "total_accepted": total_accepted,
            "acceptance_rate_pct": (
                round(total_accepted / n_problems * 100, 1) if n_problems else 0.0
            ),
            "total_submissions": len(submissions),
            "error_type_counts": dict(error_type_counts),
            "topics_covered": sorted(topics_covered),
        },
    }


async def review_submissions(
    db: Prisma,
    period: Optional[str] = "today",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Return a structured breakdown of all submissions in a given time window.

    Args:
        db:         Prisma database instance
        period:     Shorthand – 'today', 'yesterday', or 'YYYY-MM-DD'.
                    Ignored when start_date is provided.
        start_date: Explicit range start (ISO date 'YYYY-MM-DD').
        end_date:   Explicit range end, *inclusive* (ISO date 'YYYY-MM-DD').
                    Defaults to start_date when omitted.

    Returns:
        dict with keys:
            period          – human-readable label for the window
            date_range      – {start, end} ISO strings (UTC)
            summary_stats   – aggregate counts and error breakdown
            problems        – per-problem list with attempts, statuses,
                              difficulty, tags, time spent, and final code
    """
    label = start_date or period or "today"
    try:
        start, end, label = resolve_date_range(period, start_date, end_date)
    except ValueError as exc:
        return {"error": str(exc)}

    try:
        submissions, questions_map = await fetch_submissions_in_range(db, start, end)

        if not submissions:
            return {
                "period": label,
                "date_range": {
                    "start": start.isoformat(),
                    "end": end.isoformat(),
                },
                "message": f"No submissions found for '{label}'.",
                "problems": [],
                "summary_stats": {
                    "total_problems_attempted": 0,
                    "total_accepted": 0,
                    "acceptance_rate_pct": 0.0,
                    "total_submissions": 0,
                    "error_type_counts": {},
                    "topics_covered": [],
                },
            }

        structured = structure_review_data(submissions, questions_map)

        return {
            "period": label,
            "date_range": {
                "start": start.isoformat(),
                "end": end.isoformat(),
            },
            **structured,
        }

    except Exception as exc:
        return {
            "error": f"Failed to review submissions: {exc}",
            "period": label,
        }


# === MCP TOOL FUNCTIONS ===


async def get_submission_evolution(db: Prisma, title_slug: str) -> Dict[str, Any]:
    """
    Get the evolution of submissions for a specific LeetCode problem.

    Args:
        db: Prisma database instance
        title_slug: The problem slug (e.g., "two-sum", "best-time-to-buy-and-sell-stock")

    Returns:
        Dictionary containing submission timeline, evolution metrics, and insights
    """
    try:
        # Get all submissions for this problem, ordered by creation time
        submissions = await db.submission.find_many(
            where={"titleSlug": title_slug}, order=[{"createdAt": "asc"}]
        )

        if not submissions:
            return {
                "title_slug": title_slug,
                "total_submissions": 0,
                "message": "No submissions found for this problem",
            }

        # Analyze submission evolution
        evolution_data = {
            "title_slug": title_slug,
            "total_submissions": len(submissions),
            "first_attempt": submissions[0].createdAt.isoformat(),
            "latest_attempt": submissions[-1].createdAt.isoformat(),
            "submissions": [],
        }

        # Extract data for each submission
        for i, submission in enumerate(submissions):
            submission_data = {
                "attempt_number": i + 1,
                "timestamp": submission.createdAt.isoformat(),
                "status": submission.status,
                "code_length": len(submission.content or ""),
                "has_comments": "# " in (submission.content or ""),
                "content_preview": (
                    (submission.content or "")[:200] + "..."
                    if len(submission.content or "") > 200
                    else submission.content
                ),
                "comments_extracted": extract_comments(submission.content or ""),
            }
            evolution_data["submissions"].append(submission_data)

        # Calculate evolution metrics
        evolution_data["metrics"] = calculate_evolution_metrics(submissions)

        return evolution_data

    except Exception as e:
        return {
            "error": f"Failed to get submission evolution: {str(e)}",
            "title_slug": title_slug,
        }


async def analyze_thought_progression(db: Prisma, title_slug: str) -> Dict[str, Any]:
    """
    Analyze how thoughts and comments evolved across submissions for a problem.

    Args:
        db: Prisma database instance
        title_slug: The problem slug

    Returns:
        Analysis of comment evolution and thought progression
    """
    try:
        submissions = await db.submission.find_many(
            where={"titleSlug": title_slug}, order=[{"createdAt": "asc"}]
        )

        if not submissions:
            return {
                "title_slug": title_slug,
                "message": "No submissions found for this problem",
            }

        thought_progression = {
            "title_slug": title_slug,
            "total_submissions": len(submissions),
            "comment_evolution": [],
        }

        for i, submission in enumerate(submissions):
            comments = extract_comments(submission.content or "")

            thought_data = {
                "attempt_number": i + 1,
                "timestamp": submission.createdAt.isoformat(),
                "status": submission.status,
                "comments_count": len(comments),
                "comments": comments,
                "comment_themes": analyze_comment_themes(comments),
                "complexity_mentions": count_complexity_mentions(comments),
            }
            thought_progression["comment_evolution"].append(thought_data)

        # Analyze overall progression
        thought_progression["progression_analysis"] = analyze_overall_progression(
            thought_progression["comment_evolution"]
        )

        return thought_progression

    except Exception as e:
        return {
            "error": f"Failed to analyze thought progression: {str(e)}",
            "title_slug": title_slug,
        }
