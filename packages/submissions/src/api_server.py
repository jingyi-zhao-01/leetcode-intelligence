"""Unified FastAPI server for submissions and graph visualization."""

from contextlib import asynccontextmanager
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from prisma import Prisma, Json
from prisma.types import SubmissionCreateInput

from graph_models import GraphResponse, ProblemDetailResponse, StatsResponse
from graph_service import (
    build_graph_data,
    get_problem_details,
    get_all_tags,
    get_overall_stats,
)
from timer_service import TimerManager
from code_cleaner import normalize_for_embedding

# Global Prisma client and timer manager
db = Prisma()
timer_manager = TimerManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan (startup/shutdown)."""
    # Startup
    await db.connect()
    print("🚀 API server started", flush=True)
    yield
    # Shutdown
    await db.disconnect()
    print("👋 API server stopped", flush=True)


app = FastAPI(
    title="LeetCode Submissions API",
    description="API for LeetCode submissions tracking and graph visualization",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Root Endpoint
# ============================================================================


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "LeetCode Submissions API",
        "docs": "/docs",
        "version": "0.1.0",
    }


# ============================================================================
# Graph Visualization Endpoints
# ============================================================================


@app.get("/api/graph", response_model=GraphResponse)
async def get_graph(
    solved: bool = False,
    include_tags: Optional[str] = None,
    filter_tags: Optional[str] = None,
    difficulties: Optional[str] = None,
    limit: int = 3000,
):
    """Get problem graph with filters.

    Args:
        solved: Only include solved problems
        include_tags: Comma-separated tags (OR logic - any match)
        filter_tags: Comma-separated tags (AND logic - all required)
        difficulties: Comma-separated difficulties (Easy, Medium, Hard)
        limit: Maximum number of problems
    """
    # Parse comma-separated tags
    include_tags_list = (
        [t.strip() for t in include_tags.split(",") if t.strip()]
        if include_tags
        else None
    )
    filter_tags_list = (
        [t.strip() for t in filter_tags.split(",") if t.strip()]
        if filter_tags
        else None
    )
    difficulties_list = (
        [d.strip() for d in difficulties.split(",") if d.strip()]
        if difficulties
        else None
    )

    graph_data = await build_graph_data(
        solved=solved,
        include_tags=include_tags_list,
        filter_tags=filter_tags_list,
        difficulties=difficulties_list,
        limit=limit,
    )

    return graph_data


@app.get("/api/problems/{title_slug}", response_model=ProblemDetailResponse)
async def get_problem(title_slug: str):
    """Get detailed information about a specific problem."""
    problem_data = await get_problem_details(title_slug)

    if not problem_data:
        raise HTTPException(status_code=404, detail="Problem not found")

    return problem_data


@app.get("/api/tags", response_model=List[str])
async def get_tags():
    """Get all available topic tags."""
    return await get_all_tags()


@app.get("/api/stats", response_model=StatsResponse)
async def get_stats():
    """Get overall statistics."""
    return await get_overall_stats()


# ============================================================================
# Timer Management Endpoints
# ============================================================================


@app.post("/api/timers/start")
async def start_timer(
    title_slug: str = Body(..., embed=True),
    allow_multiple: bool = Body(False, embed=True),
):
    """Start a timer for a problem."""
    timer_manager.start(title_slug, allow_multiple=allow_multiple)
    return {
        "success": True,
        "action": "start_timer",
        "titleSlug": title_slug,
    }


@app.post("/api/timers/stop")
async def stop_timer(title_slug: str = Body(..., embed=True)):
    """Stop a timer for a problem and save session."""
    minutes = timer_manager.stop(title_slug)

    # Save session to database
    if minutes > 0:
        await db.problemsession.create(
            data={
                "titleSlug": title_slug,
                "timeSpentMinutes": minutes,
                "isActive": False,
            }
        )

    return {
        "success": True,
        "action": "stop_timer",
        "titleSlug": title_slug,
        "minutes": minutes,
    }


@app.get("/api/timers/active")
async def get_active_timers():
    """Get all active timers."""
    timers = timer_manager.get_active_timers()
    return {
        "success": True,
        "action": "get_active_timers",
        "timers": timers,
    }


@app.get("/api/sessions/active")
async def get_active_sessions():
    """Get all active sessions."""
    timers = timer_manager.get_active_timers()
    sessions = []
    for title_slug, elapsed_minutes in timers.items():
        sessions.append(
            {
                "titleSlug": title_slug,
                "elapsedMinutes": elapsed_minutes,
                "status": "active",
            }
        )
    return {
        "success": True,
        "action": "get_active_sessions",
        "sessions": sessions,
        "count": len(sessions),
    }


# ============================================================================
# Submission Endpoints
# ============================================================================


@app.post("/api/submissions")
async def save_submission(
    title_slug: str = Body(...),
    content: str = Body(...),
    item: dict = Body(...),
):
    """Save a submission to the database.

    Args:
        title_slug: The LeetCode problem slug (e.g., "two-sum")
        content: The submission code content
        item: Full submission details including status

    Returns:
        Success status and submission ID if successful
    """
    status = item.get("status_msg", "Unknown")

    # Skip if content contains #TEST#
    if "#TEST#" in content:
        return {
            "success": False,
            "message": "Skipped test submission",
            "titleSlug": title_slug,
        }

    # Check if content contains #CHEAT# flag
    is_cheat = "#CHEAT#" in content

    time_spent_minutes = None
    if timer_manager.has_active_timer(title_slug):
        time_spent_minutes = timer_manager.get_elapsed_time(title_slug)

    try:
        # Clean and normalize the code for better embeddings
        cleaned_content = normalize_for_embedding(content)

        # Build submission data
        submission_data: SubmissionCreateInput = {
            "titleSlug": title_slug,
            "content": cleaned_content,
            "status": status,
            "isCheat": is_cheat,
            "timeSpentMinutes": time_spent_minutes,
            "submissionDetails": Json(item) if item else None,
        }

        submission = await db.submission.create(data=submission_data)

        if status == "Accepted":
            if timer_manager.has_active_timer(title_slug):
                timer_manager.stop(title_slug)
            timer_manager.start(title_slug)

        return {
            "success": True,
            "submissionId": submission.id,
            "titleSlug": title_slug,
            "status": status,
            "isCheat": is_cheat,
            "timeSpentMinutes": time_spent_minutes,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving submission: {e}")


# ============================================================================
# CLI Entry Point
# ============================================================================


def run():
    """CLI entry point for running the server."""
    import uvicorn

    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run()
