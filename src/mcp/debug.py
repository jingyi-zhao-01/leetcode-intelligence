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

        # Check specifically for two-sum
        two_sum_submissions = await debug_db.submission.find_many(
            where={"titleSlug": "two-sum"}, order=[{"createdAt": "asc"}]
        )

        print(f"\nTwo-sum submissions: {len(two_sum_submissions)}")
        for i, sub in enumerate(two_sum_submissions):
            print(f"  {i+1}. Status: {sub.status}, Created: {sub.createdAt}")

    finally:
        await debug_db.disconnect()


async def test_submission_evolution_debug():
    """Debug version of submission evolution test."""
    print("\n🐛 Testing submission evolution with debug info...")

    await debug_db.connect()

    try:
        title_slug = "two-sum"

        # Get submissions step by step with debug info
        print(f"Looking for submissions with titleSlug: '{title_slug}'")

        submissions = await debug_db.submission.find_many(
            where={"titleSlug": title_slug}, order=[{"createdAt": "asc"}]
        )

        print(f"Found {len(submissions)} submissions")

        if not submissions:
            print("❌ No submissions found - checking if any submissions exist at all")
            all_subs = await debug_db.submission.find_many()
            print(f"Total submissions in DB: {len(all_subs)}")
            if all_subs:
                print("Available titleSlugs:")
                for sub in all_subs:
                    print(f"  - '{sub.titleSlug}'")
            return

        # Process the submissions
        evolution_data = {
            "title_slug": title_slug,
            "total_submissions": len(submissions),
            "first_attempt": submissions[0].createdAt.isoformat(),
            "latest_attempt": submissions[-1].createdAt.isoformat(),
            "submissions": [],
        }

        print(f"✅ Processing {len(submissions)} submissions...")

        for i, submission in enumerate(submissions):
            print(f"  Processing submission {i+1}: {submission.status}")

            submission_data = {
                "attempt_number": i + 1,
                "timestamp": submission.createdAt.isoformat(),
                "status": submission.status,
                "code_length": len(submission.content or ""),
                "has_comments": "# " in (submission.content or ""),
            }
            evolution_data["submissions"].append(submission_data)

        print("\n📊 Evolution Data:")
        print(f"  Title: {evolution_data['title_slug']}")
        print(f"  Total submissions: {evolution_data['total_submissions']}")
        print(f"  First attempt: {evolution_data['first_attempt']}")
        print(f"  Latest attempt: {evolution_data['latest_attempt']}")

        for sub_data in evolution_data["submissions"]:
            print(
                f"    Attempt {sub_data['attempt_number']}: {sub_data['status']} ({sub_data['code_length']} chars)"
            )

    finally:
        await debug_db.disconnect()


async def main():
    """Main debug function."""
    print("🐛 Starting MCP Debug Session")
    print("=" * 50)

    await check_database_contents()
    await test_submission_evolution_debug()

    print("\n🎉 Debug session completed!")


if __name__ == "__main__":
    asyncio.run(main())
