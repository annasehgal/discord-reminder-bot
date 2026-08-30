"""Basic connectivity command."""

from discord.ext import commands


@commands.command(name="ping", help="Check whether the bot is online.")
async def ping(ctx: commands.Context) -> None:
    latency_ms = round(ctx.bot.latency * 1000)
    await ctx.send(f"Pong! Latency: {latency_ms}ms")
