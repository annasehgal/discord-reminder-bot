"""Reminder domain models."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum


class ApprovalStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"


@dataclass
class Reminder:
    """A scheduled reminder derived from an external event or assignment."""

    id: str
    title: str
    due_at: datetime
    source: str
    channel_id: int | None = None
    approval_status: ApprovalStatus = ApprovalStatus.PENDING
    metadata: dict[str, str] = field(default_factory=dict)
