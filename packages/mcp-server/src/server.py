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
from typing import Dict, Any
from prisma import Prisma

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
from tool import (
    get_submission_evolution as get_submission_evolution_impl,
    analyze_thought_progression as analyze_thought_progression_impl,
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
