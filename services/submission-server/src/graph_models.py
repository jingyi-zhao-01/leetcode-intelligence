"""Pydantic models for API responses with camelCase field names."""

from typing import List, Optional
from pydantic import BaseModel, Field


class NodeResponse(BaseModel):
    """Graph node representing a LeetCode problem."""

    id: int
    title: str
    title_slug: str = Field(..., alias="titleSlug")
    difficulty: str
    tags: List[str]
    acceptance_rate: float = Field(..., alias="acceptanceRate")
    total_submissions: int = Field(..., alias="totalSubmissions")
    solved: bool
    freq_bar: float = Field(..., alias="freqBar")

    class Config:
        populate_by_name = True


class EdgeResponse(BaseModel):
    """Graph edge representing relationship between problems."""

    source: int
    target: int
    type: str  # "explicit" or "tag_similarity"
    shared_tags: Optional[int] = Field(None, alias="sharedTags")

    class Config:
        populate_by_name = True


class GraphStatsResponse(BaseModel):
    """Statistics about the graph."""

    total_problems: int = Field(..., alias="totalProblems")
    total_edges: int = Field(..., alias="totalEdges")
    explicit_edges: int = Field(..., alias="explicitEdges")
    tag_edges: int = Field(..., alias="tagEdges")
    solved_problems: int = Field(..., alias="solvedProblems")
    unsolved_problems: int = Field(..., alias="unsolvedProblems")

    class Config:
        populate_by_name = True


class GraphResponse(BaseModel):
    """Complete graph data response."""

    nodes: List[NodeResponse]
    edges: List[EdgeResponse]
    stats: GraphStatsResponse


class SubmissionHistoryResponse(BaseModel):
    """Individual submission record."""

    id: str
    status: str
    created_at: str = Field(..., alias="createdAt")
    time_spent_minutes: Optional[int] = Field(None, alias="timeSpentMinutes")
    is_cheat: bool = Field(..., alias="isCheat")

    class Config:
        populate_by_name = True


class ProblemDetailResponse(BaseModel):
    """Detailed problem information."""

    title: str
    title_slug: str = Field(..., alias="titleSlug")
    difficulty: str
    tags: List[str]
    related_problems: List[str] = Field(..., alias="relatedProblems")
    content: Optional[str] = None
    acceptance_rate: float = Field(..., alias="acceptanceRate")
    total_submissions: int = Field(..., alias="totalSubmissions")
    solved: bool
    submissions: List[SubmissionHistoryResponse]

    class Config:
        populate_by_name = True


class StatsResponse(BaseModel):
    """Overall statistics."""

    total_problems: int = Field(..., alias="totalProblems")
    solved_count: int = Field(..., alias="solvedCount")
    total_submissions: int = Field(..., alias="totalSubmissions")
    acceptance_rate: float = Field(..., alias="acceptanceRate")

    class Config:
        populate_by_name = True
