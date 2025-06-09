#!/usr/bin/env python3
import os, subprocess
from dotenv import load_dotenv
import openai
from github import Github

# load secrets
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN    = os.getenv("GITHUB_TOKEN")
REPO_NAME       = os.getenv("GITHUB_REPOSITORY")

if not OPENAI_API_KEY or not GITHUB_TOKEN:
    raise SystemExit("Set OPENAI_API_KEY and GITHUB_TOKEN in your .env")

openai.api_key = OPENAI_API_KEY
gh = Github(GITHUB_TOKEN)

# infer repo if needed
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
You are an expert open-source maintainer. Generate a clear, friendly README.md:
- Project name & one-line description
- Installation steps
- Basic usage
- How to contribute
- Where to get help

Top-level files/folders:
{entries}

requirements.txt (first 2000 chars):
\"\"\"{req_txt}\"\"\"

LICENSE (first 2000 chars):
\"\"\"{lic_txt}\"\"\"
"""

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}],
    temperature=0.3,
)
readme = resp.choices[0].message.content.strip()

# commit or update README.md
path = "README.md"
try:
    src = repo.get_contents(path, ref=branch)
    repo.update_file(path, "Update README", readme, src.sha, branch=branch)
    print("README.md updated")
except:
    repo.create_file(path, "Create README", readme, branch=branch)
    print("README.md created")