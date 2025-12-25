import asyncio
import json
import sys
from enum import Enum

from prisma import Prisma, Json
from prisma.types import SubmissionCreateInput

from code_cleaner import normalize_for_embedding
from timer_service import TimerManager


class ServerAction(str, Enum):
    """Enum for server action types."""

    START_TIMER = "start_timer"
    STOP_TIMER = "stop_timer"
    GET_ACTIVE_TIMERS = "get_active_timers"
    GET_ACTIVE_SESSIONS = "get_active_sessions"
    SAVE_SUBMISSION = "save_submission"


class SubmissionServer:
    """Server to handle timer and submission operations."""

    def __init__(self, host="127.0.0.1", port=3000):
        self.host = host
        self.port = port
        self.timer_manager = TimerManager()
        self.db = Prisma()

    async def log_active_sessions(self):
        """Periodically log active sessions every 5 seconds."""
        while True:
            await asyncio.sleep(5)
            timers = self.timer_manager.get_active_timers()
            if timers:
                print(f"\n⏱️  Active sessions ({len(timers)}):", file=sys.stderr)
                for title_slug, elapsed_minutes in timers.items():
                    print(f"   • {title_slug}: {elapsed_minutes} min", file=sys.stderr)
            else:
                print("💤 No active sessions", file=sys.stderr)

    async def save_submission(self, title_slug: str, content: str, item: dict) -> bool:
        """Save a submission to the database.

        Args:
            title_slug: The LeetCode problem slug (e.g., "two-sum")
            content: The submission code content
            item: Full submission details including status

        Returns:
            True if successful, False otherwise
        """
        status = item.get("status_msg", "Unknown")

        # Skip if content contains #TEST#
        if "#TEST#" in content:
            print(f"⊘ Skipping test submission: {title_slug}", file=sys.stderr)
            return False

        # Check if content contains #CHEAT# flag
        is_cheat = "#CHEAT#" in content

        time_spent_minutes = None
        if self.timer_manager.has_active_timer(title_slug):
            time_spent_minutes = self.timer_manager.get_elapsed_time(title_slug)
            print(
                f"⏱️  Current elapsed time: {time_spent_minutes} minutes",
                file=sys.stderr,
            )

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

            submission = await self.db.submission.create(data=submission_data)

            if status == "Accepted":
                if self.timer_manager.has_active_timer(title_slug):
                    self.timer_manager.stop(title_slug)
                self.timer_manager.start(title_slug)
                print("🔄 Timer restarted for accepted solution", file=sys.stderr)

            cheat_flag = " [CHEAT - needs revisit]" if is_cheat else ""
            time_info = f" ({time_spent_minutes}min)" if time_spent_minutes else ""
            print(
                f"✓ Submission saved successfully: {submission.id} {title_slug} {status}{cheat_flag}{time_info}",
                file=sys.stderr,
            )

            return True

        except Exception as e:
            print(f"✗ Error saving submission: {e}", file=sys.stderr)
            return False

    async def start(self):
        """Start the TCP server."""
        await self.db.connect()
        print(
            f"🚀 Submission server started on {self.host}:{self.port}", file=sys.stderr
        )

        # Start background task for logging active sessions
        asyncio.create_task(self.log_active_sessions())

        server = await asyncio.start_server(self.handle_client, self.host, self.port)

        async with server:
            await server.serve_forever()

    async def handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ):
        """Handle a client connection."""
        addr = writer.get_extra_info("peername")
        print(f"🔌 Client connected from {addr}", file=sys.stderr)

        try:
            while True:
                print(f"📖 Waiting for data from {addr}...", file=sys.stderr)
                data = await reader.readline()
                if not data:
                    print(
                        f"❌ No data received from {addr}, closing connection",
                        file=sys.stderr,
                    )
                    break

                print(f"📦 Received data: {data.decode().strip()}", file=sys.stderr)

                try:
                    request = json.loads(data.decode())
                    response = await self.handle_request(request)
                    writer.write((json.dumps(response) + "\n").encode())
                    await writer.drain()
                except json.JSONDecodeError as e:
                    print(f"⚠️  JSON decode error: {e}", file=sys.stderr)
                    error = {"error": f"Invalid JSON: {e}"}
                    writer.write((json.dumps(error) + "\n").encode())
                    await writer.drain()
                except Exception as e:
                    error = {"error": str(e)}
                    writer.write((json.dumps(error) + "\n").encode())
                    await writer.drain()

        finally:
            writer.close()
            await writer.wait_closed()

    async def handle_request(self, request: dict) -> dict:
        """Handle incoming requests and return response."""
        action = request.get("action")
        print(f"📨 Received request: {action}", file=sys.stderr)

        match action:
            case ServerAction.START_TIMER:
                title_slug = request["title_slug"]
                print(f"🎬 Starting timer for: {title_slug}", file=sys.stderr)
                self.timer_manager.start(title_slug, allow_multiple=False)
                return {
                    "success": True,
                    "action": ServerAction.START_TIMER,
                    "title_slug": title_slug,
                }

            case ServerAction.STOP_TIMER:
                title_slug = request["title_slug"]
                minutes = self.timer_manager.stop(title_slug)

                # Save session to database
                if minutes > 0:
                    await self.db.problemsession.create(
                        data={
                            "titleSlug": title_slug,
                            "timeSpentMinutes": minutes,
                            "isActive": False,
                        }
                    )

                return {
                    "success": True,
                    "action": ServerAction.STOP_TIMER,
                    "title_slug": title_slug,
                    "minutes": minutes,
                }

            case ServerAction.GET_ACTIVE_TIMERS:
                timers = self.timer_manager.get_active_timers()
                return {
                    "success": True,
                    "action": ServerAction.GET_ACTIVE_TIMERS,
                    "timers": timers,
                }

            case ServerAction.GET_ACTIVE_SESSIONS:
                timers = self.timer_manager.get_active_timers()
                sessions = []
                for title_slug, elapsed_minutes in timers.items():
                    sessions.append(
                        {
                            "title_slug": title_slug,
                            "elapsed_minutes": elapsed_minutes,
                            "status": "active",
                        }
                    )
                return {
                    "success": True,
                    "action": ServerAction.GET_ACTIVE_SESSIONS,
                    "sessions": sessions,
                    "count": len(sessions),
                }

            case ServerAction.SAVE_SUBMISSION:
                title_slug = request["title_slug"]
                content = request["content"]
                item = request["item"]
                print(f"💾 Saving submission for: {title_slug}", file=sys.stderr)
                success = await self.save_submission(title_slug, content, item)
                return {
                    "success": success,
                    "action": ServerAction.SAVE_SUBMISSION,
                    "title_slug": title_slug,
                }

            case _:
                return {"error": f"Unknown action: {action}"}


async def main():
    """Main entry point."""
    server = SubmissionServer()
    await server.start()


def run():
    """CLI entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
