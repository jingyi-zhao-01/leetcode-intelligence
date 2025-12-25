import argparse
import asyncio
from datetime import datetime
from typing import List, Dict, Any

from prisma import Prisma
from tabulate import tabulate


async def get_submission_stats(
    limit: int = 50, title_slug: str = None
) -> List[Dict[str, Any]]:
    """
    Retrieve submission statistics from the database.

    Args:
        limit: Maximum number of problems to display
        title_slug: Optional filter by specific problem slug

    Returns:
        List of dictionaries containing submission statistics
    """
    db = Prisma()

    try:
        await db.connect()

        # Build the query filter
        where_clause = {}
        if title_slug:
            where_clause["titleSlug"] = title_slug

        # Get all submissions with their question details
        submissions = await db.submission.find_many(
            where=where_clause,
            order={"createdAt": "desc"},
        )

        if not submissions:
            return []

        # Group submissions by problem slug
        problem_stats: Dict[str, Dict[str, Any]] = {}

        for submission in submissions:
            slug = submission.titleSlug or "Unknown"

            if slug not in problem_stats:
                problem_stats[slug] = {
                    "titleSlug": slug,
                    "difficulty": None,
                    "passed": 0,
                    "failed": 0,
                    "lastSubmission": submission.createdAt,
                    "firstSubmission": submission.createdAt,
                }

            # Count passed vs failed
            if submission.status == "Accepted":
                problem_stats[slug]["passed"] += 1
            else:
                problem_stats[slug]["failed"] += 1

            # Update timestamps
            if submission.createdAt > problem_stats[slug]["lastSubmission"]:
                problem_stats[slug]["lastSubmission"] = submission.createdAt
            if submission.createdAt < problem_stats[slug]["firstSubmission"]:
                problem_stats[slug]["firstSubmission"] = submission.createdAt

        # Get difficulty from Question table
        question_slugs = list(problem_stats.keys())
        questions = await db.question.find_many(
            where={"titleSlug": {"in": question_slugs}}
        )

        question_map = {q.titleSlug: q for q in questions}

        for slug, stats in problem_stats.items():
            if slug in question_map:
                stats["difficulty"] = question_map[slug].difficulty
                stats["title"] = question_map[slug].title
                stats["topicTags"] = question_map[slug].topicTags
            else:
                stats["difficulty"] = "Unknown"
                stats["title"] = slug
                stats["topicTags"] = []

        # Convert to list and sort by last submission date (most recent first)
        stats_list = sorted(
            problem_stats.values(),
            key=lambda x: x["lastSubmission"],
            reverse=True,
        )

        return stats_list[:limit] if not title_slug else stats_list

    except Exception as e:
        print(f"✗ Error retrieving submission stats: {e}", file=sys.stderr)
        return []

    finally:
        await db.disconnect()


async def get_covered_topics() -> Dict[str, int]:
    """Get all unique topic tags with problem counts from solved problems."""
    db = Prisma()

    try:
        await db.connect()

        # Get all accepted submissions only
        submissions = await db.submission.find_many(
            where={"status": "Accepted"},
            order={"createdAt": "desc"},
        )

        if not submissions:
            return {}

        # Get unique problem slugs from accepted submissions
        problem_slugs = list(set(s.titleSlug for s in submissions if s.titleSlug))

        # Get questions with their tags
        questions = await db.question.find_many(
            where={"titleSlug": {"in": problem_slugs}}
        )

        # Count topics
        topic_counts: Dict[str, int] = {}
        for question in questions:
            for tag in question.topicTags:
                topic_counts[tag] = topic_counts.get(tag, 0) + 1

        return topic_counts

    except Exception as e:
        print(f"✗ Error retrieving topics: {e}", file=sys.stderr)
        return {}

    finally:
        await db.disconnect()


async def get_all_topics() -> Dict[str, int]:
    """Get all unique topic tags from all problems in the database."""
    db = Prisma()

    try:
        await db.connect()

        # Get all questions with their tags
        questions = await db.question.find_many()

        if not questions:
            return {}

        # Count topics
        topic_counts: Dict[str, int] = {}
        for question in questions:
            for tag in question.topicTags:
                topic_counts[tag] = topic_counts.get(tag, 0) + 1

        return topic_counts

    except Exception as e:
        print(f"✗ Error retrieving all topics: {e}", file=sys.stderr)
        return {}

    finally:
        await db.disconnect()


async def find_related_problems(
    title_slug: str, limit: int = 10, filter_topics: List[str] = None
) -> Dict[str, Any]:
    """Find problems related to a given problem.

    Args:
        title_slug: The problem slug to find related problems for
        limit: Maximum number of related problems to return
        filter_topics: Optional list of topics - only return problems that have ALL these topics
    """
    db = Prisma()

    try:
        await db.connect()

        # Get the source problem
        source_problem = await db.question.find_unique(where={"titleSlug": title_slug})

        if not source_problem:
            return {"error": f"Problem '{title_slug}' not found in database."}

        related_problems = []

        # 1. Get explicitly related problems from relatedProblems field
        if source_problem.relatedProblems:
            explicit_related = await db.question.find_many(
                where={"titleSlug": {"in": source_problem.relatedProblems[:limit]}}
            )
            for problem in explicit_related:
                # Check if user has solved it
                submission = await db.submission.find_first(
                    where={"titleSlug": problem.titleSlug, "status": "Accepted"},
                    order={"createdAt": "desc"},
                )
                related_problems.append(
                    {
                        "title": problem.title,
                        "titleSlug": problem.titleSlug,
                        "difficulty": problem.difficulty,
                        "topicTags": problem.topicTags,
                        "freqBar": problem.freqBar or 0,
                        "solved": submission is not None,
                        "solvedDate": submission.createdAt if submission else None,
                        "source": "explicit",
                    }
                )

        # 2. Find problems with similar tags
        if len(related_problems) < limit and source_problem.topicTags:
            # Find problems that share at least one tag
            similar_problems = await db.question.find_many(
                where={
                    "titleSlug": {"not": title_slug},
                    "topicTags": {"hasSome": source_problem.topicTags},
                },
                take=limit * 2,  # Get more to filter later
            )

            for problem in similar_problems:
                if problem.titleSlug in [p["titleSlug"] for p in related_problems]:
                    continue

                # Calculate tag overlap
                common_tags = set(problem.topicTags) & set(source_problem.topicTags)
                overlap_score = len(common_tags)

                # Check if user has solved it
                submission = await db.submission.find_first(
                    where={"titleSlug": problem.titleSlug, "status": "Accepted"},
                    order={"createdAt": "desc"},
                )

                related_problems.append(
                    {
                        "title": problem.title,
                        "titleSlug": problem.titleSlug,
                        "difficulty": problem.difficulty,
                        "topicTags": problem.topicTags,
                        "commonTags": list(common_tags),
                        "overlapScore": overlap_score,
                        "freqBar": problem.freqBar or 0,
                        "solved": submission is not None,
                        "solvedDate": submission.createdAt if submission else None,
                        "source": "similar_tags",
                    }
                )

        # Filter by required topics if specified
        if filter_topics:
            related_problems = [
                p
                for p in related_problems
                if all(topic in p["topicTags"] for topic in filter_topics)
            ]

        # Sort by frequency bar (popularity), then overlap score
        related_problems.sort(
            key=lambda x: (
                -x.get("freqBar", 0),  # Higher frequency first
                x.get("overlapScore", 999),  # Then explicit relations
                -len(x.get("commonTags", [])),  # Then by number of common tags
            ),
            reverse=False,
        )

        return {
            "source": {
                "title": source_problem.title,
                "titleSlug": source_problem.titleSlug,
                "difficulty": source_problem.difficulty,
                "topicTags": source_problem.topicTags,
            },
            "related": related_problems[:limit],
        }

    except Exception as e:
        print(f"✗ Error finding related problems: {e}", file=sys.stderr)
        return {"error": str(e)}

    finally:
        await db.disconnect()


async def list_problems_by_topics(
    topics: List[str],
    limit: int = 50,
    only_unsolved: bool = False,
    require_all: bool = False,
) -> List[Dict[str, Any]]:
    """
    List all problems that contain any/all of the specified topics.

    Args:
        topics: List of topic tags to filter by
        limit: Maximum number of problems to return
        only_unsolved: If True, only return unsolved problems
        require_all: If True, require ALL topics (AND). If False, require ANY topic (OR)

    Returns:
        List of problems matching the topics
    """
    db = Prisma()

    try:
        await db.connect()

        # Find problems with any or all of the specified tags
        if require_all:
            # AND logic: problem must have ALL specified tags
            problems = await db.question.find_many(
                where={"topicTags": {"hasEvery": topics}}, take=limit
            )
        else:
            # OR logic: problem must have ANY of the specified tags
            problems = await db.question.find_many(
                where={"topicTags": {"hasSome": topics}}, take=limit
            )

        if not problems:
            return []

        # Check which problems are solved
        problem_list = []
        for problem in problems:
            # Check if user has solved it
            submission = await db.submission.find_first(
                where={"titleSlug": problem.titleSlug, "status": "Accepted"},
                order={"createdAt": "desc"},
            )

            is_solved = submission is not None

            # Skip if filtering for unsolved only
            if only_unsolved and is_solved:
                continue

            # Find which of the requested topics this problem has
            matching_tags = [tag for tag in problem.topicTags if tag in topics]

            problem_list.append(
                {
                    "title": problem.title,
                    "titleSlug": problem.titleSlug,
                    "difficulty": problem.difficulty,
                    "topicTags": problem.topicTags,
                    "matchingTags": matching_tags,
                    "freqBar": problem.freqBar or 0,
                    "solved": is_solved,
                    "solvedDate": submission.createdAt if submission else None,
                }
            )

        # Sort by frequency (most popular first), then by difficulty
        difficulty_order = {"Easy": 1, "Medium": 2, "Hard": 3}
        problem_list.sort(
            key=lambda x: (-x["freqBar"], difficulty_order.get(x["difficulty"], 4))
        )

        return problem_list

    except Exception as e:
        print(f"✗ Error listing problems by topics: {e}", file=sys.stderr)
        return []

    finally:
        await db.disconnect()


def format_date(dt: datetime) -> str:
    """Format datetime for display."""
    return dt.strftime("%Y-%m-%d %H:%M")


def format_stats_table(stats: List[Dict[str, Any]]) -> str:
    """Format statistics as a table."""
    if not stats:
        return "No submissions found."

    # Prepare table data
    headers = [
        "Problem",
        "Difficulty",
        "Tags",
        "Passed",
        "Failed",
        "Total",
        "Success Rate",
        "Last Submission",
    ]
    rows = []

    for stat in stats:
        total = stat["passed"] + stat["failed"]
        success_rate = (stat["passed"] / total * 100) if total > 0 else 0

        # Color coding for difficulty
        difficulty = stat["difficulty"]
        if difficulty == "Easy":
            difficulty_display = f"🟢 {difficulty}"
        elif difficulty == "Medium":
            difficulty_display = f"🟡 {difficulty}"
        elif difficulty == "Hard":
            difficulty_display = f"🔴 {difficulty}"
        else:
            difficulty_display = difficulty

        # Format tags
        tags = stat.get("topicTags", [])
        tags_display = ", ".join(tags[:3]) if tags else "-"
        if len(tags) > 3:
            tags_display += f" (+{len(tags) - 3})"

        rows.append(
            [
                stat.get("title", stat["titleSlug"]),
                difficulty_display,
                tags_display,
                stat["passed"],
                stat["failed"],
                total,
                f"{success_rate:.1f}%",
                format_date(stat["lastSubmission"]),
            ]
        )

    return tabulate(rows, headers=headers, tablefmt="grid")


def format_topics_table(topic_counts: Dict[str, int]) -> str:
    """Format topics as a table."""
    if not topic_counts:
        return "No topics found."

    # Sort by count (descending) then by name
    sorted_topics = sorted(topic_counts.items(), key=lambda x: (-x[1], x[0]))

    headers = ["Topic Tag", "Problem Count"]
    rows = [[tag, count] for tag, count in sorted_topics]

    return tabulate(rows, headers=headers, tablefmt="grid")


def format_problems_by_topics(problems: List[Dict[str, Any]], topics: List[str]) -> str:
    """Format problems by topics as output."""
    if not problems:
        return f"No problems found for topics: {', '.join(topics)}"

    output = []
    output.append(f"\n{'='*80}")
    output.append(f"Problems with topics: {', '.join(topics)}")
    output.append(f"{'='*80}\n")

    # Prepare table data
    headers = [
        "Problem",
        "Difficulty",
        "Frequency",
        "Matching Tags",
        "All Tags",
        "Status",
    ]
    rows = []

    for problem in problems:
        # Format difficulty with color
        difficulty = problem["difficulty"]
        if difficulty == "Easy":
            difficulty_display = f"🟢 {difficulty}"
        elif difficulty == "Medium":
            difficulty_display = f"🟡 {difficulty}"
        elif difficulty == "Hard":
            difficulty_display = f"🔴 {difficulty}"
        else:
            difficulty_display = difficulty

        # Format frequency
        freq_bar = problem.get("freqBar", 0)
        if freq_bar:
            freq_display = f"{freq_bar:.1f}"
        else:
            freq_display = "N/A"

        # Format matching tags (the ones user searched for)
        matching_tags_display = ", ".join(problem["matchingTags"])

        # Format all tags (show all of them)
        all_tags = problem["topicTags"]
        all_tags_display = ", ".join(all_tags) if all_tags else "-"

        # Status with date if solved
        if problem["solved"] and problem.get("solvedDate"):
            solved_date = format_date(problem["solvedDate"])
            status = f"✅ {solved_date}"
        elif problem["solved"]:
            status = "✅ Solved"
        else:
            status = "❌ Unsolved"

        rows.append(
            [
                problem["title"],
                difficulty_display,
                freq_display,
                matching_tags_display,
                all_tags_display,
                status,
            ]
        )

    output.append(tabulate(rows, headers=headers, tablefmt="grid"))
    output.append(f"\nShowing {len(problems)} problem(s)")

    return "\n".join(output)


def format_related_problems(result: Dict[str, Any]) -> str:
    """Format related problems as output."""
    if "error" in result:
        return f"Error: {result['error']}"

    source = result["source"]
    related = result["related"]

    if not related:
        return f"No related problems found for '{source['title']}'."

    output = []
    output.append(f"\n{'='*80}")
    output.append(f"Source Problem: {source['title']} ({source['titleSlug']})")
    output.append(f"Difficulty: {source['difficulty']}")
    output.append(f"Tags: {', '.join(source['topicTags'])}")
    output.append(f"{'='*80}\n")

    # Prepare table data
    headers = ["Problem", "Difficulty", "Frequency", "Common Tags", "Status"]
    rows = []

    for problem in related:
        # Format difficulty with color
        difficulty = problem["difficulty"]
        if difficulty == "Easy":
            difficulty_display = f"🟢 {difficulty}"
        elif difficulty == "Medium":
            difficulty_display = f"🟡 {difficulty}"
        elif difficulty == "Hard":
            difficulty_display = f"🔴 {difficulty}"
        else:
            difficulty_display = difficulty

        # Format frequency
        freq_bar = problem.get("freqBar", 0)
        if freq_bar:
            freq_display = f"{freq_bar:.1f}"
        else:
            freq_display = "N/A"

        # Format common tags
        if problem["source"] == "explicit":
            common_tags_display = "(Related by LeetCode)"
        else:
            common_tags = problem.get("commonTags", [])
            common_tags_display = ", ".join(common_tags[:3])
            if len(common_tags) > 3:
                common_tags_display += f" (+{len(common_tags) - 3})"

        # Status with date if solved
        if problem["solved"] and problem.get("solvedDate"):
            solved_date = format_date(problem["solvedDate"])
            status = f"✅ {solved_date}"
        elif problem["solved"]:
            status = "✅ Solved"
        else:
            status = "❌ Unsolved"

        rows.append(
            [
                problem["title"],
                difficulty_display,
                freq_display,
                common_tags_display,
                status,
            ]
        )

    output.append(tabulate(rows, headers=headers, tablefmt="grid"))
    output.append(f"\nShowing {len(related)} related problem(s)")

    return "\n".join(output)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="View LeetCode submission statistics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View all submission stats
  python -m src.submissions.submission_stats

  # View stats for specific problem
  python -m src.submissions.submission_stats --problem two-sum

  # View more results
  python -m src.submissions.submission_stats --limit 100

  # List topic tags from solved problems
  python -m src.submissions.submission_stats --list-topics

  # List all topic tags from all problems in database
  python -m src.submissions.submission_stats --list-all-topics

  # Find related problems for a specific problem
  python -m src.submissions.submission_stats --find-related two-sum

  # Find related problems filtered by topics (must have ALL specified topics)
  python -m src.submissions.submission_stats --find-related is-subsequence --filter-topics "two-pointers" "string"

  # List problems by topics (OR logic - any of the tags)
  python -m src.submissions.submission_stats --by-topics "Array" "Hash Table"

  # List problems that have ALL specified topics (AND logic)
  python -m src.submissions.submission_stats --by-topics "Array" "Two Pointers" --require-all-topics

  # List unsolved problems by topics
  python -m src.submissions.submission_stats --by-topics "Dynamic Programming" --unsolved-only
        """,
    )

    parser.add_argument(
        "--problem",
        "--title-slug",
        dest="title_slug",
        help="Filter by specific problem slug",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of problems to display (default: 50)",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="List topic tags from solved problems (with accepted submissions)",
    )
    parser.add_argument(
        "--list-all-topics",
        action="store_true",
        help="List all topic tags from all problems in the database",
    )
    parser.add_argument(
        "--find-related",
        type=str,
        metavar="PROBLEM_SLUG",
        help="Find related problems for a specific problem slug",
    )
    parser.add_argument(
        "--filter-topics",
        nargs="+",
        metavar="TOPIC",
        help="When used with --find-related, filter results to only show problems with ALL these topics",
    )
    parser.add_argument(
        "--by-topics",
        nargs="+",
        metavar="TOPIC",
        help="List problems by topic tags (accepts multiple topics)",
    )
    parser.add_argument(
        "--unsolved-only",
        action="store_true",
        help="When used with --by-topics, only show unsolved problems",
    )
    parser.add_argument(
        "--require-all-topics",
        action="store_true",
        help="When used with --by-topics, require ALL topics (AND logic instead of OR)",
    )

    args = parser.parse_args()

    # Handle by-topics mode
    if args.by_topics:
        problems = asyncio.run(
            list_problems_by_topics(
                args.by_topics, args.limit, args.unsolved_only, args.require_all_topics
            )
        )
        if problems:
            print(format_problems_by_topics(problems, args.by_topics))
        else:
            filter_msg = " unsolved" if args.unsolved_only else ""
            print(
                f"No{filter_msg} problems found for topics: {', '.join(args.by_topics)}"
            )
        return

    # Handle find-related mode
    if args.find_related:
        result = asyncio.run(
            find_related_problems(args.find_related, args.limit, args.filter_topics)
        )
        print(format_related_problems(result))
        return

    # Handle list-all-topics mode
    if args.list_all_topics:
        topic_counts = asyncio.run(get_all_topics())
        if topic_counts:
            print(format_topics_table(topic_counts))
            print(f"\nTotal unique topics in database: {len(topic_counts)}")
        else:
            print("No topics found in database.")
        return

    # Handle list-topics mode
    if args.list_topics:
        topic_counts = asyncio.run(get_covered_topics())
        if topic_counts:
            print(format_topics_table(topic_counts))
            print(f"\nTotal unique topics covered: {len(topic_counts)}")
        else:
            print("No topics found in solved problems.")
        return

    # Run the async function
    stats = asyncio.run(get_submission_stats(args.limit, args.title_slug))

    if stats:
        print(format_stats_table(stats))
        print(f"\nShowing {len(stats)} problem(s)")
    else:
        print("No submissions found.")


if __name__ == "__main__":
    main()
