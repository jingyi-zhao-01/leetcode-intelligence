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
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from leetcode_mcp.server import (
    db,
    get_submission_evolution,
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
    # Try every pair of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []""",
            "status": "Time Limit Exceeded",
        },
        {
            "titleSlug": "two-sum",
            "content": """# Second attempt - using hash map for optimization
# Time complexity: O(n), Space complexity: O(n)
def twoSum(nums, target):
    # Use hash map to store complements
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []""",
            "status": "Accepted",
        },
    ]

    for submission_data in test_submissions:
        await db.submission.create(data=submission_data)

    print("✅ Test data created successfully!")


async def test_get_submission_evolution():
    """Test the get_submission_evolution function."""
    print("\n📊 Testing get_submission_evolution...")

    result = await get_submission_evolution("two-sum")

    print(f"Title slug: {result.get('title_slug')}")
    print(f"Total submissions: {result.get('total_submissions')}")
    print(f"First attempt: {result.get('first_attempt')}")
    print(f"Latest attempt: {result.get('latest_attempt')}")

    if result.get("submissions"):
        for i, sub in enumerate(result["submissions"]):
            print(f"  Attempt {i+1}: {sub['status']} ({sub['code_length']} chars)")

    if result.get("metrics"):
        metrics = result["metrics"]
        print(f"Final success rate: {metrics.get('final_success_rate'):.2f}")
        print(f"Attempts to success: {metrics.get('attempts_to_success')}")


async def test_analyze_thought_progression():
    """Test the analyze_thought_progression function."""
    print("\n🧠 Testing analyze_thought_progression...")

    result = await analyze_thought_progression("two-sum")

    print(f"Title slug: {result.get('title_slug')}")
    print(f"Total submissions: {result.get('total_submissions')}")

    if result.get("comment_evolution"):
        for i, evolution in enumerate(result["comment_evolution"]):
            print(f"  Attempt {i+1}:")
            print(f"    Comments: {evolution['comments_count']}")
            print(f"    Themes: {evolution['comment_themes']}")
            print(f"    Complexity mentions: {evolution['complexity_mentions']}")


async def cleanup_test_data():
    """Clean up test data."""
    print("\n🧹 Cleaning up test data...")

    await db.submission.delete_many(where={"titleSlug": "two-sum"})

    await db.disconnect()
    print("✅ Cleanup completed!")


async def main():
    """Main test function."""
    print("🚀 Starting MCP Submission Evolution Tests")
    print("=" * 50)

    try:
        await setup_test_data()
        await test_get_submission_evolution()
        await test_analyze_thought_progression()
    finally:
        await cleanup_test_data()

    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    asyncio.run(main())
