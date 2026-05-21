#!/usr/bin/env python3
"""
Test script for the MCP submission evolution tools.
This simulates how an MCP client would interact with our server.
"""

import asyncio
import sys
import os

# Add project root to the Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)

from server import (
    db,
    get_submission_history,
    analyze_thought_progression,
)


async def setup_test_data():
    """Setup some test submissions in the database."""
    print("🔧 Setting up test data...")

    await db.connect()

    # Clean up existing test data
    await db.submission.delete_many(where={"titleSlug": "two-sum"})

    # Create test submissions for "two-sum" problem
    test_submissions = [
        {
            "titleSlug": "two-sum",
            "content": """# First attempt - brute force approach
# Time complexity: O(n^2), Space complexity: O(1)
def twoSum(nums, target):