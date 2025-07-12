# Project Title: Streamlit OpenAI Summarizer

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Project Description

The Streamlit OpenAI Summarizer is a web application that leverages OpenAI's powerful language model to summarize text content efficiently. This project aims to simplify the process of extracting key insights from lengthy documents, articles, or any text input, making it easier for users to digest information quickly. By integrating with the OpenAI API, the application provides an intuitive interface for users to input text and receive concise summaries in real-time.

## Features

- Summarize any text input using OpenAI's language model.
- User-friendly interface built with Streamlit.
- Easy setup and deployment.

## Installation

To get started with the Streamlit OpenAI Summarizer, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/streamlit-openai-summarizer.git
   cd streamlit-openai-summarizer
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   Make sure you have Python 3.8 or higher installed. Then, run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

To launch the Streamlit application, run the following command in your terminal:

```bash
streamlit run scripts/summarize.py
```

This will start a local web server, and you can access the application by navigating to `http://localhost:8501` in your web browser.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, please fork the repository and submit a pull request. Ensure that your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the API.
- [Streamlit](https://streamlit.io/) for creating an easy-to-use framework for building web applications.

---

Feel free to reach out if you have any questions or need further assistance!