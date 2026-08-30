# Use Python 3.11+ as the Implementation Language

## Context and Problem Statement

The Discord Reminder Bot needs an implementation language for the Discord client, reminder logic, Canvas integration, scheduling, persistence, and tests.

Which language should the application be written in, and what minimum version should be required?

## Considered Options

* Python 3.11+
* TypeScript / Node.js
* Go
* A mix of languages (for example a TypeScript bot with a Python backend)

## Decision Outcome

Chosen option: "Python 3.11+", because

* Python is widely used for bots, HTTP integrations, and scripting, which matches this project's mix of Discord, Canvas, and background work.
* Python 3.11+ provides `StrEnum`, improved typing, and asyncio support used by the current package.
* A single language keeps the first implementation small and easier to review.

## Consequences

### Positive

* Contributors can work in one language across Discord, services, and tests.
* The `src/` layout and `pyproject.toml` packaging are standard for Python projects.
* Async Discord and HTTP libraries are readily available.

### Negative

* TypeScript has a large Discord ecosystem (`discord.js`) that this project will not use.
* Python packaging and virtual environments add setup steps for new contributors.

## More Information

* Related decision: [0006-use-discord-py.md](0006-use-discord-py.md)
* Package metadata: `pyproject.toml` (`requires-python = ">=3.11"`)
