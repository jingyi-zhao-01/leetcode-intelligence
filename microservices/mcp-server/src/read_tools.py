from typing import Any, Awaitable, Callable, Optional, TypeAlias, TypedDict, cast

from fastmcp import FastMCP
from prisma import Prisma

from tool import (
    analyze_thought_progression as analyze_thought_progression_impl,
    check_problem_solved as check_problem_solved_impl,
    get_problem_details as get_problem_details_impl,
    get_related_problems as get_related_problems_impl,
    get_submission_detail as get_submission_detail_impl,
    get_submission_history as get_submission_history_impl,
    list_popular_problems as list_popular_problems_impl,
    list_problems_by_filters as list_problems_by_filters_impl,
    review_submissions as review_submissions_impl,
    search_problems as search_problems_impl,
)


class ErrorResponse(TypedDict):
    error: str


class TitleSlugErrorResponse(TypedDict):
    error: str
    title_slug: str


class ISODateRange(TypedDict):
    start: str
    end: str


class ProblemSummaryItem(TypedDict):
    title: str
    slug: str
    difficulty: str
    topics: list[str]
    popularity: float | int | None
