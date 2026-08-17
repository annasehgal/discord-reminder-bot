# Use Branches for Development

## Context and Problem Statement

Changes should not be made directly on the `main` branch while developing the project.
How should changes be developed and integrated into the repository?

## Considered Options

- Make changes directly on `main`
- Create a branch for each change and merge it into `main` through a pull request

## Decision Outcome

Chosen option: "Create a branch for each change and merge it into `main` through a pull request", because

- It prevents unfinished work from being committed directly to `main`.
- It keeps individual changes isolated and easier to review.
- It creates a clear history of how changes were introduced.
- It establishes a workflow that can scale if the project grows or gains contributors.

For this personal project, pull requests do not currently require external approval.

Automated linting, formatting, and CI checks are not yet configured.

## Consequences

### Positive

- `main` remains the stable version of the project.
- Changes can be developed independently.
- Pull requests provide a place to review and describe changes.
- The workflow can scale to collaboration later.

### Negative

- Creating branches adds some overhead for small changes.
- Pull requests add an additional step before changes reach `main`.

## More Information

- Related decision: `0000-use-adrs.md`
