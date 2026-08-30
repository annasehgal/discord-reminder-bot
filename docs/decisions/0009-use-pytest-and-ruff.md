# Use pytest and ruff for Tests and Linting

## Context and Problem Statement

The first application code needs a way to run automated tests and a consistent style/lint check without a full CI matrix yet.

Which test runner and linter should the project use?

## Considered Options

* pytest plus ruff
* unittest plus flake8 or pylint
* pytest plus black, isort, and flake8 as separate tools
* No test or lint tooling until more features exist

## Decision Outcome

Chosen option: "pytest plus ruff", because

* pytest is the usual Python test runner and already has `pytest-asyncio` for async tests.
* ruff covers lint and import sorting in one tool with a short config in `pyproject.toml`.
* Tests live in `tests/` and target the installed `discord_reminder_bot` package.

The first tests cover configuration loading and the in-memory cache. Discord login and reminder delivery are not automated in this decision.

Automated CI for pytest and ruff is not required by this decision; [0001-use-branches-for-development.md](0001-use-branches-for-development.md) still notes that CI may be added later.

## Consequences

### Positive

* Contributors can run `pytest` and `ruff check src tests` locally.
* Config and cache behavior is checked without a Discord token.
* One linter reduces overlapping style tools.

### Negative

* Bot connectivity still needs a manual Discord check.
* Stubs have little to test until they are implemented.
* CI is not yet enforcing these tools on pull requests.

## More Information

* Config: `pyproject.toml` (`[tool.pytest.ini_options]`, `[tool.ruff]`)
* Tests: `tests/`
* Related decision: [0007-use-src-layout-and-component-packages.md](0007-use-src-layout-and-component-packages.md)
