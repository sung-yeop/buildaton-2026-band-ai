# Recorded Runtime Settings

On 2026-11-13, selected fields were inspected using the installed Band CLI's `runtime template show --json --reveal`. These are **saved template values**, which may differ from the effective settings of current room sessions. No secret values or credentials are included.

| Setting | Coordinator | Code Author | Code Reviewer |
|---|---|---|---|
| Handle | `@yeop99/coordinator` | `@yeop99/code-author` | `@yeop99/code-reviewer` |
| Harness | Codex | Codex | Codex |
| Transport | `codex-app-server` | `codex-app-server` | `codex-app-server` |
| Explicit Model | `gpt-6.1-sol` | Unspecified (`null`) | Unspecified (`null`) |
| Explicit Effort | `medium` | Unspecified (`null`) | Unspecified (`null`) |
| Approval policy | `on-request` | `on-request` | Unspecified (`null`) |
| Tool sandbox | `workspace-write` | `danger-full-access` | Unspecified (`null`) |
| Authentication | Inherit runtime authentication | Inherit runtime authentication | Inherit runtime authentication |
| Working directory | Absolute path to `band-work/toy-result` in this repository | Same | Same |

An unspecified value does not mean no model or permissions are active. Inspect runtime defaults or session settings; do not invent values for submission documents.

Code Author uses an absolute path to the installed native Codex executable after a Node discovery failure. The other templates use `codex`. This path depends on the machine and installation version: discover it locally and verify it with Test runtime rather than copying another machine's path.

## Resolve before applying the new team

- Actual handles and instruction files for each role.
- Explicit model IDs and reasoning effort, verified in effective sessions.
- Absolute paths to the separate result repository and parallel workspaces.
- Permissions for files, Git, the Band socket, Docker, and browser checks.
- Differences between practice approvals and unattended submission execution.
- Optional memory connections and credential storage locations.

Code Author's broad tool access is an observed setting, not a recommended default for the new team. Broadening permissions or disabling prompts does not replace environment validation.
