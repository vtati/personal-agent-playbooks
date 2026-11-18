"""Thin wrapper over your broker's trading MCP client (read tools only).

The MCP server returns {"content":[{"type":"text","text":"<json>"}]}; the inner
JSON carries a "data" object. call_tool returns that data dict (or the whole
inner object when there is no data key). Raises RuntimeError on failure —
callers decide whether a failure is fatal or a named gap.
"""
import json, os, pathlib, subprocess, tempfile

# Point this at YOUR broker MCP client CLI (see kit doc 04). Override with the
# BROKER_CLIENT_PATH environment variable.
CLIENT = pathlib.Path(os.environ.get("BROKER_CLIENT_PATH", "~/workspace/custom-connectors/custom.broker/bin/client.py")).expanduser()


def call_tool(name: str, args: dict, timeout: int = 120) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(args, f)
        args_path = f.name
    r = subprocess.run(
        ["python3", str(CLIENT), "call-tool", "--name", name, "--arguments-file", args_path],
        capture_output=True, text=True, timeout=timeout,
    )
    if r.returncode != 0:
        raise RuntimeError(f"{name} failed (exit {r.returncode}): {(r.stderr or r.stdout)[:400]}")
    outer = json.loads(r.stdout)
    text = outer["content"][0]["text"]
    inner = json.loads(text)
    if isinstance(inner, dict) and "error" in inner and inner["error"]:
        raise RuntimeError(f"{name} returned error: {str(inner['error'])[:400]}")
    return inner.get("data", inner) if isinstance(inner, dict) else inner


def batches(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]
