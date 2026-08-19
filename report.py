#!/usr/bin/env python3
"""Leaderboard + ethskills-coverage report from results/*.json.

Usage: python3 report.py [--md]
"""
import argparse
import json
from pathlib import Path

from run_eval import BENCH_VERSION, load_tasks, manifest_hash

HERE = Path(__file__).resolve().parent

def task_kinds():
    """id -> kind for every task on disk. Generated tasks count as facts."""
    kinds = {}
    for p in (HERE / "tasks").glob("*.jsonl"):
        for line in p.read_text().splitlines():
            if line.strip():
                t = json.loads(line)
                kinds[t["id"]] = t.get("kind", "fact")
    return kinds

def split_scores(run, kinds):
    """(fact-only overall via per-category mean, recommendation adherence pct).

    Recommendation tasks grade agreement with ethskills' opinions, not truth —
    a model can be right and disagree — so they get their own number instead
    of silently blending into the headline.
    """
    bycat, rec = {}, []
    for row in run.get("tasks", []):
        kind = kinds.get(row["id"])
        if kind == "recommendation":
            rec.append(row["pass"])
        elif kind is not None:
            bycat.setdefault(row["category"], []).append(row["pass"])
    fact = round(100 * sum(sum(v) / len(v) for v in bycat.values()) / len(bycat), 1) if bycat else "-"
    rec_pct = round(100 * sum(rec) / len(rec), 1) if rec else "-"
    return fact, rec_pct

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true", help="emit GitHub-flavored markdown")
    args = ap.parse_args()

    all_runs = []
    for p in sorted((HERE / "results").glob("*.json")):
        all_runs.append(json.loads(p.read_text()))
    if not all_runs:
        raise SystemExit("no results yet — run run_eval.py first")

    # results are only comparable within one benchmark manifest (same tasks,
    # prompts, graders). Rank only runs matching the CURRENT on-disk manifest;
    # everything else — older task sets, pre-manifest runs, subsets — is
    # listed as legacy, never ranked alongside.
    current = manifest_hash(load_tasks())
    runs, legacy = [], []
    for r in all_runs:
        b = r.get("benchmark", {})
        if b.get("manifest_sha256") == current and not b.get("subset"):
            runs.append(r)
        else:
            legacy.append(r)
    runs.sort(key=lambda r: -r["overall"])
    legacy.sort(key=lambda r: -r["overall"])

    cats = sorted({c for r in runs for c in r["categories"]})

    def table(headers, rows):
        if args.md:
            out = ["| " + " | ".join(headers) + " |",
                   "|" + "|".join("---" for _ in headers) + "|"]
            out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
            return "\n".join(out)
        w = [max(len(str(x)) for x in [h] + [row[i] for row in rows]) for i, h in enumerate(headers)]
        out = ["  ".join(str(h).ljust(w[i]) for i, h in enumerate(headers))]
        out += ["  ".join(str(c).ljust(w[i]) for i, c in enumerate(row)) for row in rows]
        return "\n".join(out)

    kinds = task_kinds()
    hdr = (f"## Leaderboard (manifest {current[:12]}, v{BENCH_VERSION}, "
           "per-category mean, pass@1, temp 0)\n")
    print(hdr if args.md else hdr.replace("## ", "").upper())
    if runs:
        rows = []
        for r in runs:
            fact, rec = split_scores(r, kinds)
            rows.append([r["name"], r["overall"], fact, rec, f"{r['ci95'][0]}-{r['ci95'][1]}",
                         len(r.get("tasks", []))] +
                        [r["categories"].get(c, {}).get("pct", "-") for c in cats])
        print(table(["model", "overall", "facts", "rec-adh", "95% CI", "tasks"] + cats, rows))
        if not args.md:
            print("\n'facts' = objective tasks only; 'rec-adh' = agreement with ethskills' "
                  "opinionated recommendations (a model can be right and disagree — judge separately).")
    else:
        print("(no runs on the current manifest yet — every saved result predates "
              "the current task set or grader version and cannot be ranked against it)")

    if legacy:
        print("\n\n## Legacy runs (incompatible manifests — NOT comparable to the "
              "leaderboard or to each other)\n" if args.md else
              "\nLEGACY RUNS (incompatible manifests — NOT comparable to the leaderboard or each other)\n")
        rows = []
        for r in legacy:
            b = r.get("benchmark", {})
            why = ("subset" if b.get("subset") else
                   b.get("manifest_sha256", "")[:12] or "pre-manifest")
            rows.append([r["name"], r["overall"], len(r.get("tasks", [])),
                         r.get("timestamp", "")[:10], why])
        print(table(["model", "overall", "tasks", "date", "manifest"], rows))

    if not runs:
        cov_runs = legacy
        note = " — STALE: computed from legacy runs, refresh with new runs"
    else:
        cov_runs = runs
        note = ""
    skills = sorted({s for r in cov_runs for s in r.get("skills", {}) if s and s != "generated"})
    print(f"\n\n## ethskills coverage (per source skill — high everywhere = candidate to trim{note})\n"
          if args.md else f"\nETHSKILLS COVERAGE (per source skill — high everywhere = candidate to trim{note})\n")
    rows = []
    for s in skills:
        row = [s]
        pcts = []
        for r in cov_runs:
            pct = r.get("skills", {}).get(s, {}).get("pct")
            row.append(pct if pct is not None else "-")
            if pct is not None:
                pcts.append(pct)
        row.append(round(min(pcts), 1) if pcts else "-")
        rows.append(row)
    rows.sort(key=lambda x: -(x[-1] if isinstance(x[-1], (int, float)) else -1))
    print(table(["skill"] + [r["name"] for r in cov_runs] + ["min"], rows))
    if not args.md:
        print("\n'min' = worst model's score on that skill. A skill every model aces "
              "is knowledge the models already have; a low min is what ethskills is for.")

if __name__ == "__main__":
    main()
