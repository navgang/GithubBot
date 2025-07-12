# GitHub Workflow Automation with OpenAI

This project consists of three standalone Python scripts that automate common GitHub developer workflows using OpenAI and the GitHub API. By leveraging AI capabilities, these scripts help streamline tasks such as summarizing pull request diffs, auto-labeling issues, and generating README files, ultimately saving developers time and enhancing productivity.

## Quickstart Installation Guide

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install the required packages:**
   Make sure you have Python 3.7 or higher installed. Then, install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the root of the project directory and add your OpenAI API key and GitHub token:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   GITHUB_TOKEN=your_github_token
   ```

## Usage Instructions

### 1. Summarize Pull Request Diffs (`summarize.py`)

This script summarizes the diffs of pull requests, providing a concise overview of changes made.

**Usage:**
```bash
python scripts/summarize.py <owner> <repo> <pull_request_number>
```

**Example:**
```bash
python scripts/summarize.py yourusername your-repo 42
```

### 2. Auto-Label Issues (`issue.py`)

This script automatically labels GitHub issues based on their content using OpenAI's language model.

**Usage:**
```bash
python scripts/issue.py <owner> <repo> <issue_number>
```

**Example:**
```bash
python scripts/issue.py yourusername your-repo 10
```

### 3. Generate README File (`readme.py`)

This script generates a new `README.md` file based on the context of your repository, helping you maintain up-to-date documentation.

**Usage:**
```bash
python scripts/readme.py <owner> <repo>
```

**Example:**
```bash
python scripts/readme.py yourusername your-repo
```

## Requirements for Running Locally

To run these scripts locally, ensure you have the following:

- Python 3.7 or higher
- A valid OpenAI API key
- A valid GitHub token with appropriate permissions (e.g., repo access)
- Test payloads for simulating GitHub events (located in the `test_payloads` directory)

## Configuring the `.env` File

Create a `.env` file in the root directory of the project and include the following variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
```

Replace `your_openai_api_key` and `your_github_token` with your actual API key and token. This file is crucial for authenticating your requests to the OpenAI API and GitHub API.

## Conclusion

This project aims to enhance your GitHub workflow by automating repetitive tasks with the help of AI. By following the installation and usage instructions, you can quickly integrate these scripts into your development process. Happy coding!