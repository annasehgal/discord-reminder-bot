# Stub Unimplemented Components Until Their Technologies Are Chosen

## Context and Problem Statement

The component architecture requires reminder processing, Canvas access, approval, scheduling, and persistence. The first runnable increment only needs Discord login, configuration, and a connectivity command.

How should the remaining components exist in the codebase before their storage, HTTP, and scheduling libraries are selected?

## Considered Options

* Stub classes and methods that raise `NotImplementedError`, plus a working in-memory cache
* Implement SQLite, Redis, APScheduler, and a Canvas HTTP client in the same change as the boilerplate
* Omit packages entirely until each feature branch adds them

## Decision Outcome

Chosen option: "Stub classes and methods that raise `NotImplementedError`, plus a working in-memory cache", because

* Packages already match the architecture, so later work does not reshuffle the tree.
* `NotImplementedError` makes incomplete behavior obvious in tests and reviews.
* Persistence, Canvas HTTP, and the scheduler are still open technology choices and should get their own ADRs when selected.
* An in-memory `CacheStore` is enough for the cache component's first version because cached data is not the source of truth after a restart.

The Discord bot currently constructs these objects in `ReminderBot` so wiring is visible even while methods are unimplemented.

## Consequences

### Positive

* The bot can start and respond to `!ping` without a database or Canvas token.
* Future ADRs can record SQLite versus Postgres, Redis versus in-process cache, and the Canvas client library without undoing this layout.
* Reviewers can see intended interfaces (`ReminderService`, `CanvasClient`, `Scheduler`, `PersistenceStore`, `ApprovalHandler`).

### Negative

* Calling stub methods at runtime fails until those features are built.
* Interfaces may change when a real store or HTTP client is chosen.
* In-memory cache is lost on process restart and is not shared across hosts.

## More Information

* [Component Architecture](../architecture/component-architecture.md) (persistence technology is intentionally unspecified there)
* Related decision: [0007-use-src-layout-and-component-packages.md](0007-use-src-layout-and-component-packages.md)
* Stubs: `approval/`, `reminders/`, `canvas/`, `scheduler/`, `persistence/`
* Implemented now: `cache/store.py`, `bot/`, `config.py`
