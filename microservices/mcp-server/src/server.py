#!/usr/bin/env python3
"""
LeetCode Submission History MCP Server
Provides two main tools for analyzing LeetCode submissions:
- get_submission_history: List all submissions for a specific problem
- analyze_thought_progression: Comment and approach evolution analysis
"""

import asyncio
import sys
import os
import subprocess
from prisma import Prisma

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
from read_tools import register_read_tools
from write_tools import register_write_tools

# Create FastMCP server with submission evolution tools
mcp = FastMCP(name="LeetCode Submission Evolution Server 🚀")

# Global Prisma instance for submission tools
db = Prisma()


async def ensure_db_connected():
    """Ensure database connection is established."""
    if not db.is_connected():
        await db.connect()


# Register CRUD-style Read tools from a dedicated module.
register_read_tools(mcp, db, ensure_db_connected)

# Register CRUD-style Write tools from a dedicated module.
register_write_tools(mcp, db, ensure_db_connected)
