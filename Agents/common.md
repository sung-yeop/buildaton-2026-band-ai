# Shared Operating Rules

## Requirements and scope

- Implement and verify the requirements currently supplied. Preserve contracts already fixed by the specification.
- For sequential challenges, freeze the current result before opening the next specification. Do not modify earlier results after reading later specifications.
- Resolve ambiguity within the team using evidence and record the rationale in the room. Do not add unspecified features.
- Do not modify official tests or specifications, or manufacture success through implementations tailored only to test inputs.

## Assignment and handoff

- Band Room tasks are the source of truth for team work. Give each task a primary owner and explicit completion criteria.
- Distinguish completion of personal Agent tasks from completion of shared work.
- Confirm the recipient is in the room and address the actual `@handle` directly.
- Every handoff includes the complete task description, full relevant requirements, absolute repository path, change scope, and completion criteria. Links or message IDs alone are insufficient.
- Split long requirements into numbered direct messages.
- Implementation readiness requests verification. Final completion requires independent verification of the same integrated commit.

## Files, Git, and integration

- Modify assigned files and modules only. Notify the owner and Coordinator before changing anything outside that boundary.
- Use separate worktrees or working directories for parallel implementation, or serialize edits and commits. Never switch branches or stage/commit concurrently in one checkout.
- Inspect existing changes before starting. Do not discard or overwrite another contributor's uncommitted work.
- Record the full commit SHA for each result. Changes after handoff require verification of the new SHA.
- Preserve author history during integration. Do not amend, rebase, or squash commits used as submission evidence.
- Assign one editing owner for shared startup configuration and dependency files per task.

## Verification and failures

- Reviewer checks code against requirements; QA checks running behavior. Both must receive the original requirements.
- Run only one heavy official container check at a time. Record ports and process/container ownership.
- Preserve failed-run logs and use a new output directory for every run.
- Distinguish product defects, environment failures, and missing permissions. Never report an unexecuted check as passed.
- Send failures to the original implementer with expected behavior, actual behavior, reproduction commands, and target SHA.
- Do not repeat the same failure without a changed cause or new hypothesis. Report a blocker and the condition needed to resume when there is no new evidence.
- Stop or delete only resources created by your own work.

## Memory and permissions

- Store decisions and lessons with their original sources, relevant commit, and verification status. Past verification does not establish correctness after code changes.
- Never store unopened specifications, credentials, or personal information in shared memory or the graph.
- Room and Git records provide reproducible evidence. Memory helps locate those records.
- Cognee owns agent memory. The independent Neo4j graph has an explicitly designed schema; do not assume synchronization or write Cognee internals into it.
- Respect permission boundaries. Practice runs may request required environment approvals.
- Validate permissions before unattended submission runs. If a new approval is required during execution, report the blocker and evidence instead of bypassing it.
