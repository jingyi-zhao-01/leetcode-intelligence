"""
Utility functions for LeetCode submission analysis.
Provides helper functions for comment extraction, theme analysis, and metrics calculation.
"""

from typing import List, Dict, Any


def extract_comments(code: str) -> List[str]:
    """Extract comments from code."""
    lines = code.split("\n")
    comments = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            comments.append(line[1:].strip())
    return comments


def analyze_comment_themes(comments: List[str]) -> Dict[str, int]:
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


def count_complexity_mentions(comments: List[str]) -> Dict[str, int]:
    """Count complexity-related mentions in comments."""
    complexity_counts = {"time_complexity": 0, "space_complexity": 0}

    for comment in comments:
        comment_lower = comment.lower()
        if "time" in comment_lower and (
            "complexity" in comment_lower or "o(" in comment_lower
        ):
            complexity_counts["time_complexity"] += 1
        if "space" in comment_lower and (
            "complexity" in comment_lower or "o(" in comment_lower
        ):
            complexity_counts["space_complexity"] += 1

    return complexity_counts


def calculate_evolution_metrics(submissions) -> Dict[str, Any]:
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


def analyze_overall_progression(comment_evolution) -> Dict[str, Any]:
    """Analyze overall thought progression."""
    if not comment_evolution:
        return {}

    first_themes = comment_evolution[0].get("comment_themes", {})
    last_themes = comment_evolution[-1].get("comment_themes", {})

    theme_progression = {}
    for theme in first_themes:
        theme_progression[theme] = last_themes.get(theme, 0) - first_themes.get(
            theme, 0
        )

    return {
        "theme_development": theme_progression,
        "comment_density_trend": [item["comments_count"] for item in comment_evolution],
        "complexity_awareness_growth": sum(
            item["complexity_mentions"]["time_complexity"]
            + item["complexity_mentions"]["space_complexity"]
            for item in comment_evolution
        ),
    }
