# Local Infrastructure

Run two independent services on each developer's machine. A single Compose file manages their lifecycle; it does not connect their data.

| Service | Purpose | Storage | Local endpoint |
|---|---|---|---|
| Cognee MCP | Agent memory: decisions, lessons, source references | Its own SQLite, LanceDB, and embedded Ladybug graph | `http://localhost:8765/mcp` |
| Neo4j Community | A knowledge graph whose schema we design explicitly | Independent Neo4j volume | Browser: `http://localhost:7474`; Bolt: `bolt://localhost:7687` |

Cognee's standalone MCP server includes its storage pipeline. Its graph is **not** the independent Neo4j database. See the [Cognee architecture](https://docs.cognee.ai/cognee-mcp/mcp-overview) and [graph store options](https://docs.cognee.ai/setup-configuration/graph-stores).

All local agents can connect to the same Cognee endpoint. Agent scoping and backend access control are disabled deliberately for one trusted local user, with `main_dataset` as the shared default. This does not provide isolation between agents or datasets. See [Cognee's scoping documentation](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/README.md).

Each developer has independent data. Git distributes configuration, not memory or database contents. These are development-factory services, not dependencies to silently add to the judged application.

## Setup

Requirements: a running Docker engine with Compose, internet access for image downloads and model requests, and an API key with access to the selected extraction model and embeddings. Allow room for both service limits (6 GiB total), Docker overhead, and any challenge containers. Images may require several GB of disk space.

From the repository root:

```sh
cd infra
cp -n .env.example .env
chmod 600 .env
```

Edit `.env` locally. Set `LLM_API_KEY`, an exact `LLM_MODEL` supported by your account and Cognee, and a unique `NEO4J_PASSWORD` of at least 8 characters. `openssl rand -hex 24` generates a suitable password. Empty required values cause Compose validation to fail. `.env` is ignored by Git.

The provided configuration uses OpenAI for both extraction and embeddings. It explicitly selects `text-embedding-3-small` with 1536 dimensions. To use another provider, change both configurations together using [Cognee's provider documentation](https://docs.cognee.ai/setup-configuration/embedding-providers); changing an embedding model on existing data requires a migration or re-ingestion. Model calls can incur charges and send supplied memory text to the provider.

All subsequent Compose commands run from `infra/`:

```sh
docker info
docker compose config --quiet
docker compose pull
docker compose up -d --wait --wait-timeout 300
docker compose ps
curl --fail http://localhost:8765/health
```

Use `config --quiet`: the full resolved configuration includes credentials. Ports bind only to loopback. Cognee has no authentication in this local configuration; do not expose it to a LAN or the internet. Services have separate networks and volumes, with no startup dependency on one another.

## Connect agents and verify behavior

Configure the actual harness used by each Band agent with a **Streamable HTTP** MCP server named `cognee`, URL `http://localhost:8765/mcp`. Use its installed configuration UI or CLI help, then restart the relevant session if required. A Band agent's existence does not prove it has inherited that harness's MCP settings.

Before relying on memory:

1. Confirm that a connected agent can discover Cognee memory tools.
2. Ask it to store a harmless, uniquely named rehearsal fact through `remember`, with the source reference and verification status.
3. Wait for ingestion to finish; a queued job is not a completed write. Inspect its reported status.
4. Ask a second agent connected to the same endpoint to retrieve that fact through `recall` using `main_dataset` where a dataset argument is exposed.
5. Run `docker compose restart cognee` and verify the same fact can still be retrieved. Delete only that rehearsal fact when finished.

The health endpoint checks service readiness, not working API credentials, completed ingestion, or cross-agent retrieval. Never ingest unopened future-stage specifications or secrets.

## Independent Neo4j graph

Open `http://localhost:7474`, connect to `bolt://localhost:7687`, and sign in as `neo4j` with your local password. Run `RETURN 1 AS ok;` to confirm access. See the [official Neo4j Docker guide](https://neo4j.com/docs/operations-manual/current/docker/introduction/).

We own this graph's node labels, relationships, uniqueness constraints, indexes, and provenance rules. No domain schema or sample records are installed automatically: the graph's intended questions must be defined first. Version the agreed schema and migrations in Git when that work begins. Plain Cypher is sufficient initially; no APOC or Graph Data Science plugins are installed.

Neo4j does not automatically expose an MCP endpoint. A driver integration or a separate MCP server must explicitly provide the desired graph operations. It is not included yet, and Cognee does not read or write this graph. Do not use the graph as a second Band task board.

## Stop, preserve, and update

```sh
docker compose logs --tail 100 cognee neo4j
docker compose stop
docker compose start
```

`docker compose down` removes this stack's containers and networks but keeps its named volumes. **Adding `--volumes` / `-v` deletes stored memory and graph data.** Do not use it for routine restarts or troubleshooting. Both Cognee volumes and the Neo4j volume matter for backup; preserving only the graph loses other memory state.

Changing `NEO4J_PASSWORD` in `.env` does not reset an already initialized database's password. Change it in Neo4j first, then update `.env` to match. Do not delete the volume to fix a credential mismatch.

Images are pinned to multi-platform digests inspected on 2026-11-13 (AMD64 and ARM64). `pull` fetches those exact images, not a newer moving tag. Upgrade deliberately by reviewing upstream changes, backing up volumes, replacing digests in `compose.yaml`, and repeating the write/recall/restart check. Do not switch Cognee storage mode on existing volumes without a migration plan.

## Configuration self-check

From the repository root:

```sh
python3 infra/check_config.py
```

This uses dummy values, validates the Compose model and separation of services, and checks that missing secrets are rejected. It does not start containers or call a model. Runtime startup, ingestion, persistence, and agent connectivity still require the checks above with local credentials.
