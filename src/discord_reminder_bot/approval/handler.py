"""Handles moderator review of reminders before delivery."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord_reminder_bot.reminders.service import ReminderService


class ApprovalHandler:
    """Presents reminders for moderator approval and tracks approval state."""

    def __init__(self, reminder_service: ReminderService) -> None:
        self._reminder_service = reminder_service

    async def request_approval(self, reminder_id: str) -> None:
        """Present a reminder to moderators for review."""
        raise NotImplementedError

    async def approve(self, reminder_id: str, moderator_id: int) -> None:
        """Mark a reminder as approved and schedule delivery."""
        raise NotImplementedError

    async def request_changes(self, reminder_id: str, moderator_id: int, feedback: str) -> None:
        """Send a reminder back for revision."""
        raise NotImplementedError
