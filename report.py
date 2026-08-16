#!/usr/bin/env python3
"""Leaderboard + ethskills-coverage report from results/*.json.

Usage: python3 report.py [--md]
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true", help="emit GitHub-flavored markdown")
    args = ap.parse_args()

    runs = []
    for p in sorted((HERE / "results").glob("*.json")):
        runs.append(json.loads(p.read_text()))
    if not runs:
        raise SystemExit("no results yet — run run_eval.py first")
    runs.sort(key=lambda r: -r["overall"])

    cats = sorted({c for r in runs for c in r["categories"]})
    skills = sorted({s for r in runs for s in r.get("skills", {}) if s and s != "generated"})

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

    print("## Leaderboard (per-category mean, pass@1, temperature 0)\n" if args.md else
          "LEADERBOARD (per-category mean, pass@1, temp 0)\n")
    rows = [[r["name"], r["overall"], f"{r['ci95'][0]}-{r['ci95'][1]}"] +
            [r["categories"].get(c, {}).get("pct", "-") for c in cats] for r in runs]
    print(table(["model", "overall", "95% CI"] + cats, rows))

    print("\n\n## ethskills coverage (per source skill — high everywhere = candidate to trim)\n"
          if args.md else "\nETHSKILLS COVERAGE (per source skill — high everywhere = candidate to trim)\n")
    rows = []
    for s in skills:
        row = [s]
        pcts = []
        for r in runs:
            pct = r.get("skills", {}).get(s, {}).get("pct")
            row.append(pct if pct is not None else "-")
            if pct is not None:
                pcts.append(pct)
        row.append(round(min(pcts), 1) if pcts else "-")
        rows.append(row)
    rows.sort(key=lambda x: -(x[-1] if isinstance(x[-1], (int, float)) else -1))
    print(table(["skill"] + [r["name"] for r in runs] + ["min"], rows))
    if not args.md:
        print("\n'min' = worst model's score on that skill. A skill every model aces "
              "is knowledge the models already have; a low min is what ethskills is for.")

if __name__ == "__main__":
    main()
