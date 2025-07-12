#!/usr/bin/env python3
import os, subprocess
from dotenv import load_dotenv
import openai
from github import Github

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN    = os.getenv("GITHUB_TOKEN")
REPO_NAME       = os.getenv("GITHUB_REPOSITORY")

if not OPENAI_API_KEY or not GITHUB_TOKEN:
    raise SystemExit("Set OPENAI_API_KEY and GITHUB_TOKEN in your .env")

openai.api_key = OPENAI_API_KEY
gh = Github(GITHUB_TOKEN)

if not REPO_NAME:
    url = subprocess.run(
        ["git","config","--get","remote.origin.url"],
        capture_output=True, text=True
    ).stdout.strip()
    if url.startswith("git@github.com:"):
        REPO_NAME = url.split("git@github.com:")[1].rstrip(".git")
    elif url.startswith("https://github.com/"):
        REPO_NAME = url.split("https://github.com/")[1].rstrip(".git")
    else:
        raise SystemExit("Set GITHUB_REPOSITORY in .env")

repo = gh.get_repo(REPO_NAME)
branch = repo.default_branch

def list_top():
    return [e for e in os.listdir(".") if not e.startswith(".")]

def snippet(path, n=2000):
    try:
        return open(path).read()[:n]
    except:
        return ""

entries     = list_top()
req_txt     = snippet("requirements.txt")
lic_txt     = snippet("LICENSE")

prompt = f"""
You are an experienced open-source maintainer and technical writer.

Write a well-structured, developer-friendly `README.md` for this Python project. It consists of three standalone scripts that automate GitHub developer workflows using OpenAI and the GitHub API.

Your goal is to generate a README that includes:

1. A clear 2–3 sentence description of what the project does and what problem it solves
2. A quickstart installation guide based on `requirements.txt` and `.env` setup
3. Usage instructions for each script:
   - `summarize.py`: summarize GitHub pull request diffs
   - `issue.py`: auto-label issues using OpenAI
   - `readme.py`: generate a new `README.md` from repo context
4. Requirements for running locally, such as test payloads or GitHub API event simulation
5. How to configure the `.env` file
6. Clean Markdown formatting, with command-line examples

Use the following context as your source:

---

## Project Files:
{entries}

## requirements.txt (first 2000 characters):
\"\"\"{req_txt}\"\"\"

## LICENSE (first 2000 characters):
\"\"\"{lic_txt}\"\"\"

## Code Snippets from Scripts:
### summarize.py
\"\"\"{snippet("summarize.py")}\"\"\"

### issue.py
\"\"\"{snippet("issue.py")}\"\"\"

### readme.py
\"\"\"{snippet("readme.py")}\"\"\"
"""

resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}],
    temperature=0.2,
)
readme = resp.choices[0].message.content.strip()

path = "README.md"
try:
    src = repo.get_contents(path, ref=branch)
    repo.update_file(path, "Update README", readme, src.sha, branch=branch)
    print("README.md updated")
except:
    repo.create_file(path, "Create README", readme, branch=branch)
    print("README.md created")