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

* **LangChain:** A framework for developing applications with language models.
* **LlamaIndex:** A data framework for building LLM applications over external data.
* **PyMuPDF:** For reading PDF files.
* **Openpyxl:** For working with Excel files.
* **Requests:** For making HTTP requests.
* **Beautiful Soup:** For parsing HTML and XML.
* **NumPy:** For numerical computing.
* **Pandas:** For data manipulation and analysis.
* **Scikit-learn:** For machine learning tasks.
* **Requests-cache:** For caching API responses.
* **OpenAI:** For interacting with OpenAI models (used for utilities and potential direct interaction in the future).

## Development Workflow

1. **Project Setup:**
    * Create a new GitHub repository, initialized from the standard template.
    * Clone the repository locally.
    * Create a virtual environment: `python3 -m venv .venv`
    * Activate the virtual environment:
        * macOS/Linux: `source .venv/bin/activate`
        * Windows: `.venv\Scripts\activate`
    * Customize the `config.yaml` file
    * Customize the `system_prompt.md` file
    * Fill in the `.env.example` file and rename it to `.env`
    * Install dependencies using `pip install -r requirements.txt`

2. **Conceptualization:**
    * Clearly define the problem you're trying to solve.
    * Outline the high-level architecture and design of your solution.
    * Identify the key components and their interactions.
    * Use diagrams, flowcharts, or pseudocode to illustrate your ideas.
    * Update the project-specific "system prompt" to guide Cline in creating this project. Store it as markdown in a `SYSTEM_PROMPT.md` file.

3. **Implementation:**
    * Develop incrementally, focusing on one component or feature at a time.
    * Use Cline to assist with code generation, refactoring, and debugging.
    * Leverage the standard libraries whenever possible.
    * Follow the repeatable patterns and frameworks established for similar tasks.
    * Keep functions and modules short and focused.
    * Write clear and concise comments to explain complex logic.
    * When dealing with large files, break them into smaller parts that Cline can process effectively. Provide Cline with instructions on how to recombine them if needed.

4. **Testing:**
    * Write unit tests to verify the functionality of individual components.
    * Use integration tests to ensure that different components work together correctly.
    * Perform end-to-end tests to validate the overall system behavior.
    * Focus on testing critical paths and edge cases.
    * Use assertions liberally to catch unexpected behavior early.

5. **Iteration:**
    * Regularly review your code and refactor as needed to improve clarity and maintainability.
    * Seek feedback from Cline and incorporate its suggestions.
    * Continuously evaluate your design and make adjustments based on new insights or requirements.

6. **Session Development Log:**
    * At the end of each development session with Cline, update the project's development log file (`dev_log.md`).
    * Each log entry should include:
        * **Date and Time:** Timestamp of the session.
        * **Session Goal:** A brief description of what you aimed to achieve in the session.
        * **Work Completed:** A summary of the tasks accomplished, code written, or problems solved.
        * **Challenges Faced:** Any difficulties or roadblocks encountered during the session.
        * **Decisions Made:** Key design or implementation decisions made, along with their rationale.
        * **Suggested Next Steps:**  A list of potential next actions or areas to focus on in the following session. This might include tasks for you or for Cline.
        * **Open Questions:** Any questions that need to be answered or issues that require further investigation.

## Repeatable Patterns and Frameworks

* **API Orchestration:** Use a consistent pattern for managing interactions with multiple APIs or services. A dedicated module or class will handle API requests, authentication, and error handling.
* **Prompt Storage:** Store prompts for LLMs as markdown (`.md`) or text (`.txt`) files in a dedicated `prompts/` directory. Use a consistent naming convention (e.g., `verb-noun.md` or `component-action.md`). Each prompt file should include a clear description of its purpose and any relevant parameters.
* **Data Handling:** Use a standard approach for loading, processing, and storing data. Use Pandas DataFrames for tabular data and define a consistent schema for data validation.
* **Configuration:** Use a standard format (e.g., YAML, JSON) for configuration files and store them in a `config/` directory.
* **Logging:** Use Python's built-in `logging` module with a consistent format for log messages. Decide on specific log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and when to use them.
* **Error Handling:** Implement a standard way of handling errors and exceptions, including logging, reporting, and potentially retrying operations.
* **Utility Functions:** Create a `utils.py` file for common utility functions that can be reused across the project.

## Cline-Specific Considerations

* **Context Limitations:** Be mindful of Cline's context window limitations. Avoid passing excessively large files or code snippets. Break down complex tasks into smaller, more manageable steps.
* **File Chunking:** For large files, develop a strategy for splitting them into smaller chunks that Cline can process effectively. You might use a consistent chunking function (e.g., split by lines, functions, or classes) or provide Cline with specific instructions on how to divide the file.
* **Explicit Instructions:** Provide clear and explicit instructions to Cline, especially when dealing with complex or multi-step tasks. Use the project-specific system prompt defined in the conceptualization stage.
* **Iterative Refinement:** Use Cline iteratively. Start with a basic implementation and refine it based on Cline's feedback and suggestions.
* **Avoid Unnecessary Interactions:** When Cline needs to perform a series of operations on a file, structure your prompts to minimize the number of round trips. For example, instead of asking Cline to read a file, then modify it, and then read it again, combine these operations into a single prompt.

## Example Directory Structure

```
my_project/
├── .venv/                # Virtual environment
├── .env                  # Environment variables (API keys, etc.)
├── .env.example          # Example .env file
├── .gitignore           # Git ignore file
├── prompts/             # Prompts for LLMs
│   ├── create_api_client.md
│   └── process_data.md
├── src/                 # Source code
│   ├── api/             # API interaction modules
│   │   ├── __init__.py
│   │   └── my_api_client.py # Includes LLM client
│   ├── data/            # Data processing modules
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── utils/            # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py          # Main application entry point
├── tests/               # Unit tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_data.py
├── config/              # Configuration files
│   └── config.yaml
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── SYSTEM_PROMPT.md     # Project specific system prompt
├── dev_log.md          # Development log
├── projectplan.md       # High-level project plan and goals
├── clinetips.md        # Tips for working effectively with Cline
└── librarynotes.md     # Notes on standard libraries used in the project
```

## Conclusion

This manifesto provides a framework for developing software with Cline, emphasizing local Python development, simplicity, and effective use of LLMs. By adhering to these principles and practices, you can build robust, maintainable, and conceptually sound software while leveraging the power of Cline as a collaborative coding partner. Remember that this is a living document, and it should be revisited and updated as needed to reflect evolving best practices and project requirements.
