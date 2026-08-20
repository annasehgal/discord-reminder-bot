# Discord Reminder Bot
`discord-reminder-bot` is an open-source, privacy-aware Discord bot that helps users manage reminders from external services such as academic calendars and learning platforms. It retrieves selected events, formats their relevant details into consistent Discord reminders, and requires user approval before sending them. The bot is designed to support multiple Discord servers, configurable courses/event sources, role-based authorization, rate limiting, persistent scheduling, and reliable notification delivery.

# Architecture:
The project architecture is documented separately and will evolve alongside the implementation.

### System Overview

Provides the high-level system structure and key workflows, including assignment retrieval, reminder scheduling, and moderator approval.

* [System Overview](docs/architecture/system-overview.md)

### Component Architecture

Describes the responsibilities and interactions of the application's major components, including the Discord bot, reminder service, Canvas integration, scheduler, persistence, and cache.

* [Component Architecture](docs/architecture/component-architecture.md)

### Architecture Decision Records

Technology and architectural decisions are documented as Architecture Decision Records.

* [Architecture Decision Records](docs/decisions/)

### Diagrams

Architecture diagrams are maintained under:

* `docs/architecture/diagrams/`

## Development

The project uses feature branches and pull requests for development. Architectural and technology decisions should be documented through the project's ADRs when appropriate.

## License

This project is licensed under the [AGPL-3.0](LICENSE).
