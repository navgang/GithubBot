# GitHub Workflow Automation with OpenAI

This project consists of three standalone Python scripts designed to automate common GitHub developer workflows using the OpenAI API and the GitHub API. By streamlining tasks such as summarizing pull request diffs, auto-labeling issues, and generating `README.md` files, this project helps developers save time and improve productivity.

## Quickstart Installation Guide

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. **Install the required packages:**
   Make sure you have Python 3.7 or higher installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the root directory of the project and add your OpenAI API key and GitHub token:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   GITHUB_TOKEN=your_github_token
   ```

## Usage Instructions

### 1. Summarize Pull Request Diffs (`summarize.py`)

This script summarizes the diffs of GitHub pull requests, providing a concise overview of changes made.

**Usage:**
```bash
python scripts/summarize.py <owner> <repo> <pull_request_number>
```

**Example:**
```bash
python scripts/summarize.py yourusername yourrepo 42
```

### 2. Auto-Label Issues (`issue.py`)

This script automatically labels GitHub issues based on their content using OpenAI's language model.

**Usage:**
```bash
python scripts/issue.py <owner> <repo> <issue_number>
```

**Example:**
```bash
python scripts/issue.py yourusername yourrepo 7
```

### 3. Generate `README.md` (`readme.py`)

This script generates a new `README.md` file based on the context of the repository, helping to maintain up-to-date documentation.

**Usage:**
```bash
python scripts/readme.py <owner> <repo>
```

**Example:**
```bash
python scripts/readme.py yourusername yourrepo
```

## Requirements for Running Locally

To run the scripts locally, ensure you have the following:

- Python 3.7 or higher
- Access to the OpenAI API
- A valid GitHub token with appropriate permissions
- Test payloads located in the `test_payloads` directory for simulating GitHub events

## Configuring the `.env` File

The `.env` file should contain the following variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
```

Replace `your_openai_api_key` with your actual OpenAI API key and `your_github_token` with your GitHub personal access token.

## Conclusion

This project aims to enhance your GitHub development experience by automating repetitive tasks. Feel free to contribute or reach out with any questions or suggestions. Happy coding!