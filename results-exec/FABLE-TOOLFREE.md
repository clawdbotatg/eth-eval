# fable, tool-free, exec track

Flags (the only combination that actually blocks tools — see exec/README.md):

    claude -p --model fable \
      --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
      --disallowedTools Bash Read Write Edit Glob Grep Task Workflow Agent \
                        WebSearch WebFetch NotebookEdit

| task | passed | note |
|---|---|---|
| lp-rebalance-01 | **1/3** | both failures near-miss: 16% and 19% undeployed vs a 10% bar |
| lp-mint-01 | **3/8** | 1/3 here + 2/5 in a separate 5-run measurement |
| swap-slippage-01 | **2/3** | |
| dca-contract-01 | 3/3 | |
| fix-vault-01 | 3/3 | |
| lp-range-01 | 3/3 | |
| permit2-calldata-01 | 3/3 | |
| swap-calldata-01 | 3/3 | |
| vault-fuzz-01 | 3/3 | an earlier 0/3 was a rate limit, not a failure — re-run on another account |

Mean pass rate ≈ **87%**. Only `lp-mint-01` is genuinely hard tool-free (38%),
with `swap-slippage-01` partially hard (67%). The other six are solved.

With Bash available, fable passes `lp-mint-01` by shelling out to Python to
compute `getSqrtRatioAtTick` and the liquidity math — it does not know it, it
calculates it. That gap is what the track is for.

**Still too easy.** Six of eight tasks are saturated. The next tasks should be
lp-mint-class: multi-step, arithmetic that cannot be recalled, and a state
assertion that only a correct computation satisfies.


## The gap that matters: tools vs no tools

Same task, same model, 3 runs each.

| task | fable no-tools | fable with tools |
|---|---|---|
| `lp-rebalance-01` | **1/3** | **3/3** |
| `lp-mint-01` | 3/8 | passes (shells out to Python for `getSqrtRatioAtTick`) |

The tool-free failures are near misses, not confusion — fable knows it must
rebalance, it just cannot land the ratio without computing it. That is exactly
the shape a skills doc should close.
