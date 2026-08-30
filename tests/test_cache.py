"""Tests for the in-memory cache store."""

from discord_reminder_bot.cache.store import CacheStore


def test_cache_set_and_get() -> None:
    cache = CacheStore()
    cache.set("key", "value")
    assert cache.get("key") == "value"


def test_cache_delete() -> None:
    cache = CacheStore()
    cache.set("key", "value")
    cache.delete("key")
    assert cache.get("key") is None


def test_cache_clear() -> None:
    cache = CacheStore()
    cache.set("a", 1)
    cache.set("b", 2)
    cache.clear()
    assert cache.get("a") is None
    assert cache.get("b") is None
