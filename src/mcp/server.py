#!/usr/bin/env python3
"""
LeetCode Submission Evolution MCP Server
Provides two main tools for analyzing LeetCode submission evolution:
- get_submission_evolution: Timeline and metrics for a specific problem
- analyze_thought_progression: Comment and approach evolution analysis
"""

import asyncio
import sys
import os
from typing import List, Dict, Any
from prisma import Prisma

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP

# Create FastMCP server with submission evolution tools
mcp = FastMCP(name="LeetCode Submission Evolution Server 🚀")

# Global Prisma instance for submission tools
db = Prisma()


async def ensure_db_connected():
    """Ensure database connection is established."""
    if not db.is_connected():
        await db.connect()


# === ORIGINAL DICE TOOLS ===


# === LEETCODE SUBMISSION EVOLUTION TOOLS ===


@mcp.tool
async def get_submission_evolution(title_slug: str) -> Dict[str, Any]:
    """
    Get the evolution of submissions for a specific LeetCode problem.

    Args:
        title_slug: The problem slug (e.g., "two-sum", "best-time-to-buy-and-sell-stock")

    Returns:
        Dictionary containing submission timeline, evolution metrics, and insights
    """
    await ensure_db_connected()

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
                "comments_extracted": _extract_comments(submission.content or ""),
            }
            evolution_data["submissions"].append(submission_data)

        # Calculate evolution metrics
        evolution_data["metrics"] = _calculate_evolution_metrics(submissions)

        return evolution_data

    except Exception as e:
        return {
            "error": f"Failed to get submission evolution: {str(e)}",
            "title_slug": title_slug,
        }


@mcp.tool
async def analyze_thought_progression(title_slug: str) -> Dict[str, Any]:
    """
    Analyze how thoughts and comments evolved across submissions for a problem.

    Args:
        title_slug: The problem slug

    Returns:
        Analysis of comment evolution and thought progression
    """
    await ensure_db_connected()

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
            comments = _extract_comments(submission.content or "")

            thought_data = {
                "attempt_number": i + 1,
                "timestamp": submission.createdAt.isoformat(),
                "status": submission.status,
                "comments_count": len(comments),
                "comments": comments,
                "comment_themes": _analyze_comment_themes(comments),
                "complexity_mentions": _count_complexity_mentions(comments),
            }
            thought_progression["comment_evolution"].append(thought_data)

        # Analyze overall progression
        thought_progression["progression_analysis"] = _analyze_overall_progression(
            thought_progression["comment_evolution"]
        )

        return thought_progression

    except Exception as e:
        return {
            "error": f"Failed to analyze thought progression: {str(e)}",
            "title_slug": title_slug,
        }


# === HELPER FUNCTIONS ===


def _extract_comments(code: str) -> List[str]:
    """Extract comments from code."""
    lines = code.split("\n")
    comments = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            comments.append(line[1:].strip())
    return comments


def _analyze_comment_themes(comments: List[str]) -> Dict[str, int]:
    """Analyze themes in comments."""
    themes = {
        "algorithmic_thinking": 0,
        "optimization": 0,
        "edge_cases": 0,
        "complexity_analysis": 0,
        "debugging": 0,
    }

    for comment in comments:
        comment_lower = comment.lower()

        if any(
            word in comment_lower
            for word in ["algorithm", "approach", "strategy", "method"]
        ):
            themes["algorithmic_thinking"] += 1
        if any(
            word in comment_lower
            for word in ["optimize", "faster", "better", "improve"]
        ):
            themes["optimization"] += 1
        if any(
            word in comment_lower for word in ["edge", "corner", "special", "boundary"]
        ):
            themes["edge_cases"] += 1
        if any(
            word in comment_lower
            for word in ["time", "space", "complexity", "o(", "big o"]
        ):
            themes["complexity_analysis"] += 1
        if any(
            word in comment_lower for word in ["debug", "fix", "error", "bug", "issue"]
        ):
            themes["debugging"] += 1

    return themes


def _count_complexity_mentions(comments: List[str]) -> Dict[str, int]:
    """Count complexity-related mentions in comments."""
    complexity_counts = {"time_complexity": 0, "space_complexity": 0}

    for comment in comments:
        comment_lower = comment.lower()
        if "time" in comment_lower and (
            "complexity" in comment_lower or "o(" in comment_lower
        ):
            complexity_counts["time_complexity"] += 1
        if "space" in comment_lower and (
            "complexity" in comment_lower or "o(" in comment_lower
        ):
            complexity_counts["space_complexity"] += 1

    return complexity_counts


def _calculate_evolution_metrics(submissions) -> Dict[str, Any]:
    """Calculate evolution metrics for submissions."""
    success_rate_over_time = []
    code_length_trend = []

    for i, sub in enumerate(submissions):
        # Success rate up to this point
        successes = sum(1 for s in submissions[: i + 1] if s.status == "Accepted")
        success_rate = successes / (i + 1)
        success_rate_over_time.append(success_rate)

        # Code length trend
        code_length_trend.append(len(sub.content or ""))

    return {
        "success_rate_progression": success_rate_over_time,
        "code_length_trend": code_length_trend,
        "final_success_rate": (
            success_rate_over_time[-1] if success_rate_over_time else 0
        ),
        "attempts_to_success": next(
            (i + 1 for i, sub in enumerate(submissions) if sub.status == "Accepted"),
            None,
        ),
        "total_attempts": len(submissions),
    }


def _analyze_overall_progression(comment_evolution) -> Dict[str, Any]:
    """Analyze overall thought progression."""
    if not comment_evolution:
        return {}

    first_themes = comment_evolution[0].get("comment_themes", {})
    last_themes = comment_evolution[-1].get("comment_themes", {})

    theme_progression = {}
    for theme in first_themes:
        theme_progression[theme] = last_themes.get(theme, 0) - first_themes.get(
            theme, 0
        )

    return {
        "theme_development": theme_progression,
        "comment_density_trend": [item["comments_count"] for item in comment_evolution],
        "complexity_awareness_growth": sum(
            item["complexity_mentions"]["time_complexity"]
            + item["complexity_mentions"]["space_complexity"]
            for item in comment_evolution
        ),
    }


# === SERVER STARTUP ===


async def startup():
    """Initialize database connection."""
    await db.connect()
    print("✅ Database connected")


async def shutdown():
    """Clean up database connection."""
    await db.disconnect()
    print("✅ Database disconnected")


def main():
    """Main entry point for the MCP HTTP server."""

    try:
        # The FastMCP framework will handle the event loop
        mcp.run(transport="http", port=8000)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")

    # Clean shutdown
    try:
        asyncio.run(shutdown())
    except Exception:
        pass


def main_stdio():
    """Main entry point for the MCP stdio server (for GitHub Copilot)."""
    try:
        # Run the MCP server using stdio transport for Copilot
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
