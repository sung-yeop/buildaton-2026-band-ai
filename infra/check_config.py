"""Validate local infrastructure configuration without credentials or a daemon."""

import json
import os
from pathlib import Path
import subprocess
import tempfile


compose = Path(__file__).with_name("compose.yaml")
env = {key: value for key, value in os.environ.items()
       if key not in {"LLM_API_KEY", "LLM_MODEL", "NEO4J_PASSWORD"}}
with tempfile.TemporaryDirectory() as directory:
    env_file = Path(directory) / ".env"
    env_file.write_text("")
    command = ["docker", "compose", "--env-file", str(env_file),
               "-f", str(compose), "config", "--format", "json"]
    env.update(LLM_API_KEY="config-check-only", LLM_MODEL="config-check-only",
               NEO4J_PASSWORD="config-check-only")
    for required in ("LLM_API_KEY", "LLM_MODEL", "NEO4J_PASSWORD"):
        incomplete = dict(env)
        incomplete.pop(required)
        missing = subprocess.run(command, env=incomplete, capture_output=True, text=True)
        assert missing.returncode != 0 and required in missing.stderr, missing.stderr
    result = subprocess.run(command, env=env, capture_output=True, text=True, check=True)
    config = json.loads(result.stdout)

services = config["services"]
assert set(services) == {"cognee", "neo4j"}
cognee, neo4j = services["cognee"], services["neo4j"]
assert cognee["environment"]["GRAPH_DATABASE_PROVIDER"] == "ladybug"
assert "GRAPH_DATABASE_URL" not in cognee["environment"]
assert cognee["environment"]["COGNEE_MCP_AGENT_SCOPED"] == "false"
assert set(cognee["networks"]).isdisjoint(neo4j["networks"])
assert {v["source"] for v in cognee["volumes"]}.isdisjoint(
    v["source"] for v in neo4j["volumes"])
assert {v["target"] for v in cognee["volumes"]} == {
    "/cognee-storage/system", "/cognee-storage/data"}
assert {v["target"] for v in neo4j["volumes"]} == {"/data"}
for service in services.values():
    assert "@sha256:" in service["image"]
    assert not service.get("depends_on")
    assert service["healthcheck"]["test"]
    assert all(port["host_ip"] == "127.0.0.1" for port in service["ports"])
    assert all(volume["type"] == "volume" for volume in service["volumes"])
print("PASS: required secrets, pinned images, loopback ports, independent networks and persistent volumes")
