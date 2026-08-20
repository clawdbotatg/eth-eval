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

## Integrity note — read this before trusting any number

**`--allowed-tools ""` does NOT disable tools in this Claude CLI.** Verified:
a run with that flag answered "what is the current Ethereum mainnet block
number" with a live, correct block, using Bash. Every score taken with it is a
*tool-using agent* score, not a closed-book one. Those result files are flagged
with a `warning` field.

What actually blocks tools:

    --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
    --disallowedTools Bash Read Write Edit Glob Grep Task Workflow Agent WebSearch WebFetch NotebookEdit

Tool names are **space-separated**; a comma-joined list is parsed as one bogus
name and silently denies nothing. MCP must be stripped separately or the agent
reaches a browser tool, and `Workflow`/`Agent` must be denied or it spawns a
subagent that still has Bash.

The runner now also gives the agent a **temp sandbox cwd** instead of the repo
root, so it cannot read `Grader.t.sol` or the reference answers.

## One run is a coin flip

Agents are stochastic. `lp-mint-01` with fable and no tools passed **2 of 5**
attempts — the same task, the same flags, failing three different ways
(malformed hex twice, a revert twice). Use `--runs N`; the saved result carries
`pass_rate` per task and `mean_pass_rate` overall. A single PASS means very
little.
