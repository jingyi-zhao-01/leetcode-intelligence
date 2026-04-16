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
        required = value.get("hasEvery", [])
        return all(t in tags for t in required)

    @staticmethod
    def _match_slug(q, value):
        if isinstance(value, dict) and "in" in value:
            return q.titleSlug in value["in"]
        return q.titleSlug == value

    def _match_field(self, q, key, value):
        if key == "title":
            return self._match_title(q, value)
        if key == "difficulty":
            return q.difficulty == value
        if key == "topicTags":
            return self._match_topics(q, value)
        if key == "titleSlug":
            return self._match_slug(q, value)
        return True

    def _match(self, q, where):
        if not where:
            return True

        for key, value in where.items():
            if not self._match_field(q, key, value):
                return False

        return True

    def _apply_order(self, rows, order):
        if not order:
            return rows

        ordered = list(rows)
        # Apply stable sorts in reverse order for multi-key ordering
        for spec in reversed(order):
            field, direction = next(iter(spec.items()))
            reverse = direction == "desc"
            ordered.sort(key=lambda x, f=field: getattr(x, f), reverse=reverse)
        return ordered

    async def find_unique(self, where):
        await asyncio.sleep(0)
        slug = where.get("titleSlug")
        for q in self._questions:
            if q.titleSlug == slug:
                return q
        return None

    async def find_many(self, where=None, order=None, skip=0, take=50):
        await asyncio.sleep(0)
        rows = [q for q in self._questions if self._match(q, where or {})]
        rows = self._apply_order(rows, order or [])
        return rows[skip : skip + take]

    async def count(self, where=None):
        await asyncio.sleep(0)
        return len([q for q in self._questions if self._match(q, where or {})])


class StubSubmissionManager:
    def __init__(self, submissions):
        self._submissions = submissions

    def _match(self, s, where):
        if not where:
            return True
        for key, value in where.items():
            if getattr(s, key) != value:
                return False
        return True

    async def count(self, where=None):
        await asyncio.sleep(0)
        return len([s for s in self._submissions if self._match(s, where or {})])


class StubDB:
    def __init__(self, questions, submissions):
        self.question = StubQuestionManager(questions)
        self.submission = StubSubmissionManager(submissions)


QUESTIONS = [
    SimpleNamespace(
        title="Two Sum",
        titleSlug="two-sum",
        difficulty="Easy",
        topicTags=["Array", "Hash Table"],
        relatedProblems=["3sum", "valid-anagram", "missing-problem"],
        content="Given an array of integers ...",
        freqBar=98.0,
    ),
    SimpleNamespace(
        title="3Sum",
        titleSlug="3sum",
        difficulty="Medium",
        topicTags=["Array", "Two Pointers"],
        relatedProblems=["two-sum"],
        content="Given an integer array nums ...",
        freqBar=90.0,
    ),
    SimpleNamespace(
        title="Valid Anagram",
        titleSlug="valid-anagram",
        difficulty="Easy",
        topicTags=["Hash Table", "String"],
        relatedProblems=["two-sum"],
        content="Given two strings ...",
        freqBar=85.0,
    ),
]

SUBMISSIONS = [
    SimpleNamespace(titleSlug="two-sum", status="Accepted"),
    SimpleNamespace(titleSlug="two-sum", status="Wrong Answer"),
    SimpleNamespace(titleSlug="3sum", status="Time Limit Exceeded"),
]


def _db():
    return StubDB(QUESTIONS, SUBMISSIONS)


def test_search_problems_with_filters():
    result = asyncio.run(
        search_problems(cast(Any, _db()), query="sum", topic="Array", difficulty="easy")
    )

    assert "error" not in result
    assert result["total"] == 1
    assert result["items"][0]["slug"] == "two-sum"


def test_get_problem_details_with_submission_summary():
    result = asyncio.run(get_problem_details(cast(Any, _db()), slug="two-sum"))

    assert "error" not in result
    assert result["slug"] == "two-sum"
    assert result["submission_summary"]["attempts"] == 2
    assert result["submission_summary"]["accepted_submissions"] == 1
    assert result["submission_summary"]["is_solved"] is True


def test_get_related_problems_includes_missing():
    result = asyncio.run(
        get_related_problems(cast(Any, _db()), slug="two-sum", include_details=False)
    )

    assert "error" not in result
    assert result["related_problems"] == ["3sum", "valid-anagram"]
    assert result["missing_slugs"] == ["missing-problem"]


def test_list_problems_by_filters_and_sort():
    result = asyncio.run(
        list_problems_by_filters(
            cast(Any, _db()), topics=["Hash Table"], difficulty="Easy", sort_by="-title"
        )
    )

    assert "error" not in result
    assert result["total"] == 2
    # -title means reverse lexical: Valid Anagram then Two Sum
    assert [p["slug"] for p in result["items"]] == ["valid-anagram", "two-sum"]


def test_list_popular_problems_descending():
    result = asyncio.run(list_popular_problems(cast(Any, _db()), topic="Array"))

    assert "error" not in result
    assert [p["slug"] for p in result["items"]] == ["two-sum", "3sum"]


def test_check_problem_solved_true_false():
    solved = asyncio.run(check_problem_solved(cast(Any, _db()), slug="two-sum"))
    unsolved = asyncio.run(check_problem_solved(cast(Any, _db()), slug="valid-anagram"))

    assert solved["is_solved"] is True
    assert unsolved["is_solved"] is False


def test_invalid_difficulty_returns_error():
    result = asyncio.run(
        search_problems(cast(Any, _db()), query="sum", difficulty="Legendary")
    )
    assert "error" in result
    assert "Invalid difficulty" in result["error"]
