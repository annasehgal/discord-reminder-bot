"""Entry point for running the Discord Reminder Bot."""

import asyncio
import logging
import sys

from discord_reminder_bot.bot.client import create_bot
from discord_reminder_bot.config import Config


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


async def _run() -> None:
    config = Config.from_env()
    bot = create_bot(config)
    async with bot:
        await bot.start(config.discord_token)


def main() -> None:
    _configure_logging()
    try:
        asyncio.run(_run())
    except KeyboardInterrupt:
        logging.getLogger(__name__).info("Shutting down.")
    except ValueError as exc:
        logging.getLogger(__name__).error("%s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
