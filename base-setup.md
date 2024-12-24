Okay, this is a great idea! Adding a development log, incorporating the OpenAI SDK, and creating helpful reference files like `manifesto.md`, `projectplan.md`, `clinetips.md`, and `librarynotes.md` will make the base project even more powerful.

Here are the updated files, incorporating your requirements and keeping in mind the principles we've discussed:

**1. `manifesto.md`**

```markdown
# Cline Software Development Manifesto

This manifesto outlines the principles and practices for software development using Cline, focusing on local Python development, simplicity, conceptual clarity, and efficient use of LLMs for content generation and data analysis.

## Core Principles

1. **Local First:** Development is primarily done locally using Python.
2. **Simplicity:** Strive for simplicity in design and implementation. Avoid over-engineering.
3. **Conceptual Clarity:** Focus on the conceptual level of the software, ensuring a clear understanding of the problem and solution before diving into code.
4. **Manifesto as a Guide:** Always refer back to this manifesto for guidance and consistency.
5. **Standard Libraries:** Utilize a standard set of libraries for common tasks, particularly in content generation and data analysis involving LLMs.
6. **Virtual Environments:** Use a separate virtual environment (venv) for each project to manage dependencies.
7. **Secure Key Management:** Store API keys and other sensitive information in a `.env` file, which is never committed to version control.
8. **Version Control:** Use GitHub for version control and collaboration.
9. **Pragmatic Testing:** Implement just enough testing to ensure functionality and prevent regressions, without getting bogged down in excessive test coverage.
10. **Lean Design:** Design systems with minimal complexity, focusing on essential features and avoiding unnecessary abstractions.
11. **Reusable Components:** Build modular, reusable components to promote code reuse and maintainability.
12. **Repeatable Patterns:** Employ consistent design patterns and frameworks across projects to streamline development and improve predictability.
13. **Cline-Aware Development:** Optimize interactions with Cline by understanding its context limitations and breaking down large files into manageable chunks.
14. **Development Log:** Maintain a running session development log to track progress, decisions, and next steps.

## Standard Libraries

*   **LangChain:** A framework for developing applications with language models.
*   **LlamaIndex:** A data framework for building LLM applications over external data.
*   **PyMuPDF:** For reading PDF files.
*   **Openpyxl:** For working with Excel files.
*   **Requests:** For making HTTP requests.
*   **Beautiful Soup:** For parsing HTML and XML.
*   **NumPy:** For numerical computing.
*   **Pandas:** For data manipulation and analysis.
*   **Scikit-learn:** For machine learning tasks.
*   **Requests-cache:** For caching API responses.
*   **OpenAI:** For interacting with OpenAI models (used for utilities and potential direct interaction in the future).

## Development Workflow

1. **Project Setup:**
    *   Create a new GitHub repository, initialized from the standard template.
    *   Clone the repository locally.
    *   Create a virtual environment: `python3 -m venv .venv`
    *   Activate the virtual environment:
        *   macOS/Linux: `source .venv/bin/activate`
        *   Windows: `.venv\Scripts\activate`
    *   Customize the `config.yaml` file
    *   Customize the `system_prompt.md` file
    *   Fill in the `.env.example` file and rename it to `.env`
    *   Install dependencies using `pip install -r requirements.txt`
2. **Conceptualization:**
    *   Clearly define the problem you're trying to solve.
    *   Outline the high-level architecture and design of your solution.
    *   Identify the key components and their interactions.
    *   Use diagrams, flowcharts, or pseudocode to illustrate your ideas.
    *   Update the project-specific "system prompt" to guide Cline in creating this project. Store it as markdown in a `SYSTEM_PROMPT.md` file.
3. **Implementation:**
    *   Develop incrementally, focusing on one component or feature at a time.
    *   Use Cline to assist with code generation, refactoring, and debugging.
    *   Leverage the standard libraries whenever possible.
    *   Follow the repeatable patterns and frameworks established for similar tasks.
    *   Keep functions and modules short and focused.
    *   Write clear and concise comments to explain complex logic.
    *   When dealing with large files, break them into smaller parts that Cline can process effectively. Provide Cline with instructions on how to recombine them if needed.
4. **Testing:**
    *   Write unit tests to verify the functionality of individual components.
    *   Use integration tests to ensure that different components work together correctly.
    *   Perform end-to-end tests to validate the overall system behavior.
    *   Focus on testing critical paths and edge cases.
    *   Use assertions liberally to catch unexpected behavior early.
5. **Iteration:**
    *   Regularly review your code and refactor as needed to improve clarity and maintainability.
    *   Seek feedback from Cline and incorporate its suggestions.
    *   Continuously evaluate your design and make adjustments based on new insights or requirements.
6. **Session Development Log:**
    *   At the end of each development session with Cline, update the project's development log file (`dev_log.md`).
    *   Each log entry should include:
        *   **Date and Time:** Timestamp of the session.
        *   **Session Goal:** A brief description of what you aimed to achieve in the session.
        *   **Work Completed:** A summary of the tasks accomplished, code written, or problems solved.
        *   **Challenges Faced:** Any difficulties or roadblocks encountered during the session.
        *   **Decisions Made:** Key design or implementation decisions made, along with their rationale.
        *   **Suggested Next Steps:**  A list of potential next actions or areas to focus on in the following session. This might include tasks for you or for Cline.
        *   **Open Questions:** Any questions that need to be answered or issues that require further investigation.

## Repeatable Patterns and Frameworks

*   **API Orchestration:** Use a consistent pattern for managing interactions with multiple APIs or services. A dedicated module or class will handle API requests, authentication, and error handling.
*   **Prompt Storage:** Store prompts for LLMs as markdown (`.md`) or text (`.txt`) files in a dedicated `prompts/` directory. Use a consistent naming convention (e.g., `verb-noun.md` or `component-action.md`). Each prompt file should include a clear description of its purpose and any relevant parameters.
*   **Data Handling:** Use a standard approach for loading, processing, and storing data. Use Pandas DataFrames for tabular data and define a consistent schema for data validation.
*   **Configuration:** Use a standard format (e.g., YAML, JSON) for configuration files and store them in a `config/` directory.
*   **Logging:** Use Python's built-in `logging` module with a consistent format for log messages. Decide on specific log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and when to use them.
*   **Error Handling:** Implement a standard way of handling errors and exceptions, including logging, reporting, and potentially retrying operations.
*   **Utility Functions:** Create a `utils.py` file for common utility functions that can be reused across the project.

## Cline-Specific Considerations

*   **Context Limitations:** Be mindful of Cline's context window limitations. Avoid passing excessively large files or code snippets. Break down complex tasks into smaller, more manageable steps.
*   **File Chunking:** For large files, develop a strategy for splitting them into smaller chunks that Cline can process effectively. You might use a consistent chunking function (e.g., split by lines, functions, or classes) or provide Cline with specific instructions on how to divide the file.
*   **Explicit Instructions:** Provide clear and explicit instructions to Cline, especially when dealing with complex or multi-step tasks. Use the project-specific system prompt defined in the conceptualization stage.
*   **Iterative Refinement:** Use Cline iteratively. Start with a basic implementation and refine it based on Cline's feedback and suggestions.
*   **Avoid Unnecessary Interactions:** When Cline needs to perform a series of operations on a file, structure your prompts to minimize the number of round trips. For example, instead of asking Cline to read a file, then modify it, and then read it again, combine these operations into a single prompt.

## Example Directory Structure

```
my_project/
├── .venv/                # Virtual environment
├── .env                  # Environment variables (API keys, etc.)
├── .env.example          # Example .env file
├── .gitignore            # Git ignore file
├── prompts/              # Prompts for LLMs
│   ├── create_api_client.md
│   └── process_data.md
├── src/                  # Source code
│   ├── api/              # API interaction modules
│   │   ├── __init__.py
│   │   └── my_api_client.py # Includes LLM client
│   ├── data/             # Data processing modules
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py           # Main application entry point
├── tests/                # Unit tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_data.py
├── config/               # Configuration files
│   └── config.yaml
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── SYSTEM_PROMPT.md      # Project specific system prompt
├── dev_log.md            # Development log
├── projectplan.md        # High-level project plan and goals
├── clinetips.md          # Tips for working effectively with Cline
└── librarynotes.md       # Notes on standard libraries used in the project
```

## Conclusion

This manifesto provides a framework for developing software with Cline, emphasizing local Python development, simplicity, and effective use of LLMs. By adhering to these principles and practices, you can build robust, maintainable, and conceptually sound software while leveraging the power of Cline as a collaborative coding partner. Remember that this is a living document, and it should be revisited and updated as needed to reflect evolving best practices and project requirements.
```

**2. `projectplan.md` (Template)**

```markdown
# Project Plan: \[Project Name]

## Overview

\[Provide a brief description of the project and its goals. What problem are you trying to solve? What will the software do?]

## Goals

*   \[List the main objectives of the project.]
*   \[Be specific and measurable.]
*   \[Example: Create an LLM-powered application that summarizes customer reviews from a given website.]

## Key Features

*   \[Describe the core features of the software.]
*   \[Example: Fetch reviews from a specified URL.]
*   \[Example: Use an LLM to summarize the reviews.]
*   \[Example: Display the summaries in a user-friendly format.]

## Technical Approach

*   \[Outline the technical strategy for implementing the project.]
*   \[Mention the main components, libraries, and APIs that will be used.]
*   \[Example: Use the `requests` library to fetch data, `Beautiful Soup` to parse HTML, and `LangChain` to interface with the LLM.]

## Development Stages

1. **Stage 1:** \[Description of the first stage]
    *   \[Tasks to be completed in this stage]
    *   \[Expected outcome]
2. **Stage 2:** \[Description of the second stage]
    *   \[Tasks to be completed in this stage]
    *   \[Expected outcome]
    *   ...

## Open Questions

*   \[List any unresolved issues or questions that need to be addressed.]

## Notes

*   \[Any additional notes or considerations.]
```

**3. `clinetips.md`**

```markdown
# Cline Tips

This document provides tips for working effectively with Cline.

## General Tips

*   **Be Specific:** Provide clear and specific instructions to Cline. The more context you give, the better it will understand your requests.
*   **Break Down Tasks:** Divide complex tasks into smaller, more manageable subtasks. This helps Cline stay within its context window and produce more accurate results.
*   **Iterate:** Use Cline iteratively. Start with a basic implementation and refine it based on Cline's feedback and suggestions.
*   **Use Comments:**  Write clear comments in your code to explain your logic and intent to Cline.
*   **Leverage System Prompt:**  Utilize the `SYSTEM_PROMPT.md` file to guide Cline's overall behavior and understanding of the project.
*   **Review and Refactor:** Regularly review and refactor your code with Cline's help to maintain code quality.
*   **Context Window:** Keep in mind the model's context window limitations.
*   **Use @ Mentions:** In the Cline chat, use @mentions to provide context: `@file`, `@folder`, `@problems`, `@url`.

## File Handling

*   **Chunk Large Files:** For large files, provide instructions on how to split them into smaller chunks. For example:
    ```
    "Split the file 'large_file.txt' into chunks of 100 lines each. 
    Process each chunk separately and then combine the results."
    ```
*   **Provide Context:** When asking Cline to modify a specific part of a file, provide sufficient surrounding context to ensure it understands where the changes should be made.
*   **Explicitly State the Whole File:** If asking for edits and the edits involve the whole file (like adding imports), tell Cline to include the whole file in it's response.

## Prompting Strategies

*   **Chain-of-Thought:** Encourage Cline to "think step-by-step" or explain its reasoning before providing a solution.
*   **Few-Shot Learning:** Provide examples of the desired output format or behavior in your prompts.
*   **Role-Playing:** Assign Cline a specific role (e.g., "You are an expert Python developer") to guide its responses.
*   **Prompt Chaining:** Structure your interactions with Cline as a series of connected prompts, where the output of one prompt becomes the input for the next.

## Debugging

*   **Use `print()` Statements:** Ask Cline to add `print()` statements to your code to help you understand the flow of execution and identify potential issues.
*   **Leverage Error Messages:** Provide Cline with error messages or stack traces to help it diagnose and fix bugs.
*   **Ask for Explanations:** If Cline's code doesn't work as expected, ask it to explain its reasoning and suggest alternative approaches.
*   **Inspect Intermediate Outputs:** If Cline is performing a multi-step operation, ask it to show its intermediate outputs to verify that each step is working correctly.

## Tools

*   **Use `list_files_top_level` and `list_files_recursive` to get a comprehensive view of the project's directory structure.**
*   **Use `search_files` to quickly find relevant files based on keywords or patterns.**
*   **Use `view_source_code_definitions_top_level` to explore function and class definitions in your code.**
*   **Use `read_file`, `edit_file`, and `create_new_file` with clear instructions on file paths and content.**
*   **Utilize the `execute_command` tool with caution, always reviewing the command before approving it.**
*   **Use `inspect_site` to provide Claude with information from websites. Use clear directions on what you want Claude to do or find on the site.**

## Example Prompts

*   "Create a Python function called `calculate_sum` that takes a list of numbers as input and returns their sum. Add a docstring to explain the function's purpose and parameters. Save it in `src/utils/helpers.py`"
*   "Refactor the `process_data` function in `src/data/data_loader.py` to improve its readability and efficiency. Consider using list comprehensions where appropriate."
*   "I'm getting a `TypeError` on line 42 of `main.py`. Here's the error message: `TypeError: 'int' object is not iterable`. Can you help me fix it?"
*   "What are the potential security vulnerabilities in the `api_client.py` file? Suggest improvements to make it more secure."
*   "Generate unit tests for the `utils.py` module and save them in `tests/test_utils.py`."
*   "Search for the definition of the `User` class in the project and show me its methods and attributes."
*   "Find all files that import the `requests` library."
*   "Find all files that contain the string `TODO` and list them."
*   "Using the `inspect_site` tool, go to `https://www.example.com`, find the search bar, and search for 'climate change'. Return the first 5 search results."
*   "Using the `inspect_site` tool, launch a browser and navigate to `http://localhost:3000`. Click on the button with the label 'Submit'."
*   "Analyze the `process_data` function in `src/data/data_loader.py` and suggest improvements to its time complexity."

## Limitations

*   **Context Window:** Be mindful of the model's context window limitations.
*   **State:** Cline doesn't have long-term memory between tasks. Provide all necessary context in each task.
*   **External Dependencies:** If your code relies on external libraries or services, make sure they are properly installed and configured.
*   **Nondeterministic Behavior:** LLMs can sometimes produce slightly different outputs for the same input. Be prepared to iterate and refine your prompts.

By following these tips and understanding Cline's capabilities and limitations, you can work together more effectively to build high-quality software.
```

**4. `librarynotes.md`**

```markdown
# Library Notes

This document provides a brief overview of the standard libraries used in our projects and some tips for working with them effectively.

## LangChain

*   **Purpose:** Framework for building applications with language models.
*   **Key Features:**
    *   Model I/O: Abstraction over interacting with various LLMs
    *   Chains: Compose multiple LLM calls or other operations into sequences
    *   Agents: Allow LLMs to interact with external tools
    *   Memory: Manage conversation history
    *   Prompt Templates: Manage and reuse prompts
*   **Tips:**
    *   Use the documentation extensively: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)
    *   Start with simple chains and gradually build up complexity.
    *   Experiment with different prompt templates to optimize performance.
    *   Use the `verbose` flag for debugging chains and agents.
*   **Cline Usage:**
    *   Define the model to use in the project's `config.yaml`
    *   When appropriate, use the `ConversationChain` to enable multi-turn conversations with Cline.
    *   Use prompt templates to provide context and instructions to the model.

## LlamaIndex

*   **Purpose:** Data framework for connecting LLMs to external data sources.
*   **Key Features:**
    *   Data Loaders: Ingest data from various sources (files, APIs, databases).
    *   Index Structures: Efficiently organize and retrieve data for LLM consumption.
    *   Query Engines: Interface for asking questions over your data.
    *   Document Summarization: Summarize large documents or collections of documents.
*   **Tips:**
    *   Refer to the documentation for available data loaders: [https://docs.llamaindex.ai/en/stable/module_guides/loading/](https://docs.llamaindex.ai/en/stable/module_guides/loading/)
    *   Choose the appropriate index structure based on your data and query needs.
    *   Experiment with different query engine configurations.
*   **Cline Usage:**
    *   Use LlamaIndex to load and index project-specific data, then use the query engine to provide relevant information to Cline in prompts.

## PyMuPDF

*   **Purpose:** Library for working with PDF files (and other document formats).
*   **Key Features:**
    *   Extract text, images, and metadata from PDFs.
    *   Render PDF pages as images.
    *   Create and modify PDF files.
*   **Tips:**
    *   See the documentation for detailed usage: [https://pymupdf.readthedocs.io/en/latest/](https://pymupdf.readthedocs.io/en/latest/)
*   **Cline Usage:**
    *   When a task involves PDFs, use PyMuPDF to extract the text content and provide it to Cline.
    *   Use `fitz.open()` to open a PDF document.
    *   Iterate through pages using `doc.pages()`.
    *   Extract text from a page using `page.get_text()`.

## Openpyxl

*   **Purpose:** Library for reading and writing Excel 2010+ files (.xlsx, .xlsm, .xltx, .xltm).
*   **Key Features:**
    *   Read and write cell values, formulas, and styles.
    *   Create charts and tables.
    *   Manipulate worksheets and workbooks.
*   **Tips:**
    *   Refer to the documentation: [https://openpyxl.readthedocs.io/en/stable/](https://openpyxl.readthedocs.io/en/stable/)
    *   Use the `load_workbook()` function to open an existing Excel file.
    *   Access worksheets using `workbook[sheetname]`.
    *   Access cells using `worksheet[cellname]` or `worksheet.cell(row, column)`.
*   **Cline Usage:**
    *   Use Openpyxl when tasks involve reading or modifying Excel files.
    *   Provide specific instructions to Cline on which sheets and cells to access.

## Requests

*   **Purpose:**  Making HTTP requests to interact with web APIs.
*   **Key Features:**
    *   Simple and intuitive API.
    *   Supports various HTTP methods (GET, POST, PUT, DELETE, etc.).
    *   Handles headers, cookies, and authentication.
    *   Handles JSON and form data.
*   **Tips:**
    *   Documentation: [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)
    *   Use `requests.get()` for making GET requests.
    *   Use `requests.post()` for making POST requests.
    *   Use the `json` parameter to automatically parse JSON responses.
*   **Cline Usage:**
    *   When tasks require fetching data from APIs or interacting with web services, use the `requests` library.
    *   Provide clear instructions to Cline on the API endpoint, HTTP method, and any required parameters or headers.

## Beautiful Soup

*   **Purpose:** Parsing HTML and XML documents.
*   **Key Features:**
    *   Navigates and searches the parse tree.
    *   Handles poorly formatted HTML.
    *   Extracts data from specific tags and attributes.
*   **Tips:**
    *   Documentation: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    *   Create a `BeautifulSoup` object by passing the HTML/XML content and the parser to use (e.g., `html.parser`).
    *   Use methods like `find()`, `find_all()`, `select()` to navigate and search the document.
*   **Cline Usage:**
    *   Use Beautiful Soup when tasks involve scraping data from websites or parsing HTML/XML content.
    *   Provide specific instructions to Cline on which elements or attributes to extract.

## NumPy

*   **Purpose:** Fundamental library for numerical computing in Python.
*   **Key Features:**
    *   Powerful N-dimensional array objects.
    *   Broadcasting functions.
    *   Linear algebra, Fourier transform, and random number capabilities.
*   **Tips:**
    *   Documentation: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
    *   Use NumPy arrays for efficient numerical operations.
    *   Leverage broadcasting to perform operations on arrays of different shapes.
*   **Cline Usage:**
    *   Use NumPy when tasks involve numerical computations, matrix operations, or working with large datasets.

## Pandas

*   **Purpose:** Data manipulation and analysis library.
*   **Key Features:**
    *   DataFrame object for tabular data.
    *   Data alignment and handling of missing data.
    *   Reshaping and pivoting of datasets.
    *   Data aggregation and transformations.
    *   Reading and writing data from various file formats (CSV, Excel, SQL, etc.).
*   **Tips:**
    *   Documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
    *   Use DataFrames to represent and manipulate tabular data.
    *   Learn the various methods for data selection, filtering, and transformation.
*   **Cline Usage:**
    *   Use Pandas when tasks involve working with structured data, especially when data cleaning, transformation, or analysis is required.

## Scikit-learn

*   **Purpose:** Machine learning library.
*   **Key Features:**
    *   Classification, regression, clustering, dimensionality reduction algorithms.
    *   Model selection and evaluation tools.
    *   Preprocessing and feature extraction utilities.
*   **Tips:**
    *   Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
    *   Familiarize yourself with the different types of machine learning algorithms available.
    *   Use the `train_test_split` function for model evaluation.
    *   Use pipelines to streamline preprocessing and model training.
*   **Cline Usage:**
    *   Use Scikit-learn when tasks involve building and evaluating machine learning models.
    *   Provide clear instructions to Cline on the type of model to use, the features to include, and the evaluation metrics to optimize.

## Requests-cache

*   **Purpose:** Transparent persistent cache for the `requests` library.
*   **Key Features:**
    *   Automatically caches responses to HTTP requests.
    *   Reduces the number of API calls made.
    *   Improves performance by serving cached responses.
*   **Tips:**
    *   Documentation: [https://requests-cache.readthedocs.io/en/stable/](https://requests-cache.readthedocs.io/en/stable/)
    *   Install the library: `pip install requests-cache`
    *   Configure the cache backend (e.g., SQLite, Redis, MongoDB).
    *   Use `requests_cache.install_cache()` to enable caching globally.
    *   Use `CachedSession` for more fine-grained control over caching behavior.
*   **Cline Usage:**
    *   Enable requests-cache to reduce the number of API calls made by Cline, especially when working with APIs that have rate limits or cost associated with usage.
    *   Set an appropriate cache expiration time based on the frequency of data updates.

## OpenAI

*   **Purpose:** Official Python library for interacting with OpenAI's API.
*   **Key Features:**
    *   Access to OpenAI models like GPT-4, DALL-E, etc.
    *   Provides utilities for text generation, image generation, and more.
*   **Tips:**
    *   Documentation: [https://github.com/openai/openai-python](https://github.com/openai/openai-python)
    *   Install the library: `pip install openai`
    *   Set your OpenAI API key using `openai.api_key = "YOUR_API_KEY"`
*   **Cline Usage:**
    *   Although the primary interaction with LLMs in this project is through OpenRouter, the OpenAI library can be useful for tasks such as embedding generation or fine-tuning, when needed.
    *   Also, this library is useful for its utilities. For instance, token counting using `tiktoken`.

## General Notes

*   This list is not exhaustive. Other libraries may be added as needed based on project requirements.
*   Always refer to the official documentation of each library for the most up-to-date information.
*   Use virtual environments to manage project dependencies.
*   Keep your `requirements.txt` file updated with the libraries and their versions used in your project.

By understanding the capabilities of these libraries, you can effectively guide Cline in utilizing them to accomplish various tasks.
```

**5. `dev_log.md` (Template)**

```markdown
# Development Log

## Session: \[YYYY-MM-DD] - \[Start Time] to \[End Time]

**Session Goal:**

*   \[Describe the goal for this development session.]

**Work Completed:**

*   \[Summarize the tasks completed, code written, or problems solved during this session.]

**Challenges Faced:**

*   \[Describe any difficulties or roadblocks encountered.]

**Decisions Made:**

*   \[Document any significant design or implementation decisions, along with their rationale.]

**Suggested Next Steps:**

*   \[List potential next actions or areas to focus on in the next session. This could include tasks for you or for Cline.]

**Open Questions:**

*   \[Any questions that need to be answered or issues that require further investigation.]

---

<!-- Add new session entries above this line -->
```

**6. Updated `src/api/llm_client.py` (Example)**

```python
import os
import openai
from dotenv import load_dotenv
from typing import List, Dict, Any
import requests
import requests_cache

# Load environment variables from .env file
load_dotenv()

class LLMClient:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.base_url = self.config.get("base_url", "")
        self.api_key = os.getenv(self.config.get("api_key_env_var", ""))
        self.model = self.config.get("model", "")
        self.requests_cache_seconds = self.config.get("requests_cache_seconds", -1) # -1 for no expiration, 0 to disable caching

        if self.requests_cache_seconds > 0:
            requests_cache.install_cache('llm_requests_cache', expire_after=self.requests_cache_seconds)

        # Initialize the OpenAI client (used for utilities or potential direct interaction)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if openai.api_key is not None:
            print("OpenAI API key loaded successfully.")

    def send_prompt(self, prompt: str, messages:List[Dict[str,str]]=[], max_tokens: int = 500, temperature: float = 0.7, stop_sequences: List[str] = [], n: int = 1, model:str|None=None) -> str:
        """Sends a prompt to the LLM and returns the response."""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": model if model is not None else self.model,
            "messages": [{"role": "system", "content": prompt}] + messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stop": stop_sequences,
            "n": n,
        }
        # print(data) #uncomment for debugging
        try:
            response = requests.post(self.base_url, headers=headers, json=data, timeout=300)
            response.raise_for_status()  # Raise an exception for bad status codes
            response_json = response.json()
            # print(response_json) #uncomment for debugging

            # Check for choices and extract the text
            if "choices" in response_json and len(response_json["choices"]) > 0:
                return response_json["choices"][0]["message"]["content"].strip()
            else:
                print("Error: No choices returned in the response.")
                return ""  # Handle cases where no choices are returned
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return str(e)  # Provide error information

    def count_tokens(self, text: str) -> int:
        """Counts the number of tokens in a given text using the OpenAI tokenizer."""
        try:
            import tiktoken
        except ImportError:
            print("Warning: tiktoken not installed. Please install it via 'pip install tiktoken' for accurate token counting.")
            return len(text) // 4  # Rough estimate

        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo") # Use appropriate encoding, we default to gpt-3.5-turbo since it's used for most openrouter models
        return len(encoding.encode(text))

    def build_messages(self, messages, latest_message):
        # Function to format messages into the structure expected by the API
        formatted_messages = []
        for msg in messages:
            if msg.get("say") == "user_feedback":
                formatted_messages.append({"role": "user", "content": msg["text"]})
            elif msg.get("say") == "text":
                formatted_messages.append({"role": "assistant", "content": msg["text"]})

        if latest_message.get("ask") == "followup":
            formatted_messages.append({"role": "assistant", "content": latest_message["text"]})
        
        return formatted_messages
```

**7. Updated `config/config.yaml` (Example)**

```yaml
llm:
  api_provider: "openrouter" # or "openai", "anthropic", etc.
  base_url: "https://openrouter.ai/api/v1/chat/completions" #  Make sure to change this if you are using a different provider
  api_key_env_var: "OPENROUTER_API_KEY" # or "ANTHROPIC_API_KEY", "OPENAI_API_KEY", etc.
  model: "anthropic/claude-3.5-sonnet" # Default model
  max_tokens: 8192  # Default max tokens
  temperature: 0.7 # Default temperature
  requests_cache_seconds: 86400 # Cache enabled for 1 day by default
```

**8. Updated `.gitignore`**

```
# Ignore virtual environment directory
.venv/
.env

# Ignore other sensitive files or directories
__pycache__/
*.pyc
*.log
```

**9. Updated `requirements.txt`**

```
langchain
llama-index
pymupdf
openpyxl
requests
beautifulsoup4
numpy
pandas
scikit-learn
requests-cache
openai
PyYAML
tiktoken # for counting tokens with OpenAI models
```

**10. Updated `src/utils/helpers.py`**

```python
import os
import yaml

def read_file(filepath: str) -> str:
    """Reads the content of a file."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return ""
    except Exception as e:
        print(f"An error occurred while reading {filepath}: {e}")
        return ""

def write_file(filepath: str, content: str) -> None:
    """Writes content to a file."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w") as f