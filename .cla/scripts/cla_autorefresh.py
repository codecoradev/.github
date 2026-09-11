#!/usr/bin/env python3
"""Re-run failing cla-check jobs whose PR author has since signed the CLA.

Runs in codecoradev/.github via the CLA Auto-refresh workflow (OWNER_PAT).
Set DRY_RUN=1 to only print intended actions (no mutations).
"""
import base64
import datetime
import json
import os
import subprocess

ORG = os.environ.get("ORG", "codecoradev")
# Repos carrying cla-check.yml. OWNER_PAT is a fine-grained token without
# org-wide repo listing permission, so /orgs/{org}/repos returns nothing —
# list the fleet explicitly (override with REPOS="a,b,c").
DEFAULT_REPOS = [
    "uteke", "titen", "cosy", "cora-code", "trapfall",
    "corin", "skill-suites", "codecoradev.github.io", "rungu", "drawover",
]
REPOS = [r for r in os.environ.get("REPOS", ",".join(DEFAULT_REPOS)).split(",") if r]
DRY = os.environ.get("DRY_RUN", "") == "1"
MIN_AGE = datetime.timedelta(minutes=20)  # rerun-spam guard


def api(path, method="GET", **params):
    cmd = ["gh", "api", path, "-X", method]
    for k, v in params.items():
        cmd += ["-f", f"{k}={v}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{path}: {r.stderr.strip()[:200]}")
    return json.loads(r.stdout) if r.stdout.strip() else {}


def signed_usernames():
    data = api(f"/repos/{ORG}/.github/contents/.cla/signatures.json")
    raw = base64.b64decode(data["content"]).decode()
    return {s["github_username"].lower() for s in json.loads(raw).get("signatures", [])}


def main():
    signed = signed_usernames()
    print(f"signed users: {len(signed)}")
    print(f"scanning repos: {len(REPOS)}")
    for name in REPOS:
        try:
            prs = api(f"/repos/{ORG}/{name}/pulls", state="open", per_page=100)
        except RuntimeError as e:
            print(f"skip {name}: {e}")
            continue
        for pr in prs:
            author = (pr.get("user") or {}).get("login", "")
            if not author or author.lower() not in signed:
                continue
            try:
                runs = api(
                    f"/repos/{ORG}/{name}/actions/workflows/cla-check.yml/runs",
                    head_sha=pr["head"]["sha"], per_page=5,
                )
            except RuntimeError as e:
                print(f"skip {name}#{pr['number']}: no cla-check runs ({e})")
                continue
            for run in runs.get("workflow_runs", []):
                if run["conclusion"] != "failure":
                    continue
                finished = datetime.datetime.fromisoformat(
                    run["updated_at"].replace("Z", "+00:00"))
                if datetime.datetime.now(datetime.timezone.utc) - finished < MIN_AGE:
                    print(f"skip {name}#{pr['number']}: run too fresh")
                    continue
                if DRY:
                    print(f"DRY: would rerun {name}#{pr['number']} run {run['id']}")
                    break
                try:
                    api(f"/repos/{ORG}/{name}/actions/runs/{run['id']}/rerun-failed-jobs",
                        method="POST")
                    print(f"rerun: {name}#{pr['number']} run {run['id']}")
                except RuntimeError as e:
                    print(f"rerun failed {name}#{pr['number']}: {e}")
                break


if __name__ == "__main__":
    main()
