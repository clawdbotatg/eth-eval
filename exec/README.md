# exec track — execution-graded Ethereum tasks

Nothing here is compared against an answer key. The model's answer is injected
into a hidden Foundry test and run against a **pinned mainnet fork**; the EVM
decides whether it passed.

    cd exec && forge install     # first time (forge-std)
    python3 ../run_exec_eval.py --self-test
    python3 ../run_exec_eval.py --name opus --cmd 'claude -p --model opus --allowed-tools ""'

## The five families

| task | asks for | graded by |
|---|---|---|
| `swap-calldata-01` | raw calldata for a 2 WETH → USDC swap | executing it, then asserting the **0.05% pool's** WETH balance rose by exactly 2 — output size alone cannot tell fee tiers apart |
| `permit2-calldata-01` | raw calldata for a Permit2 allowance | executing it, then reading `allowance()` back (catches the uint160/uint48 ABI trap) |
| `lp-range-01` | a tight Uniswap v3 tick range | tick-spacing alignment, brackets the live tick, ≥1% and ≤2.5% each side |
| `dca-contract-01` | a whole `DCA` contract | our hidden suite: real swap through SwapRouter02 + **both** owner-gates must revert |
| `fix-vault-01` | fix a share-inflation bug | an exploit test that must stop working, plus feature tests that must still pass |

## Rules for adding a task

1. **Every task needs a `reference.txt`** — a known-good answer. `--self-test`
   grades it and must be green, otherwise the grader is unproven.
2. **Prove the grader rejects too.** A grader only checked against a correct
   answer is worthless; the swap grader passed a *wrong fee tier* until the
   pool-balance assertion was added.
3. **Do not punish a different-but-valid solution.** The vault grader once
   failed a fix that blocks dust deposits — a legitimate mitigation. It now
   escalates the attacker's seed deposit instead of hardcoding 1 wei.
4. Pin `fork_block`. Ground truth is whatever the EVM says at that block.
