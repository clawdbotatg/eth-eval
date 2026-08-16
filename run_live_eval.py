#!/usr/bin/env python3
"""eth-eval live/agentic track: can an AGENT do real Ethereum work?

Unlike run_eval.py (vanilla model, closed book), this track runs a tool-using
agent CLI (claude -p, codex, ...) against tasks whose answers live on mainnet
RIGHT NOW. Grading is execution-based with zero LLM judge: for every task the
harness computes the ground truth itself — via `cast` against the same RPC, at
grade time — and compares within a declared tolerance (prices drift, block
numbers advance; exact facts stay exact).

Requires: foundry's `cast` on PATH, RPC_URL env var (an authenticated
endpoint, e.g. Alchemy — set it in .env, never commit it).

Examples:
  RPC_URL=... python3 run_live_eval.py --self-test          # truth cmds resolve
  RPC_URL=... python3 run_live_eval.py --name claude-haiku \
      --cmd 'claude -p --model haiku'
"""
import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from run_eval import CmdTarget, ans_line, extract_bigints, norm

HERE = Path(__file__).resolve().parent
TASKS_DIR = HERE / "tasks-live"
RESULTS_DIR = HERE / "results-live"

PROMPT_PREFIX = (
    "You are an agent with shell access. Foundry's `cast` is installed and the "
    "environment variable RPC_URL holds an Ethereum mainnet RPC endpoint. Use "
    "any tools you need to answer with live data.\n\n"
)
PROMPT_SUFFIX = "\n\nEnd your reply with a line of the form \"Answer: <value>\"."


def load_env_file():
    p = HERE / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def truth_value(task):
    """Compute ground truth NOW via the task's shell command."""
    out = subprocess.run(task["truth"]["cmd"], shell=True, capture_output=True,
                        text=True, timeout=60, env=os.environ)
    if out.returncode != 0:
        raise RuntimeError(f"truth cmd failed: {out.stderr.strip()[:150]}")
    return out.stdout.strip().splitlines()[-1].strip()


def grade_live(task, resp, truth):
    t = task["truth"]["type"]
    a = ans_line(resp)
    if t == "exact":
        ok = norm(truth) in (norm(a), norm(resp.strip().splitlines()[-1] if resp.strip() else ""))
        return ok, f"truth {truth!r} got {a[:60]!r}"
    exp_nums = extract_bigints(truth)
    got_nums = extract_bigints(a) or extract_bigints(resp)
    if not exp_nums:
        return False, f"truth not numeric: {truth[:60]!r}"
    if not got_nums:
        return False, f"no number in answer {a[:60]!r}"
    exp, got = exp_nums[0], got_nums[0]
    if t == "abs":
        ok = abs(got - exp) <= task["truth"]["tol"]
    else:  # rel
        ok = exp != 0 and abs(got - exp) / abs(exp) <= task["truth"]["tol"]
    return ok, f"truth {exp} got {got}"


def load_tasks():
    tasks = []
    for f in sorted(TASKS_DIR.glob("*.jsonl")):
        for line in f.read_text().splitlines():
            if line.strip():
                tasks.append(json.loads(line))
    return tasks


def run_one(target, task):
    t0 = time.time()
    prompt = PROMPT_PREFIX + task["prompt"] + PROMPT_SUFFIX
    try:
        resp, _ = target.ask(prompt, 0)
        truth = truth_value(task)  # computed right after the agent answers
        ok, detail = grade_live(task, resp, truth)
        err = None
    except Exception as e:  # noqa: BLE001
        resp, ok, detail, err = "", False, f"ERROR: {str(e)[:150]}", True
    return {"id": task["id"], "category": task["category"], "pass": bool(ok),
            "detail": detail, "response": (resp or "")[:2000],
            "latency_s": round(time.time() - t0, 1)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name")
    ap.add_argument("--cmd", help="agent CLI; prompt on stdin, answer on stdout")
    ap.add_argument("--self-test", action="store_true", help="run every truth cmd, print values")
    ap.add_argument("--concurrency", type=int, default=2)
    args = ap.parse_args()

    load_env_file()
    if not os.environ.get("RPC_URL"):
        sys.exit("RPC_URL not set (put it in .env — an Alchemy URL, never a public RPC)")

    tasks = load_tasks()
    if args.self_test:
        bad = 0
        for t in tasks:
            try:
                v = truth_value(t)
                print(f"  ✓ {t['id']}: {v[:70]}")
            except Exception as e:  # noqa: BLE001
                print(f"  ✗ {t['id']}: {e}")
                bad += 1
        print(f"self-test: {len(tasks)-bad}/{len(tasks)} truth commands green")
        sys.exit(1 if bad else 0)

    if not (args.cmd and args.name):
        sys.exit("need --name and --cmd (or --self-test)")
    target = CmdTarget(args.cmd)
    target.env["RPC_URL"] = os.environ["RPC_URL"]

    print(f"running {len(tasks)} live tasks against {target.desc}")
    rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        for r in ex.map(lambda t: run_one(target, t), tasks):
            rows.append(r)
            print(f"  {'✓' if r['pass'] else '✗'} {r['id']} ({r['latency_s']}s) {r['detail'][:100]}")

    passed = sum(r["pass"] for r in rows)
    print(f"\n{passed}/{len(rows)} live tasks passed")
    RESULTS_DIR.mkdir(exist_ok=True)
    out = {"name": args.name, "target": target.desc,
           "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
           "passed": passed, "total": len(rows), "tasks": rows}
    (RESULTS_DIR / f"{args.name}.json").write_text(json.dumps(out, indent=1))
    print(f"saved results-live/{args.name}.json")


if __name__ == "__main__":
    main()
