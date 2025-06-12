#!/usr/bin/env python3
import os, sys, json
from github import Github
import openai

gh = Github(os.environ['GITHUB_TOKEN'])
openai.api_key = os.environ['OPENAI_API_KEY']

event = json.load(sys.stdin)
repo_name = event['repository']['full_name']
issue = event['issue']
title, body, num = issue['title'], issue['body'], issue['number']

prompt = f"""
Classify this GitHub issue into one of: bug, feature-request, documentation, performance, question.
Title: \"\"\"{title}\"\"\"
Body: \"\"\"{body}\"\"\"
Return exactly one label.
"""

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}],
    temperature=0.0,
)
label = resp.choices[0].message.content.strip().lower()

repo = gh.get_repo(repo_name)
repo.get_issue(num).add_to_labels(label)
print(f"→ Applied label: {label}")