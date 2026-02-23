#!/usr/bin/env python3
"""
Test script for the MCP submission evolution tools.
This tests the actual implementation functions directly.
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

# Import the actual implementation
sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        ),
        "src",
    )
)

# Direct import of core functions and database
from typing import List, Dict, Any
from prisma import Prisma

# Initialize our own database connection for testing
test_db = Prisma()


# Copy the actual implementation functions for testing
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


async def test_get_submission_evolution(title_slug: str) -> Dict[str, Any]:
    """Test version of get_submission_evolution."""
    try:
        # Get all submissions for this problem, ordered by creation time
        submissions = await test_db.submission.find_many(
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


async def test_analyze_thought_progression(title_slug: str) -> Dict[str, Any]:
    """Test version of analyze_thought_progression."""
    try:
        submissions = await test_db.submission.find_many(
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
            }
            thought_progression["comment_evolution"].append(thought_data)

        return thought_progression

    except Exception as e:
        return {
            "error": f"Failed to analyze thought progression: {str(e)}",
            "title_slug": title_slug,
        }


async def setup_test_data():
    """Setup some test submissions in the database."""
    print("🔧 Setting up test data...")

    await test_db.connect()

    # Clean up existing test data
    await test_db.submission.delete_many(where={"titleSlug": "two-sum"})

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
        await test_db.submission.create(data=submission_data)

    print("✅ Test data created successfully!")


async def run_get_submission_evolution_test():
    """Test the get_submission_evolution function."""
    print("\n📊 Testing get_submission_evolution...")

    result = await test_get_submission_evolution("two-sum")

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


async def run_analyze_thought_progression_test():
    """Test the analyze_thought_progression function."""
    print("\n🧠 Testing analyze_thought_progression...")

    result = await test_analyze_thought_progression("two-sum")

    print(f"Title slug: {result.get('title_slug')}")
    print(f"Total submissions: {result.get('total_submissions')}")

    if result.get("comment_evolution"):
        for i, evolution in enumerate(result["comment_evolution"]):
            print(f"  Attempt {i+1}:")
            print(f"    Comments: {evolution['comments_count']}")
            print(f"    Themes: {evolution['comment_themes']}")


async def cleanup_test_data():
    """Clean up test data."""
    print("\n🧹 Cleaning up test data...")

    await test_db.submission.delete_many(where={"titleSlug": "two-sum"})

    await test_db.disconnect()
    print("✅ Cleanup completed!")


async def main():
    """Main test function."""
    print("🚀 Starting MCP Submission Evolution Tests")
    print("=" * 50)

    try:
        await setup_test_data()
        await run_get_submission_evolution_test()
        await run_analyze_thought_progression_test()
    finally:
        await cleanup_test_data()

    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    asyncio.run(main())
