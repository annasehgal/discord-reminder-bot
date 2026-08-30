# Load Configuration from Environment Variables

## Context and Problem Statement

The bot needs a Discord token and will later need Canvas credentials and optional development settings such as a guild ID. Secrets must not be committed to the repository.

How should runtime configuration be supplied?

## Considered Options

* Environment variables loaded via python-dotenv, with `.env.example` as the documented template
* A committed YAML or TOML config file plus a separate secrets file
* Command-line flags for every setting
* A hosted secrets manager from the first version

## Decision Outcome

Chosen option: "Environment variables loaded via python-dotenv, with `.env.example` as the documented template", because

* Bot tokens and API keys are already commonly stored as environment variables in deployment.
* `.env` is gitignored; `.env.example` lists names without values.
* `Config.from_env()` fails fast when `DISCORD_TOKEN` is missing instead of starting a half-configured bot.

Current variables:

* `DISCORD_TOKEN` (required)
* `DISCORD_GUILD_ID` (optional, development)
* `CANVAS_API_URL` and `CANVAS_API_TOKEN` (optional until Canvas is implemented)

## Consequences

### Positive

* Secrets stay out of git if `.env` is not committed.
* Local setup is copy `.env.example` to `.env` and fill values.
* Tests can set environment variables without writing files.

### Negative

* Contributors must remember to create `.env`; a missing token only appears at startup.
* dotenv files are not a substitute for a production secrets manager.
* Typed validation beyond presence of `DISCORD_TOKEN` is still minimal.

## More Information

* Implementation: `src/discord_reminder_bot/config.py`
* Template: `.env.example`
* Related decision: [0006-use-discord-py.md](0006-use-discord-py.md)
