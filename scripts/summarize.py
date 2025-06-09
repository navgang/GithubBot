#!/usr/bin/env python3
import os, sys, json
from github import Github
import openai

gh = Github(os.environ['GITHUB_TOKEN'])
openai.api_key = os.environ['OPENAI_API_KEY']

event = json.load(sys.stdin)
repo_name = event['repository']['full_name']
pr = event['pull_request']
num = pr['number']

repo = gh.get_repo(repo_name)
diff = repo.get_pull(num).diff_url
diff_text = repo._requester.requestJsonAndCheck(
    "GET", diff, headers={"Accept": "application/vnd.github.v3.diff"}
)[1][:5000]  # truncate to 5k chars

prompt = f"""
You are a code reviewer. Summarize this diff in 2–3 bullet points:
\"\"\"{diff_text}\"\"\"
"""

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}],
    temperature=0.2,
)
summary = resp.choices[0].message.content.strip()

repo.get_pull(num).create_issue_comment(f"**AI Summary:**\n{summary}")
print("→ Posted PR summary")