"""Application configuration loaded from environment variables."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Runtime configuration for the bot and its integrations."""

    discord_token: str
    discord_guild_id: int | None
    canvas_api_url: str | None
    canvas_api_token: str | None

    @classmethod
    def from_env(cls) -> "Config":
        token = os.getenv("DISCORD_TOKEN", "").strip()
        if not token:
            raise ValueError("DISCORD_TOKEN is required")

        guild_id_raw = os.getenv("DISCORD_GUILD_ID", "").strip()
        guild_id = int(guild_id_raw) if guild_id_raw else None

        return cls(
            discord_token=token,
            discord_guild_id=guild_id,
            canvas_api_url=os.getenv("CANVAS_API_URL") or None,
            canvas_api_token=os.getenv("CANVAS_API_TOKEN") or None,
        )
