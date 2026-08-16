# eth-eval

**How much Ethereum does an LLM actually know?**

An evaluation suite that interrogates a vanilla LLM — no docs, no tools, no
retrieval — on the working knowledge an Ethereum builder needs: the same
knowledge [ethskills.com](https://ethskills.com) packages for AI agents.

Two questions it answers:

1. **Which model knows Ethereum best?** A leaderboard across 243 closed-book
   tasks in 23 categories: wallets, standards, security, testing, tooling, gas,
   calldata, derivations, L2s, frontend, indexing, protocol, concepts,
   addresses, fundamentals, units — plus CROPS (censorship resistance / open
   source / privacy / security), MEV, cryptoeconomics (walkaway-test
   scenarios), cypherpunk ideals, fork roadmap (date-tagged), contract-reading
   (full Solidity source in the prompt), and honesty (live-data questions where
   the only right closed-book answer is "I can't know that").
2. **What can ethskills stop teaching?** Every knowledge task is keyed to a
   specific ethskills SKILL.md claim. When every frontier model aces a skill's
   tasks, that content is already in the models and is a candidate for
   trimming. The endgame: the models know everything and ethskills retires.

## Design: where the answers come from (not the authoring LLM)

An LLM helped author this eval, which is a bias risk — an LLM writing questions
from its own knowledge would build an eval of *what LLMs already know*. Two
defenses:

- **Computational tasks (`gen/`)** — ground truth is *computed*, never authored:
  function selectors, ABI calldata, event topics, CREATE/CREATE2 addresses,
  EIP-55 checksums and storage slots come from foundry's `cast`; EIP-1559
  base-fee steps and intrinsic-gas sums are integer math from the spec pseudocode
  (sanity-asserted against known vectors, e.g. EIP-1014's CREATE2 test vector).
  Instances are randomized from a seed — regenerate per release
  (`python3 gen/generate_tasks.py --seed <new>`), so there is nothing to memorize.
- **Knowledge tasks (`tasks/skill-*.jsonl`)** — the answer key is the ethskills
  file's claim, not the author's opinion. Every task carries a `source_quote`
  field with the verbatim SKILL.md line it grades against, and a `source` field
  naming the skill, so per-skill coverage is reportable and every answer is
  auditable against the corpus.

Residual bias disclosed: question *selection* still passed through an LLM, and
pure-recall items are trained-on by definition (tagged and accepted).

Grading is 100% deterministic (exact / regex / JSON-shape / bigint) — there is
no LLM judge. `--self-test` grades every task's bundled reference answer and
must be 100% before any run counts.

## Run it

```bash
python3 run_eval.py --self-test                       # graders green? (zero tokens)

# any OpenAI-compatible endpoint:
python3 run_eval.py --name gpt-5.6 --base-url https://llm.bankr.bot/v1 \
    --model gpt-5.6-sol --api-key-env BANKR_API_KEY --auth xapikey

# any CLI harness (prompt on stdin, answer on stdout):
python3 run_eval.py --name haiku --cmd 'claude -p --model haiku' --concurrency 4

python3 report.py          # leaderboard + per-skill ethskills coverage
python3 report.py --md     # markdown tables
```

Protocol: temperature 0, pass@1, no retries, deterministic graders, bootstrap
95% CI over categories. Stdlib-only Python; `cast` (foundry) needed only to
*regenerate* tasks, not to run them.

## Task format

One JSON object per line in `tasks/*.jsonl`:

```json
{"id": "gas-k-03", "category": "gas", "source": "gas", "kind": "fact",
 "prompt": "...question ending with an answer-format instruction...",
 "grader": {"type": "regex", "pattern": "burn(ed|t)?"},
 "reference": "Answer: it is burned",
 "source_quote": "The base fee is burned, not paid to validators."}
```

`kind: "recommendation"` marks ethskills' opinionated guidance (which tool,
which pattern) vs objective `fact`s — reports can split them.

See `tasks/AUTHORING.md` for the authoring rules and grader semantics.

## Live / agentic track

`run_live_eval.py` + `tasks-live/` test whether a tool-using AGENT (claude -p,
codex, …) can do real Ethereum work right now: current block/gas/ETH price,
a Uniswap pool's live liquidity, a proxy's implementation slot, building exact
transfer calldata with correct decimals. No LLM judge: the harness computes
ground truth itself via `cast` against the same RPC at grade time, and
compares within a declared tolerance. Needs `RPC_URL` in a gitignored `.env`
(Alchemy — never a public RPC).

```bash
python3 run_live_eval.py --self-test                        # truth cmds resolve
python3 run_live_eval.py --name haiku --cmd 'claude -p --model haiku'
```

## Roadmap

- **Track 2 — execution**: model writes the `cast` command / viem script; we run
  it against a forked chain and check state.
- **Track 3 — agent harnesses**: Claude Code / Codex on real scaffold-eth +
  foundry tasks, plus a with-ethskills vs without A/B — does the skill close the
  gap for weaker models? (That finding is the whole ballgame for ethskills.)
