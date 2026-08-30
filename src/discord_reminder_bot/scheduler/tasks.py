"""Runs reminder-related background work independently of Discord commands."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord.ext import commands

    from discord_reminder_bot.reminders.service import ReminderService


class Scheduler:
    """Detects due reminders and triggers delivery."""

    def __init__(
        self,
        reminder_service: ReminderService,
        bot: commands.Bot,
    ) -> None:
        self._reminder_service = reminder_service
        self._bot = bot

    async def start(self) -> None:
        """Start background scheduling loops."""
        raise NotImplementedError

    async def stop(self) -> None:
        """Gracefully stop background tasks."""
        raise NotImplementedError
