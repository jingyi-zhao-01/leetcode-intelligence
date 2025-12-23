import argparse
import asyncio
import json
import sys
from pathlib import Path

from prisma import Prisma, Json

from src.submissions.code_cleaner import normalize_for_embedding

# Add the project root to the path to import src modules
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


async def save_submission(title_slug: str, content: str, item: dict) -> bool:
    """
    Save a submission to the database.

    Args:
        title_slug: The LeetCode problem slug (e.g., "two-sum")
        content: The submission code content
        status: The submission status (e.g., "Accepted", "Wrong_Answer", "Time_Limit_Exceeded")

    Returns:
        True if successful, False otherwise
    """
    db = Prisma()

    status = item.get("status_msg", "Unknown")

    # Skip if content contains #TEST#
    if "#TEST#" in content:
        print(f"⊘ Skipping test submission: {title_slug}", file=sys.stderr)
        return False

    # Check if content contains #CHEAT# flag
    is_cheat = "#CHEAT#" in content

    try:
        await db.connect()

        # Clean and normalize the code for better embeddings
        cleaned_content = normalize_for_embedding(content)

        # Create the submission record
        submission = await db.submission.create(
            data={
                "titleSlug": title_slug,
                "content": cleaned_content,
                "status": status,
                "isCheat": is_cheat,
                "submissionDetails": Json(item) if item else None,
            }
        )

        cheat_flag = " [CHEAT - needs revisit]" if is_cheat else ""
        print(
            f"✓ Submission saved successfully: {submission.id} {title_slug} {status}{cheat_flag}"
        )

        return True

    except Exception as e:
        print(f"✗ Error saving submission: {e}", file=sys.stderr)
        return False

    finally:
        await db.disconnect()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Save LeetCode submission to database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.submissions.submission_saver \\
    --title-slug two-sum \\
    --content "def twoSum(nums, target):\\n    return []" \\
    --status "Accepted"
        """,
    )

    parser.add_argument("--title-slug", required=True, help="LeetCode problem slug")
    parser.add_argument("--content", required=True, help="Submission code content")
    parser.add_argument(
        "--item",
        required=True,
        help="JSON string containing the full item object with status and other fields",
    )
    args = parser.parse_args()

    # Parse the item JSON string
    try:
        item = json.loads(args.item)
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing item JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Run the async function
    success = asyncio.run(save_submission(args.title_slug, args.content, item))

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
