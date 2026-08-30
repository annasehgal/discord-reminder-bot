"""Client for retrieving courses and assignments from Canvas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class CanvasAssignment:
    """Normalized assignment data from the Canvas API."""

    id: str
    name: str
    due_at: str | None
    course_id: str


class CanvasClient:
    """Communicates with the Canvas REST API."""

    def __init__(self, api_url: str, api_token: str) -> None:
        self._api_url = api_url.rstrip("/")
        self._api_token = api_token

    async def fetch_assignments(self, course_id: str) -> list[CanvasAssignment]:
        """Retrieve assignments for a course."""
        raise NotImplementedError

    async def _request(self, path: str, **params: Any) -> Any:
        """Perform an authenticated Canvas API request."""
        raise NotImplementedError
