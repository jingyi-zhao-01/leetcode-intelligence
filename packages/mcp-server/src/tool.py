"""
LeetCode Submission Evolution Tools
Provides functionality for analyzing submission evolution and thought progression.
"""

from typing import Dict, Any
from prisma import Prisma
from util import (
    extract_comments,
    analyze_comment_themes,
    count_complexity_mentions,
    calculate_evolution_metrics,
    analyze_overall_progression,
)


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
