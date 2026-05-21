#!/usr/bin/env python3
"""
Debug script to check what's in the database and test our MCP functions.
"""

import asyncio
import sys
import os

# Add project root to the Python path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from prisma import Prisma

# Initialize database connection
debug_db = Prisma()


async def check_database_contents():
    """Check what submissions are in the database."""
    print("🔍 Checking database contents...")

    await debug_db.connect()

    try:
        # Get all submissions
        all_submissions = await debug_db.submission.find_many(
            order=[{"createdAt": "asc"}]
        )

        print(f"Total submissions in database: {len(all_submissions)}")

        for i, sub in enumerate(all_submissions):
            print(
                f"  {i+1}. Title: {sub.titleSlug}, Status: {sub.status}, Created: {sub.createdAt}"
            )
            print(f"     Content preview: {(sub.content or '')[:100]}...")