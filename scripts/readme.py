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
You are an expert technical writer and open-source maintainer.

Write a high-quality `README.md` for this GitHub project using the actual code context provided below.

Focus on:
- A clear, honest project description in 2–4 sentences, explaining what the code does and what problems it solves
- Accurate installation instructions based on dependencies and usage patterns (e.g., Streamlit, OpenAI, GitHub API)
- Command-line usage examples or app launch instructions
- Clear formatting in Markdown with code blocks where needed
- Any helpful assumptions you can make from common patterns (e.g., `.env`, `requirements.txt`, Streamlit usage)

You can use placeholder badges (optional) and should write this for developers who may clone or contribute to the project.

---

## Project File List:
{entries}

## requirements.txt (first 2000 characters):
\"\"\"
{req_txt}
\"\"\"

## LICENSE (first 2000 characters):
\"\"\"
{lic_txt}
\"\"\"

## Code Snippet from `summarize.py`:
\"\"\"
{snippet("summarize.py")}
\"\"\"
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