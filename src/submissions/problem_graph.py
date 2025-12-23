import argparse
import asyncio
import sys
from pathlib import Path
from typing import List, Dict, Set, Any
from collections import defaultdict

from prisma import Prisma

# Add the project root to the path to import src modules
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


async def build_problem_graph(
    filter_solved: bool = False,
    filter_tags: List[str] = None,
    max_problems: int = 50,
) -> Dict[str, Any]:
    """
    Build a graph of problem connections based on tags and explicit relationships.

    Args:
        filter_solved: If True, only include solved problems
        filter_tags: If provided, only include problems with these tags
        max_problems: Maximum number of problems to include

    Returns:
        Dictionary containing nodes and edges for the graph
    """
    db = Prisma()

    try:
        await db.connect()

        # Get problems based on filters
        where_clause = {}
        problem_slugs = None

        if filter_solved:
            # Get solved problem slugs
            submissions = await db.submission.find_many(
                where={"status": "Accepted"},
                distinct=["titleSlug"],
            )
            problem_slugs = [s.titleSlug for s in submissions if s.titleSlug]
            if problem_slugs:
                where_clause["titleSlug"] = {"in": problem_slugs}
            else:
                return {"nodes": [], "edges": [], "stats": {"total_problems": 0}}

        # Get problems
        problems = await db.question.find_many(
            where=where_clause,
            take=max_problems,
        )

        if not problems:
            return {"nodes": [], "edges": [], "stats": {"total_problems": 0}}

        # Filter by tags if specified
        if filter_tags:
            problems = [
                p for p in problems if any(tag in p.topicTags for tag in filter_tags)
            ]

        # Build nodes and edges
        nodes = []
        edges = []
        slug_to_idx = {}

        # Create nodes
        for idx, problem in enumerate(problems):
            slug_to_idx[problem.titleSlug] = idx

            # Check if solved
            submission = await db.submission.find_first(
                where={"titleSlug": problem.titleSlug, "status": "Accepted"}
            )

            nodes.append(
                {
                    "id": idx,
                    "titleSlug": problem.titleSlug,
                    "title": problem.title,
                    "difficulty": problem.difficulty,
                    "topicTags": problem.topicTags,
                    "freqBar": problem.freqBar or 0,
                    "solved": submission is not None,
                }
            )

        # Create edges based on explicit relationships
        edge_set = set()
        for problem in problems:
            if problem.relatedProblems:
                source_idx = slug_to_idx.get(problem.titleSlug)
                if source_idx is not None:
                    for related_slug in problem.relatedProblems:
                        target_idx = slug_to_idx.get(related_slug)
                        if target_idx is not None:
                            # Create undirected edge (add both directions but dedupe)
                            edge_pair = tuple(sorted([source_idx, target_idx]))
                            if edge_pair not in edge_set:
                                edge_set.add(edge_pair)
                                edges.append(
                                    {
                                        "source": source_idx,
                                        "target": target_idx,
                                        "type": "explicit",
                                    }
                                )

        # Create edges based on shared tags
        # Group problems by tags
        tag_to_problems = defaultdict(list)
        for idx, problem in enumerate(problems):
            for tag in problem.topicTags:
                tag_to_problems[tag].append(idx)

        # Connect problems that share multiple tags
        tag_edge_count = defaultdict(int)
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

                        # Only create edge if they share 2+ tags
                        if shared_count >= 2 and edge_pair not in edge_set:
                            edge_set.add(edge_pair)
                            edges.append(
                                {
                                    "source": idx1,
                                    "target": idx2,
                                    "type": "tag_similarity",
                                    "sharedTags": shared_count,
                                }
                            )

        stats = {
            "total_problems": len(nodes),
            "total_edges": len(edges),
            "explicit_edges": sum(1 for e in edges if e["type"] == "explicit"),
            "tag_edges": sum(1 for e in edges if e["type"] == "tag_similarity"),
            "solved_problems": sum(1 for n in nodes if n["solved"]),
            "unsolved_problems": sum(1 for n in nodes if not n["solved"]),
        }

        return {"nodes": nodes, "edges": edges, "stats": stats}

    except Exception as e:
        print(f"✗ Error building problem graph: {e}", file=sys.stderr)
        return {"nodes": [], "edges": [], "stats": {"error": str(e)}}

    finally:
        await db.disconnect()


def export_to_graphviz(graph_data: Dict[str, Any], output_file: str) -> bool:
    """Export graph to Graphviz DOT format."""
    try:
        with open(output_file, "w") as f:
            f.write("graph ProblemGraph {\n")
            f.write("  layout=neato;\n")
            f.write("  overlap=false;\n")
            f.write("  splines=true;\n")
            f.write("  node [shape=box, style=filled];\n\n")

            # Write nodes
            for node in graph_data["nodes"]:
                # Color by difficulty and solved status
                if node["solved"]:
                    if node["difficulty"] == "Easy":
                        color = "lightgreen"
                    elif node["difficulty"] == "Medium":
                        color = "lightyellow"
                    else:
                        color = "lightcoral"
                else:
                    color = "lightgray"

                # Size by frequency
                width = max(0.5, min(2.0, node["freqBar"] / 50))

                label = node["title"].replace('"', '\\"')
                f.write(
                    f'  {node["id"]} [label="{label}", fillcolor="{color}", width={width:.2f}];\n'
                )

            f.write("\n")

            # Write edges
            for edge in graph_data["edges"]:
                if edge["type"] == "explicit":
                    style = "solid"
                    color = "blue"
                    penwidth = "2.0"
                else:
                    style = "dashed"
                    color = "gray"
                    penwidth = "1.0"

                f.write(
                    f'  {edge["source"]} -- {edge["target"]} [style="{style}", color="{color}", penwidth={penwidth}];\n'
                )

            f.write("}\n")

        return True
    except Exception as e:
        print(f"✗ Error exporting to Graphviz: {e}", file=sys.stderr)
        return False


def export_to_json(graph_data: Dict[str, Any], output_file: str) -> bool:
    """Export graph to JSON format for use with web visualization libraries."""
    import json

    try:
        with open(output_file, "w") as f:
            json.dump(graph_data, f, indent=2, default=str)
        return True
    except Exception as e:
        print(f"✗ Error exporting to JSON: {e}", file=sys.stderr)
        return False


def print_graph_stats(graph_data: Dict[str, Any]) -> None:
    """Print graph statistics."""
    stats = graph_data["stats"]

    print("\n" + "=" * 60)
    print("PROBLEM GRAPH STATISTICS")
    print("=" * 60)
    print(f"Total Problems: {stats['total_problems']}")
    print(f"  Solved: {stats.get('solved_problems', 0)}")
    print(f"  Unsolved: {stats.get('unsolved_problems', 0)}")
    print(f"\nTotal Connections: {stats['total_edges']}")
    print(f"  Explicit (LeetCode): {stats.get('explicit_edges', 0)}")
    print(f"  Tag Similarity: {stats.get('tag_edges', 0)}")
    print("=" * 60 + "\n")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Visualize LeetCode problem connections as a graph",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate graph of solved problems
  python -m src.submissions.problem_graph --solved

  # Generate graph with specific tags
  python -m src.submissions.problem_graph --tags "Array" "Dynamic Programming"

  # Export to Graphviz DOT format
  python -m src.submissions.problem_graph --output graph.dot --format dot

  # Export to JSON for web visualization
  python -m src.submissions.problem_graph --output graph.json --format json

  # Limit number of problems
  python -m src.submissions.problem_graph --limit 30 --output graph.dot
        """,
    )

    parser.add_argument(
        "--solved",
        action="store_true",
        help="Only include solved problems",
    )
    parser.add_argument(
        "--tags",
        nargs="+",
        help="Filter problems by topic tags",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of problems to include (default: 50)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path",
    )
    parser.add_argument(
        "--format",
        choices=["dot", "json"],
        default="dot",
        help="Output format (default: dot)",
    )

    args = parser.parse_args()

    # Build the graph
    print("Building problem graph...")
    graph_data = asyncio.run(
        build_problem_graph(
            filter_solved=args.solved,
            filter_tags=args.tags,
            max_problems=args.limit,
        )
    )

    if not graph_data["nodes"]:
        print("No problems found matching the criteria.")
        sys.exit(1)

    # Print statistics
    print_graph_stats(graph_data)

    # Export if requested
    if args.output:
        print(f"Exporting to {args.output}...")
        if args.format == "dot":
            success = export_to_graphviz(graph_data, args.output)
            if success:
                print(f"✓ Graph exported to {args.output}")
                print(f"\nTo visualize, install Graphviz and run:")
                print(f"  neato -Tpng {args.output} -o graph.png")
                print(f"  neato -Tsvg {args.output} -o graph.svg")
        else:
            success = export_to_json(graph_data, args.output)
            if success:
                print(f"✓ Graph exported to {args.output}")
                print(
                    f"\nJSON format can be used with D3.js, Cytoscape.js, or other web viz libraries"
                )

        if not success:
            sys.exit(1)
    else:
        print("Use --output to export the graph to a file.")


if __name__ == "__main__":
    main()
