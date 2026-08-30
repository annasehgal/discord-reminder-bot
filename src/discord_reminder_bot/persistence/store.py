"""Stores reminders and approval state that must survive bot restarts."""

from discord_reminder_bot.reminders.models import Reminder


class PersistenceStore:
    """Persistence layer for reminders and related state."""

    async def save_reminder(self, reminder: Reminder) -> None:
        raise NotImplementedError

    async def get_reminder(self, reminder_id: str) -> Reminder | None:
        raise NotImplementedError

    async def list_reminders(self) -> list[Reminder]:
        raise NotImplementedError
