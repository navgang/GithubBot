```markdown
# GitHub Workflow Automation with OpenAI

This project provides a set of three standalone Python scripts that automate common GitHub developer workflows using the OpenAI API and the GitHub API. By streamlining tasks such as summarizing pull request diffs, auto-labeling issues, and generating `README.md` files, this project aims to enhance productivity and reduce manual effort for developers.

## Quickstart Installation Guide

To get started, follow these steps to set up the project on your local machine:

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
python scripts/summarize.py <repository> <pull_request_number>
```
**Example:**
```bash
python scripts/summarize.py yourusername/your-repo 42
```

### 2. Auto-Label Issues (`issue.py`)

This script automatically labels GitHub issues based on their content using OpenAI's language model.

**Usage:**
```bash
python scripts/issue.py <repository> <issue_number>
```
**Example:**
```bash
python scripts/issue.py yourusername/your-repo 10
```

### 3. Generate `README.md` (`readme.py`)

This script generates a new `README.md` file based on the context of your repository, helping you maintain up-to-date documentation.

**Usage:**
```bash
python scripts/readme.py <repository>
```
**Example:**
```bash
python scripts/readme.py yourusername/your-repo
```

## Requirements for Running Locally

To run the scripts successfully, ensure you have:
- A valid OpenAI API key.
- A GitHub personal access token with appropriate permissions (e.g., repo access).
- Sample payloads for testing, which can be found in the `test_payloads` directory.

## Configuring the `.env` File

The `.env` file should contain the following variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
```

Replace `your_openai_api_key` and `your_github_token` with your actual API keys. Ensure that this file is kept secure and not shared publicly.

## Conclusion

This project aims to simplify and enhance your GitHub workflow by leveraging the power of OpenAI and the GitHub API. For any issues or feature requests, please open an issue in the repository. Happy coding!
```