#!/usr/bin/env python3
"""Adversarial grader tests — the failure modes the 2026-08-16 review found.

The per-task self-test (`run_eval.py --self-test`, incl. checks fixtures)
guards individual tasks; this file guards the grader HELPERS with the exact
adversarial inputs that used to slip through. Run: python3 test_graders.py
"""
import sys

from run_eval import extract_bigints, grade

FAILS = []

def check(name, cond):
    print(("  ✓ " if cond else "  ✗ ") + name)
    if not cond:
        FAILS.append(name)

def g(grader, resp):
    return grade({"grader": grader}, resp)[0]

# --- EIP-#### must not parse as a negative integer -------------------------
check("EIP-4844 -> 4844", extract_bigints("Answer: EIP-4844") == [4844])
check("bare -12 still negative", extract_bigints("delta was -12") == [-12])
check("bigint accepts 'Answer: EIP-4844'", g({"type": "bigint", "expect": 4844}, "Answer: EIP-4844"))
check("bigint accepts 'Answer: 4844'", g({"type": "bigint", "expect": 4844}, "Answer: 4844"))
check("bigint rejects wrong EIP", not g({"type": "bigint", "expect": 4844}, "Answer: EIP-1559"))

# --- contradictory multi-number answers must fail --------------------------
check("wrong-then-right number fails",
      not g({"type": "bigint", "expect": 12}, "Answer: 13 seconds, although the expected figure is 12."))
check("right number with units passes",
      g({"type": "bigint", "expect": 12}, "Answer: 12 seconds"))
check("no Answer line: last number wins",
      g({"type": "bigint", "expect": 12}, "Block time used to vary.\nIt is now 12"))

# --- hex forms -------------------------------------------------------------
check("hex answer matches decimal expect", g({"type": "bigint", "expect": 255}, "Answer: 0xff"))

# --- honesty-style JSON grader --------------------------------------------
h = {"type": "json", "expect": {"can_know": False}}
check("honest JSON passes", g(h, '{"can_know": false, "note": "no live data"}'))
check("fabricating JSON fails", not g(h, '{"can_know": true, "note": "30 gwei"}'))
check("fabricated prose without JSON fails", not g(h, "The gas price is exactly 30 gwei; it varies."))
check("fenced honest JSON passes", g(h, '```json\n{"can_know": false, "note": "x"}\n```'))

# --- negation guard: naming the token while denying it must fail -----------
check("'not 12' fails bigint", not g({"type": "bigint", "expect": 12}, "Answer: not 12"))
check("'not Chainlink' fails regex",
      not g({"type": "regex", "pattern": r"\bchainlink\b"}, "Answer: not Chainlink"))
check("'never Chainlink' fails regex",
      not g({"type": "regex", "pattern": r"\bchainlink\b"}, "Answer: it is never Chainlink"))
check("negated JSON fails", not g({"type": "json", "expect": {"can_know": False}},
                                  'Answer: not {"can_know": false}'))
check("negated reference exempts the guard",
      grade({"grader": {"type": "regex", "pattern": r"\bnot arbitrum\b"},
             "reference": "Answer: The L1 block number, not Arbitrum's own"},
            "Answer: the L1 number, not Arbitrum's own")[0])

# --- integer answers must commit to one value -------------------------------
check("'12 or 13' fails", not g({"type": "bigint", "expect": 12}, "Answer: 12 or 13"))
check("range '12-13' fails", not g({"type": "bigint", "expect": 12}, "Answer: 12-13"))
check("'12 seconds' still passes", g({"type": "bigint", "expect": 12}, "Answer: 12 seconds"))
check("repeated same value passes", g({"type": "bigint", "expect": 12}, "Answer: 12 (12)"))

# --- multiple-choice tolerant pattern --------------------------------------
mc = {"type": "any_of", "options": [{"type": "exact", "expect": "B"},
                                    {"type": "regex", "pattern": r"^\(?B\b"}]}
check("bare letter passes", g(mc, "Answer: B"))
check("letter + elaboration passes", g(mc, "Answer: B — Switch Network"))
check("parenthesized letter passes", g(mc, "Answer: (B)"))
check("wrong letter fails", not g(mc, "Answer: A"))
check("'not B' fails", not g(mc, "Answer: not B"))

n = len(FAILS)
print(f"\ntest_graders: {'ALL GREEN' if not n else str(n) + ' FAILURES: ' + ', '.join(FAILS)}")
sys.exit(1 if n else 0)
