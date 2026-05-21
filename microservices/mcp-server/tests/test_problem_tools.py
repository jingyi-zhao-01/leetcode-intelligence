import asyncio
import os
import sys
from types import SimpleNamespace
from typing import Any, cast

# Ensure src/ is importable when running tests directly
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

from tool import (  # noqa: E402
    search_problems,
    get_problem_details,
    get_related_problems,
    list_problems_by_filters,
    list_popular_problems,
    check_problem_solved,
)


class StubQuestionManager:
    def __init__(self, questions):
        self._questions = questions

    @staticmethod
    def _match_title(q, value):
        needle = value.get("contains", "")
        mode = value.get("mode")
        haystack = q.title
        if mode == "insensitive":
            return needle.lower() in haystack.lower()
        return needle in haystack

    @staticmethod
    def _match_topics(q, value):
        tags = set(q.topicTags or [])
        has_tag = value.get("has")
        if has_tag and has_tag not in tags:
            return False
