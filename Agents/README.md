# Agent Setup

## Status

- Current practice team: `@yeop99/coordinator`, `@yeop99/code-author`, and `@yeop99/code-reviewer`.
- The six roles below are the agreed team design. They have not yet been created, switched over, or applied to Band.
- [runtime-settings.md](runtime-settings.md) records saved settings read on 2026-11-13, not necessarily the effective settings of every running session.

| Role | Instructions | Responsibility |
|---|---|---|
| Coordinator | [coordinator.md](roles/coordinator.md) | Assignment, dependencies, blockers, stage completion |
| Planner | [planner.md](roles/planner.md) | Current specification, interface interpretation, verification plan |
| Backend | [backend.md](roles/backend.md) | Server, data, integrations, concurrency, recovery |
| Frontend / Integrator | [frontend-integrator.md](roles/frontend-integrator.md) | UI, real server integration, integration commit |
| Reviewer | [reviewer.md](roles/reviewer.md) | Independent code, design, and specification review |
| QA | [qa.md](roles/qa.md) | Runtime verification, defect reproduction, retesting |

Do not invent UI work to keep Frontend busy when the current requirements have no UI. The original implementer repairs defects; there is no separate Repair role.

## Apply in Band

1. Set each agent's runtime, model, reasoning effort, and absolute working directory explicitly.
2. Apply [common.md](common.md) as **Team guidelines**. When importing a guidelines file, save its contents and verify that the intended existing rooms receive them.
3. Connect each role file through **Instructions → Choose instructions file**.
4. Without team guidelines, supply both the shared rules and role instructions in the agent's Instructions. Do not assume relative document references are automatically loaded.
5. Assign work to actual created `@handles`, not just role names. Rehearse handoffs, responses, and permissions in a fresh room.

The installed Band CLI supports `agent create --instructions-file`, `agent create --dry-run`, and `team create --guidelines-file`. Consult the installed version's `--help` for complete options. This repository does not contain provisioning scripts with account keys or machine-specific executable paths.

## Sources of truth

| Information | Authoritative location |
|---|---|
| Owner, status, prerequisites, blocker | Band Room tasks |
| Actual handoffs, decisions, verification reports | Band room messages |
| Source code, interface definitions, design decisions | Git and Markdown |
| Execution evidence | Test logs and reports for the target commit |
| Optional shared memory | Cognee entries with original references and verification status |
| Explicit domain graph | Independently designed Neo4j schema and data, with source provenance |

Agent tasks are personal checklists. Manage team assignments through Room tasks. Do not introduce a second status system in Linear. [Local infrastructure](../infra/README.md) supplies a Compose configuration for Cognee and an independent Neo4j graph; deployment and agent connections require the documented setup. Neither service replaces the task board.

## Templates

- [Task assignment](templates/task.md)
- [Implementation handoff](templates/handoff.md)
- [Independent verification](templates/verification.md)

These are Markdown forms for people and agents, not a custom parser or enforcement engine. Operating rules do not replace Band permission controls.

## Competition submission

This directory is not the submitted `mandates/` directory. Preserve the actual shared rules and role instructions used in the final run together in each seat's mandate, using the actual seat name as the filename. Start each file with the actual `Harness:`, exact `Model:`, and, when available, `Effort:`. Do not guess inherited defaults.

Generic role instructions must not contain challenge-specific API paths, field names, error codes, or test IDs. Dispatch the full current requirements in task messages. Never preload unopened future-stage specifications into memory or the graph.

Use a fresh room and a fresh result repository for the final run. The practice team's approval prompts are not a validated configuration for an unattended submission run.

## References

- [Band agents and teams](https://docs.band.ai/band-desktop/agents)
- [Band room work management](https://docs.band.ai/band-desktop/rooms)
- [Participant guide](https://github.com/band-ai/sf-buildathon-2026/blob/main/docs/participant-guide.md)
