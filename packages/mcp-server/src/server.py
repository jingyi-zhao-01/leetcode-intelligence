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
from typing import Dict, Any, Optional
from prisma import Prisma

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
from tool import (
    get_submission_evolution as get_submission_evolution_impl,
    analyze_thought_progression as analyze_thought_progression_impl,
    review_submissions as review_submissions_impl,
)

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
    return await get_submission_evolution_impl(db, title_slug)


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
    return await analyze_thought_progression_impl(db, title_slug)


@mcp.tool
async def review_submissions(
    period: str = "today",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Return a structured breakdown of all LeetCode submissions in a time window
    so the client can generate a summary, error analysis, and improvement advice.

    Time window (pick one mode):

    Shorthand via `period`:
        - "today"      – current calendar day (UTC)
        - "yesterday"  – previous calendar day (UTC)
        - "YYYY-MM-DD" – a specific single day

    Explicit range via `start_date` / `end_date`:
        - start_date: ISO date string, e.g. "2026-02-01"  (required for range mode)
        - end_date:   ISO date string, inclusive, e.g. "2026-02-22"  (optional;
                      defaults to start_date, giving a single-day window)
        When start_date is provided it takes precedence over `period`.

    Returns:
        {
          period:         str,   # human-readable label for the window
          date_range:     {start: ISO str, end: ISO str},
          summary_stats:  {
              total_problems_attempted: int,
              total_accepted:           int,
              acceptance_rate_pct:      float,
              total_submissions:        int,
              error_type_counts:        {status: count},
              topics_covered:           [str]
          },
          problems: [
            {
              title_slug:               str,
              title:                    str,
              difficulty:               str,
              topic_tags:               [str],
              attempts:                 int,
              statuses:                 [str],   # ordered chronologically
              final_status:             str,
              total_time_spent_minutes: int,
              first_attempt_at:         ISO str,
              final_submission_code:    str
            }
          ]
        }
    """
    await ensure_db_connected()
    return await review_submissions_impl(db, period, start_date, end_date)


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
