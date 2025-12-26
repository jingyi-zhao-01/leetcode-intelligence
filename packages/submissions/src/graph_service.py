"""Graph service for building problem relationship graphs."""

import sys
from typing import List, Dict, Optional, Any
from collections import defaultdict

from prisma import Prisma

# Configuration: Minimum shared tags required for tag similarity edges
MIN_SHARED_TAGS_FOR_EDGE = 3


async def build_graph_data(
    solved: bool = False,
    include_tags: Optional[List[str]] = None,
    filter_tags: Optional[List[str]] = None,
    difficulties: Optional[List[str]] = None,
    limit: int = 3000,
) -> Dict[str, Any]:
    """
    Build a graph of problem connections with acceptance rates.

    Args:
        solved: If True, only include solved problems
        include_tags: If provided, include problems with ANY of these tags (OR logic)
        filter_tags: If provided, only include problems with ALL of these tags (AND logic)
        difficulties: If provided, only include problems with these difficulties
        limit: Maximum number of problems to include

    Returns:
        Dictionary containing nodes, edges, and stats
    """
    db = Prisma()

    try:
        await db.connect()

        # Build where clause for problems
        where_clause = {}
        problem_slugs = None

        if solved:
            # Get solved problem slugs
            submissions = await db.submission.find_many(
                where={"status": "Accepted"},
                distinct=["titleSlug"],
            )
            problem_slugs = [s.titleSlug for s in submissions if s.titleSlug]
            if problem_slugs:
                where_clause["titleSlug"] = {"in": problem_slugs}
            else:
                return {
                    "nodes": [],
                    "edges": [],
                    "stats": {
                        "totalProblems": 0,
                        "totalMatching": 0,
                        "totalEdges": 0,
                        "explicitEdges": 0,
                        "tagEdges": 0,
                        "solvedProblems": 0,
                        "unsolvedProblems": 0,
                    },
                }

        # Add difficulty filter to where clause
        if difficulties:
            where_clause["difficulty"] = {"in": difficulties}

        # Get ALL problems matching database-level filters (no limit yet)
        # We'll apply limit after in-memory tag filtering
        problems = await db.question.find_many(where=where_clause)

        if not problems:
            return {
                "nodes": [],
                "edges": [],
                "stats": {
                    "totalProblems": 0,
                    "totalMatching": 0,
                    "totalEdges": 0,
                    "explicitEdges": 0,
                    "tagEdges": 0,
                    "solvedProblems": 0,
                    "unsolvedProblems": 0,
                },
            }

        # Filter by include_tags (OR logic - has ANY of the tags)
        if include_tags:
            problems = [
                p for p in problems if any(tag in p.topicTags for tag in include_tags)
            ]

        # Filter by filter_tags (AND logic - has ALL of the tags)
        if filter_tags:
            problems = [
                p for p in problems if all(tag in p.topicTags for tag in filter_tags)
            ]

        # Store total matching count before applying limit
        total_matching = len(problems)

        # Apply limit after all filters
        problems = problems[:limit]

        # Get submission data for all problems in one query
        all_submissions = await db.submission.find_many(
            where={"titleSlug": {"in": [p.titleSlug for p in problems]}}
        )

        # Group submissions by titleSlug and status
        submission_stats = defaultdict(lambda: {"total": 0, "accepted": 0})
        for sub in all_submissions:
            if sub.titleSlug:
                submission_stats[sub.titleSlug]["total"] += 1
                if sub.status == "Accepted":
                    submission_stats[sub.titleSlug]["accepted"] += 1

        # Build nodes
        nodes = []
        slug_to_idx = {}
        solved_slugs = set(
            s.titleSlug
            for s in all_submissions
            if s.status == "Accepted" and s.titleSlug
        )

        for idx, problem in enumerate(problems):
            slug_to_idx[problem.titleSlug] = idx

            stats = submission_stats[problem.titleSlug]
            acceptance_rate = (
                (stats["accepted"] / stats["total"] * 100)
                if stats["total"] > 0
                else 0.0
            )

            nodes.append(
                {
                    "id": idx,
                    "title": problem.title,
                    "titleSlug": problem.titleSlug,
                    "difficulty": problem.difficulty,
                    "tags": problem.topicTags,
                    "acceptanceRate": round(acceptance_rate, 2),
                    "totalSubmissions": stats["total"],
                    "solved": problem.titleSlug in solved_slugs,
                    "freqBar": problem.freqBar or 0.0,
                }
            )

        # TODO: Add centralizing logic for solved problems

        # Build edges based on explicit relationships
        edges = []
        edge_set = set()

        for problem in problems:
            if problem.relatedProblems:
                source_idx = slug_to_idx.get(problem.titleSlug)
                if source_idx is not None:
                    for related_slug in problem.relatedProblems:
                        target_idx = slug_to_idx.get(related_slug)
                        if target_idx is not None:
                            # Create undirected edge (dedupe)
                            edge_pair = tuple(sorted([source_idx, target_idx]))
                            if edge_pair not in edge_set:
                                edge_set.add(edge_pair)
                                edges.append(
                                    {
                                        "source": source_idx,
                                        "target": target_idx,
                                        "type": "explicit",
                                        "sharedTags": None,
                                    }
                                )

        # Build edges based on shared tags (2+ tags in common)
        tag_to_problems = defaultdict(list)
        for idx, problem in enumerate(problems):
            for tag in problem.topicTags:
                tag_to_problems[tag].append(idx)

        for tag, problem_indices in tag_to_problems.items():
            if len(problem_indices) > 1:
                for i in range(len(problem_indices)):
                    for j in range(i + 1, len(problem_indices)):
                        idx1, idx2 = problem_indices[i], problem_indices[j]
                        edge_pair = tuple(sorted([idx1, idx2]))

                        # Count shared tags
                        tags1 = set(problems[idx1].topicTags)
                        tags2 = set(problems[idx2].topicTags)
                        shared_count = len(tags1 & tags2)

                        # Only create edge if they share MIN_SHARED_TAGS_FOR_EDGE+ tags and not already connected
                        if (
                            shared_count >= MIN_SHARED_TAGS_FOR_EDGE
                            and edge_pair not in edge_set
                        ):
                            edge_set.add(edge_pair)
                            edges.append(
                                {
                                    "source": idx1,
                                    "target": idx2,
                                    "type": "tag_similarity",
                                    "sharedTags": shared_count,
                                }
                            )

        # Calculate stats
        solved_count = sum(1 for n in nodes if n["solved"])
        stats = {
            "totalProblems": len(nodes),
            "totalMatching": total_matching,
            "totalEdges": len(edges),
            "explicitEdges": sum(1 for e in edges if e["type"] == "explicit"),
            "tagEdges": sum(1 for e in edges if e["type"] == "tag_similarity"),
            "solvedProblems": solved_count,
            "unsolvedProblems": len(nodes) - solved_count,
        }

        return {"nodes": nodes, "edges": edges, "stats": stats}

    except Exception as e:
        print(f"✗ Error building problem graph: {e}", file=sys.stderr)
        return {
            "nodes": [],
            "edges": [],
            "stats": {
                "totalProblems": 0,
                "totalMatching": 0,
                "totalEdges": 0,
                "explicitEdges": 0,
                "tagEdges": 0,
                "solvedProblems": 0,
                "unsolvedProblems": 0,
            },
        }

    finally:
        await db.disconnect()


async def get_problem_details(title_slug: str) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a specific problem.

    Args:
        title_slug: The problem's unique slug

    Returns:
        Dictionary with problem details and submission history
    """
    db = Prisma()

    try:
        await db.connect()

        # Get problem
        problem = await db.question.find_unique(where={"titleSlug": title_slug})
        if not problem:
            return None

        # Get all submissions for this problem
        submissions = await db.submission.find_many(
            where={"titleSlug": title_slug}, order={"createdAt": "desc"}
        )

        # Calculate acceptance rate
        total = len(submissions)
        accepted = sum(1 for s in submissions if s.status == "Accepted")
        acceptance_rate = (accepted / total * 100) if total > 0 else 0.0

        return {
            "title": problem.title,
            "titleSlug": problem.titleSlug,
            "difficulty": problem.difficulty,
            "tags": problem.topicTags,
            "relatedProblems": problem.relatedProblems or [],
            "content": problem.content,
            "acceptanceRate": round(acceptance_rate, 2),
            "totalSubmissions": total,
            "solved": accepted > 0,
            "submissions": [
                {
                    "id": s.id,
                    "status": s.status,
                    "createdAt": s.createdAt.isoformat(),
                    "timeSpentMinutes": s.timeSpentMinutes,
                    "isCheat": s.isCheat,
                    "content": s.content if s.status == "Accepted" else None,
                }
                for s in submissions
            ],
        }

    except Exception as e:
        print(f"✗ Error getting problem details: {e}", file=sys.stderr)
        return None

    finally:
        await db.disconnect()


async def get_all_tags() -> List[str]:
    """
    Get all unique topic tags from all problems.

    Returns:
        Sorted list of unique tags
    """
    db = Prisma()

    try:
        await db.connect()

        # Get all problems
        problems = await db.question.find_many()

        # Collect all unique tags
        all_tags = set()
        for problem in problems:
            all_tags.update(problem.topicTags)

        return sorted(list(all_tags))

    except Exception as e:
        print(f"✗ Error getting tags: {e}", file=sys.stderr)
        return []

    finally:
        await db.disconnect()


async def get_overall_stats() -> Dict[str, Any]:
    """
    Get overall statistics about all problems and submissions.

    Returns:
        Dictionary with overall stats
    """
    db = Prisma()

    try:
        await db.connect()

        # Count total problems
        total_problems = await db.question.count()

        # Get all submissions
        all_submissions = await db.submission.find_many()

        # Count solved problems
        solved_slugs = set(
            s.titleSlug
            for s in all_submissions
            if s.status == "Accepted" and s.titleSlug
        )
        solved_count = len(solved_slugs)

        # Calculate overall acceptance rate
        total_submissions = len(all_submissions)
        accepted_submissions = sum(1 for s in all_submissions if s.status == "Accepted")
        acceptance_rate = (
            (accepted_submissions / total_submissions * 100)
            if total_submissions > 0
            else 0.0
        )

        return {
            "totalProblems": total_problems,
            "solvedCount": solved_count,
            "totalSubmissions": total_submissions,
            "acceptanceRate": round(acceptance_rate, 2),
        }

    except Exception as e:
        print(f"✗ Error getting overall stats: {e}", file=sys.stderr)
        return {
            "totalProblems": 0,
            "solvedCount": 0,
            "totalSubmissions": 0,
            "acceptanceRate": 0.0,
        }

    finally:
        await db.disconnect()
