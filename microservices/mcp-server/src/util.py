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