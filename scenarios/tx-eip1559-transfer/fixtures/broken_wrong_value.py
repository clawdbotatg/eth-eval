#!/usr/bin/env python3
"""Broken fixture: correct type-2 mechanics but transfers value-1 wei — an
off-by-one in amount handling. Envelope/signature/receipt milestones pass;
fields_correct and state_correct must fail."""
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
                          p["recipient"], "--value", str(p["value_wei"] - 1),
                          "--gas-price", str(p["max_fee_per_gas_wei"]),
                          "--priority-gas-price", str(10**9), "--json"))
tx_hash = receipt["transactionHash"]
raw = json.loads(cast("rpc", "--rpc-url", p["rpc_url"],
                      "eth_getRawTransactionByHash", tx_hash))
json.dump({"tx_hash": tx_hash, "raw_tx": raw, "from": sender,
           "to": p["recipient"], "receipt_block": hx(receipt["blockNumber"])},
          open(p["submission_file"], "w"))
print("sent wrong-value tx", tx_hash)
