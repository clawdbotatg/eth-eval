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
| `swap-slippage-01` | calldata with a REAL slippage guard | run twice: clean (must fill) and after an adversary moves the price 4% (must revert) — `amountOutMinimum=0` passes the first and fails the second |
| `vault-fuzz-01` | a yield-bearing ERC-4626-style vault | a **fuzz campaign**: yield accrues pro-rata, late depositors don't dilute, no round-trip profit, solvent on exit, inflation attack dead |

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
5. **Grade only what the prompt asked for.** The fuzz grader called
   `totalShares()`, a getter the task never required, and failed a correct
   contract for not having it.
6. **Measure before setting a threshold.** The first draft of the routing task
   assumed splitting across pools beats one pool. Measured at the pinned block,
   500 WETH through the single 0.05% pool returns 948,849 USDC and a 50/50
   split returns 939,998 — splitting is *worse*. The task was rewritten around
   slippage guards instead.
7. **A mutant that still satisfies the spec is not a grader bug.** Two "wrong"
   vault variants were accepted; tracing them showed floor-then-ceil returns
   exactly the deposit, so the rounding never leaks. The spec defines
   correctness, and a vault with no yield makes share math irrelevant — which
   is why `vault-fuzz-01` requires yield.

## Integrity note

`CmdTarget` runs the model with `cwd` = the repo root. With tools disabled
(`--allowed-tools ""`) that is fine, and it is how every run here was scored.
A **tool-enabled** agent, though, could read `Grader.t.sol` or write to it —
two stray `.sol` files did land in the repo root during development. Before
running this track against an agent that has file access, sandbox it or move
the graders out of its reach; otherwise the score measures nothing.
