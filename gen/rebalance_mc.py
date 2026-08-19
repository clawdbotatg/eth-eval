#!/usr/bin/env python3
"""Rebalance multiple-choice answer positions across the closed-book corpus.

The 2026-08 review found 28 of 39 MC answers sat on B — blind-B scored ~72%
on that slice. This script deterministically (seed 2026) reassigns correct
option positions to a near-uniform spread, swapping option TEXT between the
old and new letters and updating grader, reference, and checks fixtures to
match. Letter regexes are canonicalized to `^\\(?X\\b` on the answer line
(any semantic alternation tail is preserved).

Idempotent-ish: rerunning reshuffles again; run once, verify with
`run_eval.py --self-test`, commit.
"""
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TASKS = HERE / "tasks"
LETTERS = "ABCD"
OPT_RE = re.compile(r"^([A-D])\)\s?(.*)$", re.M)


def is_mc(t):
    return len(OPT_RE.findall(t["prompt"])) == 4


def current_letter(t):
    g = t["grader"]
    opts = g["options"] if g["type"] == "any_of" else [g]
    for o in opts:
        if o["type"] == "exact" and o["expect"].upper() in LETTERS and len(o["expect"]) == 1:
            return o["expect"].upper()
    # letter-only regex forms: ^\(?B\b, ^b\b, \bB\b, answer:\s*C\b
    for o in opts:
        if o["type"] == "regex":
            m = re.search(r"([A-D])\\b", o["pattern"], re.I)
            if m:
                return m.group(1).upper()
    raise ValueError(f"{t['id']}: cannot determine correct letter")


def retarget_pattern(pat, tgt):
    """Replace the letter alternative with a canonical anchored form; keep any
    semantic alternation tail (e.g. '|under\\s*1\\s*gwei')."""
    parts = pat.split("|")
    head = f"^\\(?{tgt}\\b"
    if re.fullmatch(r"answer:\\s\*[A-D]\\b", parts[0], re.I):
        head = f"answer:\\s*{tgt}\\b"
    return "|".join([head] + parts[1:])


def map_letters(s, perm):
    return re.sub(r"\b([A-D])\b", lambda m: perm[m.group(1)], s)


def rewrite(t, tgt):
    cur = current_letter(t)
    perm = {L: L for L in LETTERS}
    perm[cur], perm[tgt] = tgt, cur

    opts = dict(OPT_RE.findall(t["prompt"]))
    def sub_opt(m):
        return f"{m.group(1)}) {opts[perm_inv[m.group(1)]]}"
    # perm is a swap, so it is its own inverse
    perm_inv = perm
    t["prompt"] = OPT_RE.sub(sub_opt, t["prompt"])

    g = t["grader"]
    for o in (g["options"] if g["type"] == "any_of" else [g]):
        if o["type"] == "exact" and o["expect"].upper() == cur:
            o["expect"] = tgt
        elif o["type"] == "regex" and re.search(rf"{cur}\\b", o["pattern"], re.I):
            o["pattern"] = retarget_pattern(o["pattern"], tgt)

    t["reference"] = map_letters(t["reference"], perm)
    for key in ("must_pass", "must_fail"):
        if key in t.get("checks", {}):
            t["checks"][key] = [map_letters(s, perm) for s in t["checks"][key]]
    return t


def main():
    files = sorted(TASKS.glob("*.jsonl"))
    all_tasks = []  # (file, line_no, task or raw)
    for f in files:
        for i, line in enumerate(f.read_text().splitlines()):
            all_tasks.append([f, i, json.loads(line) if line.strip() else None, line])

    mc = [row for row in all_tasks if row[2] and is_mc(row[2])]
    mc.sort(key=lambda r: r[2]["id"])
    n = len(mc)
    pool = [LETTERS[i % 4] for i in range(n)]
    random.Random(2026).shuffle(pool)

    from collections import Counter
    before = Counter(current_letter(r[2]) for r in mc)
    for row, tgt in zip(mc, pool):
        row[2] = rewrite(row[2], tgt)
        row[3] = json.dumps(row[2], ensure_ascii=False)
    after = Counter(current_letter(r[2]) for r in mc)
    print(f"{n} MC tasks: {dict(before)} -> {dict(after)}")

    touched = {row[0] for row in mc}
    byfile = {}
    for f, i, _, line in all_tasks:
        byfile.setdefault(f, []).append(line)
    for f in touched:
        f.write_text("\n".join(byfile[f]) + "\n")
    print(f"rewrote {len(touched)} files")


if __name__ == "__main__":
    sys.exit(main())
