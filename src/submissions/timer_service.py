"""
Timer management for tracking time spent on problems.
In-memory timer tracking with database persistence for sessions.
"""

from datetime import datetime
from typing import Dict, Optional


class TimerManager:
    """Manages active timers in memory."""

    def __init__(self):
        self._timers: Dict[str, datetime] = {}

    def start(self, title_slug: str, allow_multiple: bool = False) -> None:
        """Start a timer for a problem.

        Args:
            title_slug: The problem slug to start timer for
            allow_multiple: If True, allows multiple sessions (keeps existing timer running).
                           If False (default), clears all timers and starts fresh for this problem.
        """
        # Check if timer already exists for this problem
        existing_timer = title_slug in self._timers

        if existing_timer and allow_multiple:
            # Keep existing timer, don't restart
            elapsed = int(
                (datetime.now() - self._timers[title_slug]).total_seconds() / 60
            )
            print(f"⏱️  Timer already running for {title_slug} ({elapsed}min elapsed)")
            return

        # Clear all timers if allow_multiple is False
        if not allow_multiple and self._timers:
            if existing_timer:
                elapsed = int(
                    (datetime.now() - self._timers[title_slug]).total_seconds() / 60
                )
                print(
                    f"⏱️  Clearing all timers, restarting {title_slug} (was {elapsed}min)"
                )
            else:
                print(f"⏱️  Clearing {len(self._timers)} existing timer(s)")
            self._timers.clear()

        # Start the timer
        self._timers[title_slug] = datetime.now()
        print(f"⏱️  Timer started for {title_slug}")

    def stop(self, title_slug: str) -> int:
        """Stop a timer and return minutes spent."""
        if title_slug not in self._timers:
            return 0

        start_time = self._timers.pop(title_slug)
        time_delta = datetime.now() - start_time
        minutes_spent = max(1, int(time_delta.total_seconds() / 60))

        print(f"⏱️  Timer stopped for {title_slug}: {minutes_spent} minutes")
        return minutes_spent

    def get_active_timers(self) -> Dict[str, int]:
        """Get all active timers with elapsed time in minutes."""
        return {
            slug: int((datetime.now() - start).total_seconds() / 60)
            for slug, start in self._timers.items()
        }

    def has_active_timer(self, title_slug: str) -> bool:
        """Check if a timer is active for a problem."""
        return title_slug in self._timers

    def get_elapsed_time(self, title_slug: str) -> int:
        """Get elapsed time for an active timer without stopping it.

        Args:
            title_slug: The problem slug

        Returns:
            Elapsed minutes, or 0 if no active timer
        """
        if title_slug not in self._timers:
            return 0

        elapsed = int((datetime.now() - self._timers[title_slug]).total_seconds() / 60)
        return max(1, elapsed)
