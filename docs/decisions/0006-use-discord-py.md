# Use discord.py for Discord Integration

## Context and Problem Statement

The bot is the primary interface for users and moderators. A library is needed to connect to Discord, handle commands and events, and send messages.

Which Discord library should the Python application use?

## Considered Options

* discord.py
* Nextcord, PyCord, or other discord.py forks
* Interactions.py or a slash-command-only library
* Direct REST and Gateway clients without a framework

## Decision Outcome

Chosen option: "discord.py", because

* It is the established Python Discord library and matches the Python language decision.
* `commands.Bot` supports prefix commands immediately (`!ping`) and can grow into cogs and slash commands later.
* It keeps Discord-specific code in the `bot/` package rather than spreading Gateway details through the reminder service.

The current client enables the default intents plus `message_content` so prefix commands can be read in guilds. Slash-command migration is not part of this decision and can be recorded later if the command surface grows.

## Consequences

### Positive

* Discord connection, commands, and events have a standard API.
* The bot layer can stay separate from reminder, Canvas, and persistence logic.
* A small connectivity command (`!ping`) can verify the token and intents without implementing reminders.

### Negative

* discord.py requires a bot token and privileged intents for message content.
* Forks and slash-first libraries may offer different defaults; switching later would touch the `bot/` package.
* Prefix commands are less discoverable than slash commands.

## More Information

* [discord.py](https://github.com/Rapptz/discord.py)
* Related decision: [0005-use-python.md](0005-use-python.md)
* Implementation: `src/discord_reminder_bot/bot/`
