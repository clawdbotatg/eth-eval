#!/usr/bin/env python3
"""Broken fixture: sends a LEGACY (type-0) transaction instead of the required
type-2. The transfer itself lands, so receipt/state milestones pass — the
type milestones must fail. Demonstrates partial credit."""
import json
import subprocess


def cast(*args):
    p = subprocess.run(["cast", *args], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise SystemExit(p.stderr[:300])
    return p.stdout.strip()


def hx(v):
    return int(v, 16) if isinstance(v, str) and v.startswith("0x") else int(v)


p = json.loads(open("params.json").read())
key = open(p["key_file"]).read().strip()
sender = cast("wallet", "address", "--private-key", key)
receipt = json.loads(cast("send", "--rpc-url", p["rpc_url"], "--private-key", key,
                          p["recipient"], "--value", str(p["value_wei"]),
                          "--legacy", "--gas-price", str(2 * 10**9), "--json"))
tx_hash = receipt["transactionHash"]
raw = json.loads(cast("rpc", "--rpc-url", p["rpc_url"],
                      "eth_getRawTransactionByHash", tx_hash))
json.dump({"tx_hash": tx_hash, "raw_tx": raw, "from": sender,
           "to": p["recipient"], "receipt_block": hx(receipt["blockNumber"])},
          open(p["submission_file"], "w"))
print("sent legacy tx", tx_hash)
