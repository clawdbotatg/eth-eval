#!/usr/bin/env python3
"""Reference solution — must score 100/100 on every seed (harness exit test).

Runs inside the agent workspace exactly like a real agent would: reads
params.json + wallet.key, queries the node, sends one EIP-1559 transfer via
cast, verifies the receipt, writes submission.json.
"""
import json
import subprocess
import sys


def cast(*args):
    p = subprocess.run(["cast", *args], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        sys.exit(f"cast {' '.join(args[:3])} failed: {p.stderr[:300]}")
    return p.stdout.strip()


def hx(v):
    return int(v, 16) if isinstance(v, str) and v.startswith("0x") else int(v)


def main():
    p = json.loads(open("params.json").read())
    key = open(p["key_file"]).read().strip()
    rpc, to, value = p["rpc_url"], p["recipient"], p["value_wei"]
    max_fee = p["max_fee_per_gas_wei"]
    sender = cast("wallet", "address", "--private-key", key)

    receipt = json.loads(cast(
        "send", "--rpc-url", rpc, "--private-key", key, to,
        "--value", str(value),
        "--gas-price", str(max_fee), "--priority-gas-price", str(10**9),
        "--json"))
    if hx(receipt["status"]) != 1:
        sys.exit("transfer reverted")

    tx_hash = receipt["transactionHash"]
    raw = json.loads(cast("rpc", "--rpc-url", rpc, "eth_getRawTransactionByHash", tx_hash))
    json.dump({
        "tx_hash": tx_hash,
        "raw_tx": raw,
        "from": sender,
        "to": to,
        "receipt_block": hx(receipt["blockNumber"]),
    }, open(p["submission_file"], "w"), indent=1)
    print(f"sent {tx_hash} in block {hx(receipt['blockNumber'])}")


if __name__ == "__main__":
    main()
