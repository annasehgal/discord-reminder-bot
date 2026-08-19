# System Overview

## Purpose

The Discord Reminder Bot is a Discord-based reminder system that retrieves assignment information from Canvas, processes upcoming deadlines, schedules reminders, and delivers them to users through Discord.

The system is designed to reduce manual tracking of assignments while allowing moderators to review and approve reminder content before it is delivered.

## System Architecture

```mermaid
flowchart TD
    U[Discord Users / Moderators]
    D[Discord Bot]

    C[Canvas API]
    R[Reminder Service]
    S[Scheduler / Background Tasks]
    P[Persistence]
    CA[Cache]

    U --> D
    D --> C
    D --> R

    C --> R
    R --> S
    R --> P
    R --> CA

    S --> D
    D --> U
```

## Major Components

### Discord Bot

The Discord bot provides the primary interface for users and moderators.

Responsibilities include:

* Receiving Discord commands and events
* Sending reminder messages
* Handling moderator approval
* Processing user interactions
* Routing requests to the appropriate application component

### Canvas Integration

The Canvas integration retrieves assignment and course information from the Canvas API.

Responsibilities include:

* Fetching assignments
* Retrieving assignment due dates
* Providing course and assignment information to the reminder service
* Handling communication with the external Canvas API

### Reminder Service

The reminder service contains the core application logic.

Responsibilities include:

* Processing assignments retrieved from Canvas
* Determining when reminders should be sent
* Handling time-zone conversions
* Grouping multiple reminders into a single message when appropriate
* Tracking reminder and approval state

### Scheduler / Background Tasks

The scheduler is responsible for running reminder-related tasks without requiring a user to manually trigger them.

Responsibilities include:

* Checking for upcoming reminders
* Triggering scheduled reminder jobs
* Running recurring background tasks
* Coordinating reminder delivery with the Discord bot

### Persistence

Persistent storage maintains application data that must survive beyond the lifetime of the running bot.

Potential data includes:

* User preferences
* Assignment information
* Reminder configuration
* Approval status
* Reminder history

The specific persistence technology is determined separately from the system architecture.

### Cache

The cache stores frequently accessed or temporary data to reduce unnecessary requests and improve application responsiveness.

Potential cached information includes:

* Recently retrieved Canvas assignments
* Temporary reminder state
* Frequently accessed user or course information

## Key Flows

### Assignment and Reminder Flow

```mermaid
sequenceDiagram
    participant C as Canvas API
    participant R as Reminder Service
    participant S as Scheduler
    participant D as Discord Bot
    participant U as User

    R->>C: Request assignment data
    C-->>R: Return assignments
    R->>R: Process assignments
    R->>S: Schedule reminders
    S->>D: Trigger reminder
    D->>U: Send Discord notification
```

### Approval Flow

```mermaid
flowchart LR
    A[Assignment / Reminder Created]
    B[Approval State Tracked]
    C[Moderator Reviews]
    D{Approved?}
    E[Schedule / Send Reminder]
    F[Request Changes]

    A --> B
    B --> C
    C --> D
    D -->|Yes| E
    D -->|No| F
    F --> C
```

### Time-Zone Handling

Assignment deadlines may originate from Canvas in a specific time zone while users may operate in different time zones.

The reminder service therefore handles time-zone conversion when determining and displaying reminder times.

```text
Canvas Assignment
       │
       ▼
Due Date + Source Time Zone
       │
       ▼
Reminder Service
       │
       ├──► User Time Zone A
       │
       └──► User Time Zone B
```

## Design Goals

The system architecture prioritizes:

* Clear separation between Discord interaction and application logic
* Reliable background reminder scheduling
* Integration with the Canvas API
* Explicit moderator approval
* Time-zone-aware reminders
* Reduced duplicate API requests through caching
* Persistence for state that must survive bot restarts
* Grouped notifications to avoid unnecessary Discord message spam

## Related Documentation

* Component Architecture
* Architecture Decision Records
* GitHub Actions and Repository Automation

