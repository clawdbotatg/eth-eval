"""Minimal JSON-RPC client for the scenario harness (stdlib only)."""
import json
import urllib.request


def rpc(url, method, params=None, timeout=20):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                       "params": params or []}).encode()
    req = urllib.request.Request(url, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.load(resp)
    if "error" in data:
        raise RuntimeError(f"{method}: {data['error']}")
    return data["result"]


def hexint(v):
    """int from an RPC hex quantity (or passthrough int/None)."""
    if v is None or isinstance(v, int):
        return v
    return int(v, 16)
