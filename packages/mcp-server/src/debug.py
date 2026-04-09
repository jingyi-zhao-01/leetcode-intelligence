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


async def test_submission_history_debug():
    """Debug version of submission history test."""
    print("\n🐛 Testing submission history with debug info...")

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

        history = {
            "title_slug": title_slug,
            "total_submissions": len(submissions),
            "submissions": [],
        }

        print(f"✅ Processing {len(submissions)} submissions...")

        for submission in submissions:
            print(f"  Processing submission: {submission.id} - {submission.status}")
            history["submissions"].append(
                {
                    "submissionId": submission.id,
                    "submittedCode": submission.content or "",
                    "result": submission.status,
                    "mistakes": submission.mistake,
                    "time": submission.createdAt.isoformat(),
                }
            )

        print("\n📊 Submission History:")
        print(f"  Title: {history['title_slug']}")
        print(f"  Total submissions: {history['total_submissions']}")

        for sub_data in history["submissions"]:
            print(
                f"    [{sub_data['submissionId']}] {sub_data['result']} @ {sub_data['time']}"
            )

    finally:
        await debug_db.disconnect()


async def main():
    """Main debug function."""
    print("🐛 Starting MCP Debug Session")
    print("=" * 50)

    await check_database_contents()
    await test_submission_history_debug()

    print("\n🎉 Debug session completed!")


if __name__ == "__main__":
    asyncio.run(main())
