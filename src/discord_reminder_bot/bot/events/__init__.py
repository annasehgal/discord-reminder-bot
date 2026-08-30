"""Discord event handlers."""

import logging

from discord.ext import commands

logger = logging.getLogger(__name__)


def setup_events(bot: commands.Bot) -> None:
    """Register bot event handlers."""

    @bot.event
    async def on_ready() -> None:
        logger.info(
            "Logged in as %s (id=%s)",
            bot.user,
            bot.user.id if bot.user else "unknown",
        )
