"""Slash and prefix command registration."""

from discord.ext import commands

from discord_reminder_bot.bot.commands.ping import ping


def setup_commands(bot: commands.Bot) -> None:
    """Register bot commands."""
    bot.add_command(ping)
