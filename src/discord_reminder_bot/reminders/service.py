"""Reminder creation, scheduling, and state management."""

from __future__ import annotations

from typing import TYPE_CHECKING

from discord_reminder_bot.reminders.models import Reminder

if TYPE_CHECKING:
    from discord_reminder_bot.cache.store import CacheStore
    from discord_reminder_bot.persistence.store import PersistenceStore


class ReminderService:
    """Core application logic for reminders."""

    def __init__(
        self,
        persistence: PersistenceStore,
        cache: CacheStore,
    ) -> None:
        self._persistence = persistence
        self._cache = cache

    async def create_reminder(self, reminder: Reminder) -> Reminder:
        """Persist a new reminder and return the stored record."""
        raise NotImplementedError

    async def get_reminder(self, reminder_id: str) -> Reminder | None:
        """Retrieve a reminder by ID."""
        raise NotImplementedError

    async def list_pending_reminders(self) -> list[Reminder]:
        """Return reminders awaiting approval or delivery."""
        raise NotImplementedError
