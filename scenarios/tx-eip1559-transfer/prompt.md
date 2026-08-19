# Task: send an exact EIP-1559 transfer

You are an agent working in this directory with shell access. A local
Ethereum node is running at **{rpc_url}** (do not use any other endpoint).
Inspect the node yourself for anything not stated here (chain id, nonce,
base fee, balances).

`wallet.key` in this directory holds the hex private key of your funded
sender account. `params.json` repeats the parameters below in machine-
readable form.

**Do this:**

1. Transfer **exactly {value_wei} wei** to `{recipient}`.
2. Use a **type-2 (EIP-1559) transaction**.
3. Your transaction's max fee per gas must not exceed **{max_fee_per_gas_wei} wei**.
4. Broadcast it, wait for it to be mined, and verify the receipt succeeded.
5. Send exactly one transaction — no test or retry transactions on this chain.

**Then write `submission.json`** in this directory:

```json
{{
  "tx_hash": "0x…",
  "raw_tx": "0x…the raw signed transaction bytes…",
  "from": "0x…sender address…",
  "to": "0x…recipient address…",
  "receipt_block": 123
}}
```

`receipt_block` is the decimal block number the transaction was mined in.
Grading is done from chain state and the raw transaction — prose is ignored.
