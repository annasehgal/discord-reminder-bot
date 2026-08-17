# Use GitHub Pull Requests for Merging

## Context and Problem Statement

The project uses branches to isolate development changes from the `main` branch.
A process is needed for merging completed changes back into `main`.

Should branches be merged locally using Git, or should changes be merged through
GitHub Pull Requests?

## Considered Options

- Merge branches locally using Git
- Merge branches through GitHub Pull Requests

## Decision Outcome

Chosen option: "Merge branches through GitHub Pull Requests", because

- Pull Requests provide a clear review point before changes are merged into `main`.
- The changes and commit history can be reviewed through GitHub.
- Pull Requests provide a workflow that can support automated checks in the future.
- The workflow is consistent with common collaborative software development practices.

Although this is currently a personal project and does not require another person
to approve changes, Pull Requests will still be used to review changes before
merging them into `main`.

## Consequences

### Positive

- Changes can be reviewed before being merged into `main`.
- The Pull Request provides a record of what changed and why.
- The workflow can later incorporate CI checks and required reviews.
- It provides experience with a collaborative GitHub workflow.

### Negative

- Merging through a Pull Request adds an additional step compared with merging locally.
- For a personal project, reviewing your own Pull Requests adds some overhead.

## More Information

- [GitHub Pull Requests documentation](https://docs.github.com/en/pull-requests)
