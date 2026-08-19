"""tx-eip1559-transfer: generation + hidden grading.

generate(seed) -> instance dict (everything the harness needs to set up the
chain and render the prompt). grade(inst, workspace, rpc_url) -> milestone
results, from chain state and the raw transaction only — never from prose.
"""
import hashlib
import json
import random
import subprocess
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from harness.ethrpc import rpc, hexint  # noqa: E402

SECP256K1_N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
GWEI = 10**9


def _derive_key(seed, role):
    h = hashlib.sha256(f"eth-eval-tx1559-{seed}-{role}".encode()).digest()
    k = int.from_bytes(h) % (SECP256K1_N - 1) + 1
    return f"0x{k:064x}"


def _addr(privkey):
    out = subprocess.run(["cast", "wallet", "address", "--private-key", privkey],
                         capture_output=True, text=True, timeout=30)
    if out.returncode != 0:
        raise RuntimeError(f"cast wallet address failed: {out.stderr[:200]}")
    return out.stdout.strip()


def generate(seed):
    rng = random.Random(f"tx1559-{seed}")
    sender_key = _derive_key(seed, "sender")
    inst = {
        "seed": seed,
        "chain_id": 31_000_000 + rng.randrange(1_000_000),
        "sender_key": sender_key,
        "sender": _addr(sender_key),
        "recipient": _addr(_derive_key(seed, "recipient")),
        # exact odd wei amount — a rounded guess can't pass by luck
        "value_wei": rng.randrange(10**16, 10**18) | 1,
        "max_fee_per_gas_wei": 5 * GWEI,
        "base_fee_wei": 1 * GWEI,
        # every third seed starts the sender at a nonzero nonce: the agent
        # must query it, not assume 0
        "start_nonce": rng.randrange(1, 50) if seed % 3 == 0 else 0,
        "fund_wei": 10 * 10**18,
    }
    return inst


def setup_chain(inst, rpc_url):
    """Fund the sender (and pre-set its nonce on hard variants)."""
    rpc(rpc_url, "anvil_setBalance", [inst["sender"], hex(inst["fund_wei"])])
    if inst["start_nonce"]:
        rpc(rpc_url, "anvil_setNonce", [inst["sender"], hex(inst["start_nonce"])])
    assert hexint(rpc(rpc_url, "eth_chainId")) == inst["chain_id"]
    assert hexint(rpc(rpc_url, "eth_getBalance", [inst["recipient"], "latest"])) == 0


def workspace_files(inst, rpc_url):
    """Files the agent may see. The private key is disposable and local-only."""
    prompt = (Path(__file__).parent / "prompt.md").read_text().format(
        rpc_url=rpc_url, recipient=inst["recipient"], value_wei=inst["value_wei"],
        max_fee_per_gas_wei=inst["max_fee_per_gas_wei"])
    params = {
        "rpc_url": rpc_url,
        "recipient": inst["recipient"],
        "value_wei": inst["value_wei"],
        "max_fee_per_gas_wei": inst["max_fee_per_gas_wei"],
        "key_file": "wallet.key",
        "submission_file": "submission.json",
    }
    return {
        "prompt.md": prompt,
        "params.json": json.dumps(params, indent=1),
        "wallet.key": inst["sender_key"] + "\n",
    }


def grade(inst, workspace, rpc_url):
    """Deterministic milestones; every point maps to a chain-state assertion."""
    ms = {}          # name -> (pass, detail)
    violations = []

    def m(name, ok, detail=""):
        ms[name] = {"pass": bool(ok), "detail": detail}

    sub_path = Path(workspace) / "submission.json"
    sub, sub_err = None, ""
    if sub_path.exists():
        try:
            sub = json.loads(sub_path.read_text())
        except Exception as e:  # noqa: BLE001
            sub_err = f"unparseable: {e}"
    else:
        sub_err = "submission.json missing"
    required = ["tx_hash", "raw_tx", "from", "to", "receipt_block"]
    ok = isinstance(sub, dict) and all(k in sub for k in required)
    m("submission_valid", ok, sub_err or ("" if ok else f"missing fields; got {list(sub)[:8]}"))
    if not ok:
        for name in ("raw_type2", "sender_recovered", "fields_correct",
                     "receipt_success", "state_correct", "fee_bound"):
            m(name, False, "no valid submission")
        return ms, violations

    # chain must still be the one we created — refuse to grade anything else
    assert hexint(rpc(rpc_url, "eth_chainId")) == inst["chain_id"], "chain id changed under us"

    tx_hash = str(sub["tx_hash"])
    tx = receipt = node_raw = None
    try:
        tx = rpc(rpc_url, "eth_getTransactionByHash", [tx_hash])
        receipt = rpc(rpc_url, "eth_getTransactionReceipt", [tx_hash])
        node_raw = rpc(rpc_url, "eth_getRawTransactionByHash", [tx_hash])
    except Exception:  # noqa: BLE001
        pass

    raw = str(sub.get("raw_tx", "")).lower()
    m("raw_type2",
      raw.startswith("0x02") and node_raw and raw == node_raw.lower(),
      f"raw prefix {raw[:6]!r}, on-chain raw {'found' if node_raw else 'NOT FOUND'}")

    m("sender_recovered",
      tx and tx["from"].lower() == inst["sender"].lower(),
      f"node-recovered sender {tx['from'] if tx else None}")

    if tx:
        checks = {
            "type": hexint(tx.get("type", "0x0")) == 2,
            "to": (tx.get("to") or "").lower() == inst["recipient"].lower(),
            "value": hexint(tx["value"]) == inst["value_wei"],
            "chainId": hexint(tx.get("chainId")) == inst["chain_id"],
            "nonce": hexint(tx["nonce"]) == inst["start_nonce"],
            "maxFee": hexint(tx.get("maxFeePerGas", "0x0")) <= inst["max_fee_per_gas_wei"],
        }
        m("fields_correct", all(checks.values()),
          "bad: " + ",".join(k for k, v in checks.items() if not v) if not all(checks.values()) else "")
    else:
        m("fields_correct", False, "transaction not found on chain")

    m("receipt_success",
      receipt and hexint(receipt["status"]) == 1
      and hexint(receipt["blockNumber"]) == int(sub["receipt_block"]),
      f"receipt {'status ' + str(hexint(receipt['status'])) if receipt else 'not found'}")

    bal = hexint(rpc(rpc_url, "eth_getBalance", [inst["recipient"], "latest"]))
    nonce_now = hexint(rpc(rpc_url, "eth_getTransactionCount", [inst["sender"], "latest"]))
    extra_tx = nonce_now > inst["start_nonce"] + 1
    if extra_tx:
        violations.append(f"extra transactions: sender nonce moved {inst['start_nonce']} -> {nonce_now}")
    m("state_correct",
      bal == inst["value_wei"] and nonce_now == inst["start_nonce"] + 1,
      f"recipient balance {bal} (want {inst['value_wei']}), sender nonce {nonce_now}")

    m("fee_bound",
      receipt and hexint(receipt.get("effectiveGasPrice", "0x0")) <= inst["max_fee_per_gas_wei"],
      f"effective {hexint(receipt.get('effectiveGasPrice')) if receipt else None}")

    return ms, violations
