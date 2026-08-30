"""Test configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DISCORD_TOKEN", "test-token")
