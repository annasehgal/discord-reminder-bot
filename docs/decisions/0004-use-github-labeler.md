# GitHub Labels and Pull Request Labeling

## Purpose

This document defines the labels used in the repository and how pull requests are automatically categorized.

Labels should provide useful information about the purpose or scope of a change without replacing the pull request title or description.

## Label Categories

### Type Labels

These labels describe what kind of change is being made.

* `feature` — Adds new functionality
* `bug` — Fixes incorrect or unexpected behavior
* `docs` — Documentation-only changes
* `refactor` — Restructures existing code without changing behavior
* `test` — Adds or modifies tests
* `chore` — Maintenance or repository configuration
* `ci` — Continuous integration or GitHub Actions changes

### Area Labels

These labels describe which part of the repository is affected.

* `architecture` — System architecture or design
* `backend` — Backend application code
* `discord` — Discord bot functionality or integrations
* `database` — Database-related changes
* `documentation` — Documentation and project guides
* `github` — GitHub repository configuration, templates, or automation

## Pull Request Labeling

Pull requests should receive labels based on the files or areas they modify.

The GitHub Actions Labeler workflow may automatically apply labels based on configured file paths.

For example:

| Changed Area           | Label           |
| ---------------------- | --------------- |
| `docs/**`              | `documentation` |
| `docs/architecture/**` | `architecture`  |
| `docs/decisions/**`    | `decisions` |
| `.github/**`           | `github`        |
| `src/**`               | `backend`       |
| `tests/**`             | `test`          |

Type labels such as `feature`, `bug`, `refactor`, and `docs` may be added manually or through future automation when the repository has enough implementation history to justify it.

## Labeling Principles

* Keep the label set small and useful.
* Prefer labels that communicate information not already obvious from the PR title.
* Do not create labels solely for the sake of having more labels.
* Update this document when the repository's labeling conventions change.
* Automation should follow the conventions documented here.

## GitHub Actions

The repository uses GitHub Actions to automate pull request labeling based on changed files.

The labeler configuration should be maintained alongside the workflow and updated when repository structure changes.

## Current Status

The labeling system is being established before the main application implementation.

Additional labels may be introduced as the project develops and new areas of the system become necessary.

