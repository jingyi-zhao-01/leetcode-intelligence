"""FastAPI server for data analytics on LeetCode submissions."""

from contextlib import asynccontextmanager
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prisma import Prisma

from graph_models import GraphResponse, ProblemDetailResponse, StatsResponse
from graph_service import (
    build_graph_data,
    get_problem_details,
    get_all_tags,
    get_overall_stats,
)

# Global Prisma client
db = Prisma()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan (startup/shutdown)."""
    # Startup
    await db.connect()
    print("🚀 Analytics API server started on port 8000", flush=True)
    yield
    # Shutdown
    await db.disconnect()
    print("👋 Analytics API server stopped", flush=True)


app = FastAPI(
    title="LeetCode Analytics API",
    description="Read-only API for LeetCode submissions data analytics and graph visualization",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],  # Frontend and other clients
    allow_credentials=True,
    allow_methods=["GET"],  # Read-only
    allow_headers=["*"],
)


# ============================================================================
# Root Endpoint
# ============================================================================


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "LeetCode Analytics API",
        "docs": "/docs",
        "version": "0.1.0",
        "purpose": "Read-only data analytics and visualization",
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
# CLI Entry Point
# ============================================================================


def run():
    """CLI entry point for running the analytics server."""
    import uvicorn

    uvicorn.run(
        "analytics_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run()
