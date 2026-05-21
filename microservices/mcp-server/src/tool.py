"""
LeetCode Submission Evolution Tools
Provides functionality for analyzing submission evolution and thought progression.
"""

import asyncio
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Tuple

from prisma import Prisma
from util import (
    extract_comments,
    analyze_comment_themes,
    count_complexity_mentions,
    analyze_overall_progression,
)


# === PROBLEM DISCOVERY HELPERS ===

_DIFFICULTY_VALUES = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}


def _normalize_slug(value: str) -> str:
    slug = (value or "").strip()
    if not slug:
        raise ValueError("'slug' is required and cannot be empty.")
    return slug


def _normalize_query(value: str) -> str:
    query = (value or "").strip()
    if not query:
        raise ValueError("'query' is required and cannot be empty.")
    return query


def _normalize_difficulty(value: Optional[str]) -> Optional[str]:
    if value is None: