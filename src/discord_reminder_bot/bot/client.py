"""Discord bot client factory."""

import discord
from discord.ext import commands

from discord_reminder_bot.approval.handler import ApprovalHandler
from discord_reminder_bot.bot.commands import setup_commands
from discord_reminder_bot.bot.events import setup_events
from discord_reminder_bot.cache.store import CacheStore
from discord_reminder_bot.config import Config
from discord_reminder_bot.persistence.store import PersistenceStore
from discord_reminder_bot.reminders.service import ReminderService
from discord_reminder_bot.scheduler.tasks import Scheduler


class ReminderBot(commands.Bot):
    """Discord bot wired to application services."""

    def __init__(self, config: Config) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix="!", intents=intents)
        self.config = config
        self.persistence = PersistenceStore()
        self.cache = CacheStore()
        self.reminder_service = ReminderService(
            persistence=self.persistence,
            cache=self.cache,
        )
        self.approval_handler = ApprovalHandler(reminder_service=self.reminder_service)
        self.scheduler = Scheduler(
            reminder_service=self.reminder_service,
            bot=self,
        )


def create_bot(config: Config) -> ReminderBot:
    """Create and configure the Discord bot."""
    bot = ReminderBot(config)
    setup_commands(bot)
    setup_events(bot)
    return bot
