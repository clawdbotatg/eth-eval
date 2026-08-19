#!/usr/bin/env python3
"""Broken fixture: constructs and signs a valid transaction but NEVER
broadcasts it — the classic calldata-only / "here is the transaction object"
failure. Must fail raw_type2, receipt_success, and state_correct."""
import json
import subprocess


def cast(*args):
    return subprocess.run(["cast", *args], capture_output=True, text=True,
                          timeout=60).stdout.strip()


p = json.loads(open("params.json").read())
key = open(p["key_file"]).read().strip()
sender = cast("wallet", "address", "--private-key", key)
raw = cast("mktx", "--rpc-url", p["rpc_url"], "--private-key", key,
           p["recipient"], "--value", str(p["value_wei"]),
           "--gas-price", str(p["max_fee_per_gas_wei"]),
           "--priority-gas-price", str(10**9))
tx_hash = cast("keccak", raw)
json.dump({"tx_hash": tx_hash, "raw_tx": raw, "from": sender,
           "to": p["recipient"], "receipt_block": 1},
          open(p["submission_file"], "w"))
print("built but did not broadcast", tx_hash)
