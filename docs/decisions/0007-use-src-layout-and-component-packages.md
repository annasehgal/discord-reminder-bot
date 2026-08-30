# Use a src Layout Mapped to Architecture Components

## Context and Problem Statement

The architecture documents define Discord, approval, reminder, Canvas, scheduler, persistence, and cache components, but the repository previously had empty `src/` and `tests/` directories.

How should application code be packaged, and how should files map to those components so contributors can find the right place to change behavior?

## Considered Options

* A `src/` layout with one package (`discord_reminder_bot`) and one subdirectory per architecture component
* A flat package with all modules in a single directory
* Multiple top-level packages (bot, services, integrations)
* An application framework layout (Django or FastAPI project tree)

## Decision Outcome

Chosen option: "A `src/` layout with one package (`discord_reminder_bot`) and one subdirectory per architecture component", because

* `src/` keeps the installable package separate from `tests/`, `docs/`, and repository config.
* Package names follow the component architecture instead of inventing a second structure.
* Unimplemented areas can live as stubs in the correct package without mixing Discord I/O into reminder logic.

### What is where

| Path | Role |
| ---- | ---- |
| `pyproject.toml` | Package metadata, dependencies, pytest and ruff settings, console script |
| `requirements.txt` | Runtime dependencies for environments that do not use `pyproject.toml` |
| `requirements-dev.txt` | Test and lint tools |
| `.env.example` | Documented environment variables (no secrets) |
| `src/discord_reminder_bot/__main__.py` | Process entry: logging, `Config.from_env()`, start the bot |
| `src/discord_reminder_bot/config.py` | Typed configuration loaded from the environment |
| `src/discord_reminder_bot/bot/` | Discord client, prefix commands, event handlers |
| `src/discord_reminder_bot/bot/client.py` | `ReminderBot` wiring: persistence, cache, reminder service, approval, scheduler |
| `src/discord_reminder_bot/bot/commands/` | Discord commands (`ping` and future commands) |
| `src/discord_reminder_bot/bot/events/` | Discord events (`on_ready` and future events) |
| `src/discord_reminder_bot/approval/` | Moderator approval workflow |
| `src/discord_reminder_bot/reminders/` | Reminder models and core reminder service |
| `src/discord_reminder_bot/canvas/` | Canvas LMS API client |
| `src/discord_reminder_bot/scheduler/` | Background reminder tasks |
| `src/discord_reminder_bot/persistence/` | Durable state that must survive restarts |
| `src/discord_reminder_bot/cache/` | Temporary in-memory cache |
| `tests/` | Automated tests (`conftest.py`, config and cache tests) |
| `docs/architecture/` | System and component design |
| `docs/decisions/` | Architecture Decision Records |

Run the bot with `python -m discord_reminder_bot` or the `discord-reminder-bot` console script after an editable install.

## Consequences

### Positive

* File location matches the documented component, which reduces guesswork during review.
* Tests import the installed package instead of relying on ad-hoc `sys.path` hacks.
* New features have an obvious home (commands under `bot/commands/`, reminder rules under `reminders/`).

### Negative

* Empty or stub packages add files before those components are implemented.
* Wiring currently lives on `ReminderBot` in `bot/client.py`; a dedicated composition root may be needed later if construction grows.

## More Information

* [Component Architecture](../architecture/component-architecture.md)
* Related decisions: [0005-use-python.md](0005-use-python.md), [0010-stub-unimplemented-components.md](0010-stub-unimplemented-components.md)
