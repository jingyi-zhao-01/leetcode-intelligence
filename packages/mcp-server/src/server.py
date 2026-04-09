#!/usr/bin/env python3
"""
LeetCode Submission History MCP Server
Provides two main tools for analyzing LeetCode submissions:
- get_submission_history: List all submissions for a specific problem
- analyze_thought_progression: Comment and approach evolution analysis
"""

import asyncio
import sys
import os
import subprocess
from prisma import Prisma

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
from read_tools import register_read_tools
from write_tools import register_write_tools

# Create FastMCP server with submission evolution tools
mcp = FastMCP(name="LeetCode Submission Evolution Server 🚀")

# Global Prisma instance for submission tools
db = Prisma()


async def ensure_db_connected():
    """Ensure database connection is established."""
    if not db.is_connected():
        await db.connect()


# Register CRUD-style Read tools from a dedicated module.
register_read_tools(mcp, db, ensure_db_connected)

# Register CRUD-style Write tools from a dedicated module.
register_write_tools(mcp, db, ensure_db_connected)


# === SERVER STARTUP ===


async def startup():
    """Initialize database connection."""
    await db.connect()
    print("✅ Database connected")


async def shutdown():
    """Clean up database connection."""
    await db.disconnect()
    print("✅ Database disconnected")


def main():
    """Main entry point for the MCP HTTP server."""

    try:
        # The FastMCP framework will handle the event loop
        mcp.run(transport="http", port=8000)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")

    # Clean shutdown
    try:
        asyncio.run(shutdown())
    except Exception:
        pass


def main_dev():
    """Main entry point for development with hot reload.

    Watches source files and automatically restarts the server on changes.
    """
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        import time

        class ServerReloader(FileSystemEventHandler):
            def __init__(self):
                self.process = None
                self.start_server()

            def start_server(self):
                """Start the MCP server process."""
                if self.process:
                    print("🔄 Restarting server...")
                    self.process.terminate()
                    try:
                        self.process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        self.process.kill()
                else:
                    print("🚀 Starting MCP server with hot reload...")

                # Start stdio server since that's what we use for Copilot
                self.process = subprocess.Popen(
                    [sys.executable, "-m", "server", "main_stdio"],
                    cwd=os.path.dirname(os.path.abspath(__file__)),
                )

            def on_modified(self, event):
                """Handle file modifications."""
                if event.is_directory or event.src_path.endswith(".pyc"):
                    return
                if event.src_path.endswith(".py"):
                    print(f"📝 Detected change in {os.path.basename(event.src_path)}")
                    self.start_server()

        # Watch the src directory for changes
        observer = Observer()
        handler = ServerReloader()
        src_dir = os.path.dirname(os.path.abspath(__file__))
        observer.schedule(handler, src_dir, recursive=True)
        observer.start()

        try:
            # Keep the observer running
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Shutting down dev server...")
            observer.stop()
            if handler.process:
                handler.process.terminate()

        observer.join()

    except ImportError:
        print("❌ watchdog not installed. Install dev dependencies with: uv sync --dev")
        sys.exit(1)


def main_stdio():
    """Main entry point for the MCP stdio server (for GitHub Copilot)."""
    try:
        # Run the MCP server using stdio transport for Copilot
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
