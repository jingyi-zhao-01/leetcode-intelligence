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


class SubmissionHistoryItem(TypedDict):
    submissionId: str
    submittedCode: str
    result: str
    mistakes: str | None
    time: str


class SubmissionHistorySuccess(TypedDict):
    title_slug: str
    total_submissions: int
    submissions: list[SubmissionHistoryItem]


class SubmissionHistoryEmpty(TypedDict):
    title_slug: str
    total_submissions: int
    message: str


GetSubmissionHistoryResponse: TypeAlias = (
    SubmissionHistorySuccess | SubmissionHistoryEmpty | TitleSlugErrorResponse
)


class ThoughtEvolutionItem(TypedDict):
    attempt_number: int
    timestamp: str
    status: str
    comments_count: int
    comments: list[str]
    comment_themes: dict[str, Any]
    complexity_mentions: dict[str, Any]
    thought: str | None


class ThoughtProgressionSuccess(TypedDict):
    title_slug: str
    total_submissions: int
    comment_evolution: list[ThoughtEvolutionItem]
    progression_analysis: dict[str, Any]


class ThoughtProgressionEmpty(TypedDict):
    title_slug: str
    message: str


AnalyzeThoughtProgressionResponse: TypeAlias = (
    ThoughtProgressionSuccess | ThoughtProgressionEmpty | TitleSlugErrorResponse
)


class ReviewSummaryStats(TypedDict):
    total_problems_attempted: int
    total_accepted: int
    acceptance_rate_pct: float
    total_submissions: int
    error_type_counts: dict[str, int]
    topics_covered: list[str]


class ReviewProblemItem(TypedDict):
    title_slug: str
    title: str
    difficulty: str
    topic_tags: list[str]
    attempts: int
    statuses: list[str]
    final_status: str
    total_time_spent_minutes: int
    first_attempt_at: str
    final_submission_code: str | None
    final_submission_thought: str | None


class ReviewSubmissionsSuccess(TypedDict):
    period: str
    date_range: ISODateRange
    summary_stats: ReviewSummaryStats
    problems: list[ReviewProblemItem]


class ReviewSubmissionsEmpty(TypedDict):
    period: str
    date_range: ISODateRange
    message: str
    problems: list[ReviewProblemItem]
    summary_stats: ReviewSummaryStats


class ReviewErrorResponse(TypedDict):
    error: str
    period: str


ReviewSubmissionsResponse: TypeAlias = (
    ReviewSubmissionsSuccess | ReviewSubmissionsEmpty | ReviewErrorResponse
)


class SearchProblemsSuccess(TypedDict):
    query: str
    filters: dict[str, str | None]
    items: list[ProblemSummaryItem]
    total: int
    limit: int
    offset: int


SearchProblemsResponse: TypeAlias = SearchProblemsSuccess | ErrorResponse


class SubmissionSummary(TypedDict):
    attempts: int
    accepted_submissions: int
    is_solved: bool


class ProblemDetailsSuccess(TypedDict):
    title: str
    slug: str
    difficulty: str
    description: str | None
    topics: list[str]
    related_problems: list[str]
    popularity: float | int | None
    submission_summary: SubmissionSummary


GetProblemDetailsResponse: TypeAlias = ProblemDetailsSuccess | ErrorResponse


class RelatedProblemsWithDetailsSuccess(TypedDict):
    slug: str
    related_problems: list[ProblemSummaryItem]
    missing_slugs: list[str]


class RelatedProblemsWithSlugsSuccess(TypedDict):
    slug: str
    related_problems: list[str]
    missing_slugs: list[str]


GetRelatedProblemsResponse: TypeAlias = (
    RelatedProblemsWithDetailsSuccess | RelatedProblemsWithSlugsSuccess | ErrorResponse
)


class ListProblemsByFiltersSuccess(TypedDict):
    filters: dict[str, Any]
    sort_by: str
    items: list[ProblemSummaryItem]
    total: int
    limit: int
    offset: int


ListProblemsByFiltersResponse: TypeAlias = ListProblemsByFiltersSuccess | ErrorResponse


class ListPopularProblemsSuccess(TypedDict):
    filters: dict[str, str | None]
    sort_by: str
    items: list[ProblemSummaryItem]
    total: int
    limit: int
    offset: int


ListPopularProblemsResponse: TypeAlias = ListPopularProblemsSuccess | ErrorResponse


class CheckProblemSolvedSuccess(TypedDict):
    slug: str
    is_solved: bool
    accepted_submissions: int


CheckProblemSolvedResponse: TypeAlias = CheckProblemSolvedSuccess | ErrorResponse


class SubmissionDetail(TypedDict):
    submissionId: str
    titleSlug: str | None
    submittedCode: str
    result: str
    thought: str | None
    mistakes: str | None
    time: str
    submissionDetails: Any
    isCheat: bool
    timeSpentMinutes: int | None


class SubmissionDetailNotFound(TypedDict):
    submissionId: str
    message: str


GetSubmissionDetailResponse: TypeAlias = (
    SubmissionDetail | SubmissionDetailNotFound | ErrorResponse
)


def register_read_tools(
    mcp: FastMCP,
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
) -> None:
    """Register read/query MCP tools (CRUD: Read)."""

    @mcp.tool
    async def get_submission_history(
        title_slug: str,
    ) -> GetSubmissionHistoryResponse:
        await ensure_db_connected()
        result = await get_submission_history_impl(db, title_slug)
        return cast(GetSubmissionHistoryResponse, result)

    @mcp.tool
    async def analyze_thought_progression(
        title_slug: str,
    ) -> AnalyzeThoughtProgressionResponse:
        await ensure_db_connected()
        result = await analyze_thought_progression_impl(db, title_slug)
        return cast(AnalyzeThoughtProgressionResponse, result)

    @mcp.tool
    async def review_submissions(
        period: str = "today",
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> ReviewSubmissionsResponse:
        await ensure_db_connected()
        result = await review_submissions_impl(db, period, start_date, end_date)
        return cast(ReviewSubmissionsResponse, result)

    @mcp.tool
    async def search_problems(
        query: str,
        topic: Optional[str] = None,
        difficulty: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> SearchProblemsResponse:
        await ensure_db_connected()
        result = await search_problems_impl(db, query, topic, difficulty, limit, offset)
        return cast(SearchProblemsResponse, result)

    @mcp.tool
    async def get_problem_details(slug: str) -> GetProblemDetailsResponse:
        await ensure_db_connected()
        result = await get_problem_details_impl(db, slug)
        return cast(GetProblemDetailsResponse, result)

    @mcp.tool
    async def get_related_problems(
        slug: str,
        include_details: bool = True,
    ) -> GetRelatedProblemsResponse:
        await ensure_db_connected()
        result = await get_related_problems_impl(db, slug, include_details)
        return cast(GetRelatedProblemsResponse, result)

    @mcp.tool
    async def list_problems_by_filters(
        topics: Optional[list[str]] = None,
        difficulty: Optional[str] = None,
        sort_by: str = "title",
        limit: int = 50,
        offset: int = 0,
    ) -> ListProblemsByFiltersResponse:
        await ensure_db_connected()
        result = await list_problems_by_filters_impl(
            db,
            topics,
            difficulty,
            sort_by,
            limit,
            offset,
        )
        return cast(ListProblemsByFiltersResponse, result)

    @mcp.tool
    async def list_popular_problems(
        topic: Optional[str] = None,
        difficulty: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> ListPopularProblemsResponse:
        await ensure_db_connected()
        result = await list_popular_problems_impl(db, topic, difficulty, limit, offset)
        return cast(ListPopularProblemsResponse, result)

    @mcp.tool
    async def check_problem_solved(slug: str) -> CheckProblemSolvedResponse:
        await ensure_db_connected()
        result = await check_problem_solved_impl(db, slug)
        return cast(CheckProblemSolvedResponse, result)

    @mcp.tool
    async def get_submission_detail(
        submission_id: str,
    ) -> GetSubmissionDetailResponse:
        await ensure_db_connected()
        result = await get_submission_detail_impl(db, submission_id)
        return cast(GetSubmissionDetailResponse, result)
