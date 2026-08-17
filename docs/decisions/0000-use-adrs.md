# Adopt MADR for Architectural Decision Records

## Context and Problem Statement

This project needs a consistent way to document important technical and architectural decisions.

The goal is not only to document what was implemented, but also to preserve the reasoning behind significant decisions so that future contributors can understand the context, alternatives, and trade-offs.

Several approaches and tools were considered, including MADR, Excalidraw, draw.io, and the C4 Model.

## Considered Options

* MADR (Markdown Architectural Decision Records)
* Excalidraw
* draw.io (diagrams.net)
* C4 Model
* A custom documentation approach
* No formal decision-record process

## Decision Outcome

Chosen option: "MADR" for recording architectural and technical decisions.

MADR was selected because it provides a structured, lightweight format for documenting the context, options considered, decision outcome, and consequences of a decision.

Markdown also allows the decision records to live directly in the repository and be version-controlled alongside the project.

Diagramming tools and architectural modeling approaches may still be used where appropriate for the architecture documentation; they are not replacements for the decision-record format.

## Consequences

### Positive

* Important decisions have a permanent record.
* The reasoning behind decisions is preserved.
* Future contributors can understand why an approach was selected.
* Decisions are version-controlled alongside the project.
* The format is lightweight and does not require a separate documentation platform.

### Negative

* Writing ADRs introduces some documentation overhead.
* Not every implementation detail warrants an ADR.
* Architecture diagrams and ADRs serve different purposes and may need to be maintained separately.

## More Information

* [MADR](https://github.com/adr/madr)
* [Excalidraw](https://excalidraw.com/)
* [diagrams.net](https://www.diagrams.net/)
* [C4 Model](https://c4model.com/)
