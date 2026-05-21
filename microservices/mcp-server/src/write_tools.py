from typing import Any, Awaitable, Callable, Optional, TypeAlias, TypedDict, cast

from fastmcp import FastMCP
from prisma import Prisma


class ErrorResponse(TypedDict):
    error: str


class SubmissionWriteItem(TypedDict):
    id: str
    title_slug: str | None
    status: str
    thought: str | None
    mistake: str | None
    is_cheat: bool
    time_spent_minutes: int | None
    created_at: str


class CreateSubmissionSuccess(TypedDict):
    submission: SubmissionWriteItem


class UpdateSubmissionSuccess(TypedDict):
    submission: SubmissionWriteItem


class DeleteSubmissionSuccess(TypedDict):
    deleted_id: str


CreateSubmissionResponse: TypeAlias = CreateSubmissionSuccess | ErrorResponse
UpdateSubmissionResponse: TypeAlias = UpdateSubmissionSuccess | ErrorResponse
DeleteSubmissionResponse: TypeAlias = DeleteSubmissionSuccess | ErrorResponse


class FollowUpItem(TypedDict):
    id: str
