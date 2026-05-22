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


class SaveMistakesSuccess(TypedDict):
    submission_id: str
    mistakes: str


class SaveMistakesNotFound(TypedDict):
    submission_id: str
    message: str


SaveMistakesResponse: TypeAlias = (
    SaveMistakesSuccess | SaveMistakesNotFound | ErrorResponse
)


def _validate_required_text(field_name: str, value: str) -> Optional[ErrorResponse]:
    if not value.strip():
        return {"error": f"'{field_name}' is required and cannot be empty."}
    return None


def _build_update_payload(
    title_slug: Optional[str],
    content: Optional[str],
    status: Optional[str],
    thought: Optional[str],
    mistake: Optional[str],
    submission_details: Optional[dict[str, Any]],
    is_cheat: Optional[bool],
    time_spent_minutes: Optional[int],
) -> tuple[dict[str, Any], Optional[str]]:
    data: dict[str, Any] = {}

    if title_slug is not None:
        data["titleSlug"] = title_slug

    if content is not None:
        if not content.strip():
            return {}, "'content' cannot be empty when provided."
        data["content"] = content

    if status is not None:
        if not status.strip():
            return {}, "'status' cannot be empty when provided."
        data["status"] = status

    if thought is not None:
        data["thought"] = thought
    if mistake is not None:
        data["mistake"] = mistake
    if submission_details is not None:
        data["submissionDetails"] = submission_details
    if is_cheat is not None:
        data["isCheat"] = is_cheat
    if time_spent_minutes is not None:
        data["timeSpentMinutes"] = time_spent_minutes

    return data, None


def _serialize_submission(submission: Any) -> SubmissionWriteItem:
    return {
        "id": submission.id,
        "title_slug": submission.titleSlug,
        "status": submission.status,
        "thought": submission.thought,
        "mistake": submission.mistake,
        "is_cheat": submission.isCheat,
        "time_spent_minutes": submission.timeSpentMinutes,
        "created_at": submission.createdAt.isoformat(),
    }


async def _handle_create_submission(
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
    content: str,
    status: str,
    title_slug: Optional[str],
    thought: Optional[str],
    mistake: Optional[str],
    submission_details: Optional[dict[str, Any]],
    is_cheat: bool,
    time_spent_minutes: Optional[int],
) -> CreateSubmissionResponse:
    await ensure_db_connected()

    content_err = _validate_required_text("content", content)
    if content_err:
        return content_err

    status_err = _validate_required_text("status", status)
    if status_err:
        return status_err

    try:
        create_data = cast(
            Any,
            {
                "titleSlug": title_slug,
                "content": content,
                "status": status,
                "thought": thought,
                "mistake": mistake,
                "submissionDetails": submission_details,
                "isCheat": is_cheat,
                "timeSpentMinutes": time_spent_minutes,
            },
        )
        created = await db.submission.create(data=create_data)
        return {"submission": _serialize_submission(created)}
    except Exception as exc:
        return {"error": f"Failed to create submission: {exc}"}


async def _handle_update_submission(
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
    submission_id: str,
    title_slug: Optional[str],
    content: Optional[str],
    status: Optional[str],
    thought: Optional[str],
    mistake: Optional[str],
    submission_details: Optional[dict[str, Any]],
    is_cheat: Optional[bool],
    time_spent_minutes: Optional[int],
) -> UpdateSubmissionResponse:
    await ensure_db_connected()

    submission_id_err = _validate_required_text("submission_id", submission_id)
    if submission_id_err:
        return submission_id_err

    data, data_error = _build_update_payload(
        title_slug=title_slug,
        content=content,
        status=status,
        thought=thought,
        mistake=mistake,
        submission_details=submission_details,
        is_cheat=is_cheat,
        time_spent_minutes=time_spent_minutes,
    )
    if data_error:
        return {"error": data_error}

    if not data:
        return {"error": "No fields provided to update."}

    try:
        updated = await db.submission.update(
            where={"id": submission_id},
            data=cast(Any, data),
        )
        return {"submission": _serialize_submission(updated)}
    except Exception as exc:
        return {"error": f"Failed to update submission '{submission_id}': {exc}"}


async def _handle_delete_submission(
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
    submission_id: str,
) -> DeleteSubmissionResponse:
    await ensure_db_connected()

    submission_id_err = _validate_required_text("submission_id", submission_id)
    if submission_id_err:
        return submission_id_err

    try:
        deleted = await db.submission.delete(where={"id": submission_id})
        if deleted is None:
            return {"error": f"Submission '{submission_id}' was not found."}
        return {"deleted_id": deleted.id}
    except Exception as exc:
        return {"error": f"Failed to delete submission '{submission_id}': {exc}"}


async def _handle_save_mistakes(
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
    submission_id: str,
    mistakes: list[str],
) -> SaveMistakesResponse:
    await ensure_db_connected()

    id_err = _validate_required_text("submission_id", submission_id)
    if id_err:
        return id_err

    if not mistakes:
        return {"error": "'mistakes' list cannot be empty."}

    bullet_text = "\n".join(f"- {item.strip()}" for item in mistakes if item.strip())
    if not bullet_text:
        return {"error": "All provided mistake items were blank."}

    try:
        existing = await db.submission.find_unique(where={"id": submission_id})
        if existing is None:
            return {
                "submission_id": submission_id,
                "message": "Submission not found",
            }

        await db.submission.update(
            where={"id": submission_id},
            data=cast(Any, {"mistake": bullet_text}),
        )
        return {"submission_id": submission_id, "mistakes": bullet_text}
    except Exception as exc:
        return {"error": f"Failed to save mistakes for '{submission_id}': {exc}"}


def register_write_tools(
    mcp: FastMCP,
    db: Prisma,
    ensure_db_connected: Callable[[], Awaitable[None]],
) -> None:
    """Register write/mutation MCP tools (CRUD: Create/Update/Delete)."""

    @mcp.tool
    async def create_submission(
        content: str,
        status: str,
        title_slug: Optional[str] = None,
        thought: Optional[str] = None,
        mistake: Optional[str] = None,
        submission_details: Optional[dict[str, Any]] = None,
        is_cheat: bool = False,
        time_spent_minutes: Optional[int] = None,
    ) -> CreateSubmissionResponse:
        """Create a new submission row in the database."""
        return await _handle_create_submission(
            db=db,
            ensure_db_connected=ensure_db_connected,
            content=content,
            status=status,
            title_slug=title_slug,
            thought=thought,
            mistake=mistake,
            submission_details=submission_details,
            is_cheat=is_cheat,
            time_spent_minutes=time_spent_minutes,
        )

    @mcp.tool
    async def update_submission(
        submission_id: str,
        title_slug: Optional[str] = None,
        content: Optional[str] = None,
        status: Optional[str] = None,
        thought: Optional[str] = None,
        mistake: Optional[str] = None,
        submission_details: Optional[dict[str, Any]] = None,
        is_cheat: Optional[bool] = None,
        time_spent_minutes: Optional[int] = None,
    ) -> UpdateSubmissionResponse:
        """Update an existing submission by ID."""
        return await _handle_update_submission(
            db=db,
            ensure_db_connected=ensure_db_connected,
            submission_id=submission_id,
            title_slug=title_slug,
            content=content,
            status=status,
            thought=thought,
            mistake=mistake,
            submission_details=submission_details,
            is_cheat=is_cheat,
            time_spent_minutes=time_spent_minutes,
        )

    @mcp.tool
    async def delete_submission(submission_id: str) -> DeleteSubmissionResponse:
        """Delete an existing submission by ID."""
        return await _handle_delete_submission(
            db=db,
            ensure_db_connected=ensure_db_connected,
            submission_id=submission_id,
        )

    @mcp.tool
    async def save_submission_mistakes(
        submission_id: str,
        mistakes: list[str],
    ) -> SaveMistakesResponse:
        """Save a bullet-list of mistakes for a submission, replacing any existing value.

        Each item in `mistakes` becomes one bullet point (e.g. `- forgot edge case`).
        """
        return await _handle_save_mistakes(
            db=db,
            ensure_db_connected=ensure_db_connected,
            submission_id=submission_id,
            mistakes=mistakes,
        )
