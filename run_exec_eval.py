#!/usr/bin/env python3
"""Execution-graded Ethereum eval.

Nothing here is string-matched against an answer key. The model's answer is
injected into a hidden Foundry test and run against a pinned mainnet fork —
the EVM decides whether it passed.

  python3 run_exec_eval.py --self-test
  python3 run_exec_eval.py --name opus-5 --cmd 'claude -p --model opus'
"""
import argparse, json, os, re, subprocess, sys, tempfile, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_eval import CmdTarget, OpenAITarget  # noqa: E402

HERE = Path(__file__).resolve().parent
EXEC = HERE / "exec"
TASKS = EXEC / "tasks"
RESULTS = HERE / "results-exec"

# The ONLY flag combination that actually disables tools in this Claude CLI.
# `--allowed-tools ""` does not. Tool names must be space-separated (a comma
# list parses as one bogus name), MCP has to be stripped separately or the agent
# reaches a browser tool, and Workflow/Agent must be denied or it spawns a
# subagent that still has Bash.
NOTOOLS_FLAGS = (
    "--strict-mcp-config --mcp-config '{\"mcpServers\":{}}' "
    "--disallowedTools Bash Read Write Edit Glob Grep Task Workflow Agent "
    "WebSearch WebFetch NotebookEdit"
)

STUB_SUBMISSION = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract _Stub {}
"""

def rpc_url():
    for line in (HERE / ".env").read_text().splitlines():
        if line.startswith("RPC_URL="):
            return line.split("=", 1)[1].strip()
    sys.exit("no RPC_URL in .env (Alchemy endpoint required)")

def load_tasks(only=None):
    out = []
    for d in sorted(TASKS.iterdir()):
        f = d / "task.json"
        if f.is_file():
            t = json.loads(f.read_text())
            t["dir"] = d
            if not only or t["id"] in only:
                out.append(t)
    return out

# ------------------------------------------------------------------ extraction

def strip_fences(s):
    """Pull the solidity out of a reply.

    Models sometimes emit an EMPTY ```solidity fence before the real code, so
    taking the first fenced block is not safe - take the first one that
    actually contains a pragma, and fall back to slicing the raw text.
    """
    for block in re.findall(r"```(?:solidity|sol)?\s*\n(.*?)```", s, re.S):
        if "pragma solidity" in block:
            return block.strip()
    body = re.sub(r"```(?:solidity|sol)?", "", s)
    i = body.find("// SPDX")
    if i < 0:
        i = body.find("pragma solidity")
    return (body[i:] if i >= 0 else body).strip()

def extract(kind, resp):
    """Pull the answer out of a model reply. Returns (payload, error)."""
    if kind == "calldata":
        m = re.search(r"0x[0-9a-fA-F]{8,}", resp)
        if not m:
            return None, "no 0x calldata found in reply"
        h = m.group(0)
        if len(h) % 2:
            return None, "odd-length calldata hex"
        return h, None
    if kind == "ticks":
        nums = re.findall(r"-?\d+", resp.replace(",", " , "))
        if len(nums) < 2:
            return None, "expected two integers"
        return (int(nums[0]), int(nums[1])), None
    if kind == "contract":
        src = strip_fences(resp)
        if "pragma solidity" not in src:
            return None, "reply is not a solidity source file"
        return src, None
    raise ValueError(kind)

def write_answer(kind, payload):
    calldata, lo, hi = "", 0, 0
    if kind == "calldata":
        calldata = payload[2:]
    elif kind == "ticks":
        lo, hi = payload
    (EXEC / "src" / "Answer.sol").write_text(
        "// SPDX-License-Identifier: MIT\n"
        "pragma solidity ^0.8.20;\n"
        "// GENERATED PER RUN by run_exec_eval.py\n"
        "library Answer {\n"
        f'    bytes  constant CALLDATA   = hex"{calldata}";\n'
        f"    int24  constant TICK_LOWER = {lo};\n"
        f"    int24  constant TICK_UPPER = {hi};\n"
        "}\n")
    (EXEC / "src" / "Submission.sol").write_text(
        payload if kind == "contract" else STUB_SUBMISSION)

# ------------------------------------------------------------------ grading

def forge_grade(task, timeout=420):
    env = {**os.environ,
           "FOUNDRY_TEST": f"tasks/{task['id']}",
           "FOUNDRY_PROFILE": "default"}
    p = subprocess.run(
        ["forge", "test", "--fork-url", rpc_url(),
         "--fork-block-number", str(task["fork_block"]), "-vv"],
        cwd=EXEC, capture_output=True, text=True, env=env, timeout=timeout)
    out = (p.stdout or "") + (p.stderr or "")
    if p.returncode == 0:
        return True, ""
    if "Compiler run failed" in out or "Error (" in out:
        m = re.search(r"Error \([0-9]+\):[^\n]*", out)
        return False, f"COMPILE: {m.group(0) if m else 'compile failed'}"[:220]
    fails = re.findall(r"\[FAIL:\s*([^\]]*)\]\s*(\S+)", out)
    if fails:
        return False, "; ".join(f"{fn}: {reason.strip()}" for reason, fn in fails[:3])[:220]
    m = re.search(r"(?:Error|error)[:\s][^\n]{5,180}", out)
    return False, (m.group(0) if m else out.strip().splitlines()[-1] if out.strip() else "forge failed")[:220]

def run_one(target, task, max_tokens, reference=None):
    t0 = time.time()
    if reference is not None:
        resp, usage, err = reference, {}, None
    else:
        try:
            resp, usage = target.ask(task["prompt"], max_tokens)
            err = None
        except Exception as e:  # noqa: BLE001
            resp, usage, err = "", {}, str(e)[:200]
    base = {"id": task["id"], "category": task["category"],
            "latency_s": round(time.time() - t0, 1), "usage": usage}
    if err:
        return {**base, "pass": False, "detail": f"TARGET ERROR: {err}", "response": ""}
    payload, perr = extract(task["answer"], resp)
    if perr:
        return {**base, "pass": False, "detail": f"FORMAT: {perr}", "response": resp}
    write_answer(task["answer"], payload)
    ok, detail = forge_grade(task)
    return {**base, "pass": ok, "detail": detail, "response": resp}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name")
    ap.add_argument("--cmd")
    ap.add_argument("--base-url"); ap.add_argument("--model")
    ap.add_argument("--api-key-env", default="OPENAI_API_KEY")
    ap.add_argument("--auth", choices=["bearer", "xapikey"], default="bearer")
    ap.add_argument("--task", action="append")
    ap.add_argument("--mode", choices=["notools", "tools"], default="notools",
                    help="notools = the model alone; tools = a full agent. "
                         "Both are real measurements - report them separately.")
    ap.add_argument("--runs", type=int, default=1,
                    help="attempts per task; an agent is stochastic, so 1 run is a coin flip")
    ap.add_argument("--self-test", action="store_true",
                    help="grade each task's reference answer (no model calls)")
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--timeout", type=int, default=2400,
                    help="per-task seconds; writing a fuzz-proof contract is slow")
    args = ap.parse_args()

    tasks = load_tasks(args.task)
    if not tasks:
        sys.exit("no exec tasks found")

    if args.self_test:
        good = 0
        for t in tasks:
            ref = (t["dir"] / "reference.txt")
            if not ref.is_file():
                # a task with no reference is an ungraded grader — never silently OK
                print(f"FAIL {t['id']}: no reference.txt to prove the grader")
                continue
            r = run_one(None, t, 0, reference=ref.read_text())
            print(f"{'PASS' if r['pass'] else 'FAIL'} {t['id']} {r['detail'][:150]}")
            good += r["pass"]
        print(f"\nself-test: {good}/{len(tasks)} references green")
        sys.exit(0 if good == len(tasks) else 1)

    if args.cmd:
        # sandbox: the agent has tools, so keep it out of the repo entirely
        sandbox = tempfile.mkdtemp(prefix="ethexec-")
        print(f"agent sandbox: {sandbox}")
        cmd = args.cmd
        if args.mode == "notools" and " --disallowedTools" not in cmd:
            cmd = cmd + " " + NOTOOLS_FLAGS
        target = CmdTarget(cmd, timeout=args.timeout, cwd=sandbox)
    elif args.base_url and args.model:
        target = OpenAITarget(args.base_url, args.model,
                              os.environ.get(args.api_key_env, ""), args.auth)
    else:
        sys.exit("need --self-test, --cmd, or --base-url + --model")
    if not args.name:
        sys.exit("--name required")

    print(f"running {len(tasks)} exec tasks x{args.runs} against {target.desc}")
    rows, t0 = [], time.time()
    for t in tasks:
        attempts = []
        for k in range(args.runs):
            r = run_one(target, t, args.max_tokens)
            attempts.append(r)
            tag = f" [{k+1}/{args.runs}]" if args.runs > 1 else ""
            print(f"  {'PASS' if r['pass'] else 'FAIL'} {r['id']}{tag} ({r['latency_s']}s) {r['detail'][:130]}")
        n_ok = sum(a["pass"] for a in attempts)
        best = next((a for a in attempts if a["pass"]), attempts[0])
        best = {**best, "attempts": len(attempts), "passed_attempts": n_ok,
                "pass_rate": round(n_ok / len(attempts), 2)}
        if args.runs > 1:
            print(f"    -> {r['id']}: {n_ok}/{args.runs} passed")
        rows.append(best)

    errs = [r["id"] for r in rows if r["detail"].startswith("TARGET ERROR")]
    if errs:
        # same rule as the closed-book runner: an outage is not a score
        sys.exit(f"refusing to save - never reached the target on: {', '.join(errs)}")

    RESULTS.mkdir(exist_ok=True)
    path = RESULTS / f"{args.name}.json"
    if args.task and path.is_file():          # merge a single-task re-run
        prev = json.loads(path.read_text())
        keep = [r for r in prev["tasks"] if r["id"] not in {x["id"] for x in rows}]
        rows = sorted(rows + keep, key=lambda r: r["id"])
    n = sum(r["pass"] for r in rows)
    rate = sum(r.get("pass_rate", 1.0 if r["pass"] else 0.0) for r in rows) / len(rows)
    print(f"\n{n}/{len(rows)} tasks passed at least once; "
          f"mean pass rate {rate*100:.0f}% ({time.time()-t0:.0f}s)")
    out = {"name": args.name, "target": target.desc, "track": "exec",
           "mode": args.mode,
           "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
           "passed": n, "total": len(rows),
           "overall": round(100 * n / len(rows), 1),
           "mean_pass_rate": round(100 * rate, 1), "runs": args.runs, "tasks": rows}
    path.write_text(json.dumps(out, indent=1))
    print(f"saved results-exec/{args.name}.json")

if __name__ == "__main__":
    main()
