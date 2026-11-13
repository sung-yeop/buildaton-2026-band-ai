# Band Development Team

Role instructions, operating rules, task templates, and runtime records for a development team in Band Desktop.

- [Agent setup and workflow](Agents/README.md)
- [Shared operating rules](Agents/common.md)
- [Recorded runtime settings](Agents/runtime-settings.md)
- [Local infrastructure: Cognee memory and an independent Neo4j graph](infra/README.md)

The current practice team uses Coordinator, Code Author, and Code Reviewer. The six-role instructions are a proposed configuration; saving these files does not change Band settings.

This repository manages the development factory. Keep judged result repositories and official challenge materials separate. Local `band-work/`, `sf-buildathon-2026/`, and raw room exports are excluded by `.gitignore`.

`.gitkeep` is a convention for tracking an otherwise empty directory. It does not exclude uploads; `.gitignore` does that. `Agents/` contains actual files and needs no `.gitkeep`.
