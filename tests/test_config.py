"""Tests for application configuration."""

import pytest

from discord_reminder_bot.config import Config


def test_config_from_env(sample_env: None) -> None:
    config = Config.from_env()
    assert config.discord_token == "test-token"
    assert config.discord_guild_id is None
    assert config.canvas_api_url is None


def test_config_requires_discord_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DISCORD_TOKEN", raising=False)
    with pytest.raises(ValueError, match="DISCORD_TOKEN"):
        Config.from_env()


def test_config_parses_guild_id(sample_env: None, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DISCORD_GUILD_ID", "123456789")
    config = Config.from_env()
    assert config.discord_guild_id == 123456789
