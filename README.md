# Base Project Template

A comprehensive Python project template with LLM integration, designed for building AI-powered applications. This template provides a solid foundation with pre-configured LLM client, utility functions, and best practices documentation.

## Features

- **LLM Integration**: Pre-configured OpenRouter client for easy access to various LLM models
- **Project Structure**: Well-organized Python package structure with separate modules for API clients and utilities
- **Documentation**: Comprehensive guides and best practices
  - `manifesto.md`: Development principles and practices
  - `projectplan.md`: Template for project planning
  - `clinetips.md`: Tips for working with Cline
  - `librarynotes.md`: Documentation of standard libraries
  - `dev_log.md`: Development session tracking
- **Configuration Management**: YAML-based configuration and environment variables support
- **Development Tools**: Integrated development environment setup with virtual environment support

## Project Structure

```
my_project/
├── .venv/                # Virtual environment
├── .env                  # Environment variables (API keys, etc.)
├── .env.example          # Example .env file
├── .gitignore           # Git ignore file
├── prompts/             # Prompts for LLMs
├── src/                 # Source code
│   ├── api/             # API interaction modules
│   │   ├── __init__.py
│   │   └── llm_client.py
│   ├── utils/           # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py         # Main application entry point
├── tests/              # Unit tests
├── config/             # Configuration files
│   └── config.yaml
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
├── manifesto.md       # Development principles
├── projectplan.md     # Project planning template
├── clinetips.md      # Tips for working with Cline
├── librarynotes.md   # Library documentation
└── dev_log.md        # Development log
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/williamrthomas/base.git new-project-name
cd new-project-name
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

5. Update configuration:
```bash
# Edit config/config.yaml with your project-specific settings
```

## Development Workflow

1. Read through `manifesto.md` to understand the development principles and practices
2. Use `projectplan.md` to plan your project
3. Follow the tips in `clinetips.md` for effective development with Cline
4. Reference `librarynotes.md` for information about the standard libraries
5. Maintain a development log in `dev_log.md`

## Standard Libraries

The template includes support for common Python libraries:
- LangChain: Framework for building LLM applications
- LlamaIndex: Data framework for LLM applications
- PyMuPDF: PDF processing
- Openpyxl: Excel file handling
- Requests: HTTP client
- BeautifulSoup4: HTML parsing
- NumPy: Numerical computing
- Pandas: Data manipulation
- Scikit-learn: Machine learning
- Requests-cache: HTTP caching
- OpenAI: OpenAI API client

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
