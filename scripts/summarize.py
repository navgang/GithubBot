#!/usr/bin/env python3
from dotenv import load_dotenv
import os, sys, json
from github import Github
import openai
import requests

# ─── Load your .env ─────────────────────────────────────────────────────────
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_KEY   = os.getenv("OPENAI_API_KEY")
REPO_NAME    = os.getenv("GITHUB_REPOSITORY")  # optional: for local

if not GITHUB_TOKEN or not OPENAI_KEY:
    raise SystemExit("Set GITHUB_TOKEN and OPENAI_API_KEY in your .env")

# ─── Init clients ────────────────────────────────────────────────────────────
gh = Github(GITHUB_TOKEN)
openai.api_key = OPENAI_KEY

# ─── Read webhook payload from STDIN ─────────────────────────────────────────
event     = json.load(sys.stdin)
repo_name = event["repository"]["full_name"]
pr        = event["pull_request"]
num       = pr["number"]

# ─── Determine the diff URL ──────────────────────────────────────────────────
# GitHub payload always includes `pull_request.diff_url`
diff_url = pr.get("diff_url") \
    or f"https://api.github.com/repos/{repo_name}/pulls/{num}.diff"

# ─── Fetch the raw diff via HTTP ─────────────────────────────────────────────
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept":        "application/vnd.github.v3.diff"
}
resp = requests.get(diff_url, headers=headers)
if resp.status_code != 200:
    raise SystemExit(f"Failed to fetch diff: {resp.status_code}")

diff_text = resp.text[:5000]  # limit to 5000 chars for LLM

# ─── Prompt the LLM ─────────────────────────────────────────────────────────
prompt = f"""
You are a thoughtful code reviewer. Summarize this Git diff into 2–3 concise bullet points:
```diff
{diff_text}
"""

completion = openai.ChatCompletion.create(
model="gpt-4o-mini", # or whichever model you prefer
messages=[{"role": "user", "content": prompt}],
temperature=0.2,
)
summary = completion.choices[0].message.content.strip()

# ─── 5. Post the summary as a PR comment (or print locally) ──────────────────
try:
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(num)
    pr.create_issue_comment(f"AI Summary:\n{summary}")
    print("Summary posted to GitHub PR.")
    
except Exception as e:
    print("⚠️ Could not post to GitHub (probably local test). Here’s the summary:\n")
    print(summary)