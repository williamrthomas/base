# Library Notes

This document provides a brief overview of the standard libraries used in our projects and some tips for working with them effectively.

## LangChain

* **Purpose:** Framework for building applications with language models.
* **Key Features:**
    * Model I/O: Abstraction over interacting with various LLMs
    * Chains: Compose multiple LLM calls or other operations into sequences
    * Agents: Allow LLMs to interact with external tools
    * Memory: Manage conversation history
    * Prompt Templates: Manage and reuse prompts
* **Tips:**
    * Use the documentation extensively: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)
    * Start with simple chains and gradually build up complexity.
    * Experiment with different prompt templates to optimize performance.
    * Use the `verbose` flag for debugging chains and agents.
* **Cline Usage:**
    * Define the model to use in the project's `config.yaml`
    * When appropriate, use the `ConversationChain` to enable multi-turn conversations with Cline.
    * Use prompt templates to provide context and instructions to the model.

## LlamaIndex

* **Purpose:** Data framework for connecting LLMs to external data sources.
* **Key Features:**
    * Data Loaders: Ingest data from various sources (files, APIs, databases).
    * Index Structures: Efficiently organize and retrieve data for LLM consumption.
    * Query Engines: Interface for asking questions over your data.
    * Document Summarization: Summarize large documents or collections of documents.
* **Tips:**
    * Refer to the documentation for available data loaders: [https://docs.llamaindex.ai/en/stable/module_guides/loading/](https://docs.llamaindex.ai/en/stable/module_guides/loading/)
    * Choose the appropriate index structure based on your data and query needs.
    * Experiment with different query engine configurations.
* **Cline Usage:**
    * Use LlamaIndex to load and index project-specific data, then use the query engine to provide relevant information to Cline in prompts.

## PyMuPDF

* **Purpose:** Library for working with PDF files (and other document formats).
* **Key Features:**
    * Extract text, images, and metadata from PDFs.
    * Render PDF pages as images.
    * Create and modify PDF files.
* **Tips:**
    * See the documentation for detailed usage: [https://pymupdf.readthedocs.io/en/latest/](https://pymupdf.readthedocs.io/en/latest/)
* **Cline Usage:**
    * When a task involves PDFs, use PyMuPDF to extract the text content and provide it to Cline.
    * Use `fitz.open()` to open a PDF document.
    * Iterate through pages using `doc.pages()`.
    * Extract text from a page using `page.get_text()`.

## Openpyxl

* **Purpose:** Library for reading and writing Excel 2010+ files (.xlsx, .xlsm, .xltx, .xltm).
* **Key Features:**
    * Read and write cell values, formulas, and styles.
    * Create charts and tables.
    * Manipulate worksheets and workbooks.
* **Tips:**
    * Refer to the documentation: [https://openpyxl.readthedocs.io/en/stable/](https://openpyxl.readthedocs.io/en/stable/)
    * Use the `load_workbook()` function to open an existing Excel file.
    * Access worksheets using `workbook[sheetname]`.
    * Access cells using `worksheet[cellname]` or `worksheet.cell(row, column)`.
* **Cline Usage:**
    * Use Openpyxl when tasks involve reading or modifying Excel files.
    * Provide specific instructions to Cline on which sheets and cells to access.

## Requests

* **Purpose:**  Making HTTP requests to interact with web APIs.
* **Key Features:**
    * Simple and intuitive API.
    * Supports various HTTP methods (GET, POST, PUT, DELETE, etc.).
    * Handles headers, cookies, and authentication.
    * Handles JSON and form data.
* **Tips:**
    * Documentation: [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)
    * Use `requests.get()` for making GET requests.
    * Use `requests.post()` for making POST requests.
    * Use the `json` parameter to automatically parse JSON responses.
* **Cline Usage:**
    * When tasks require fetching data from APIs or interacting with web services, use the `requests` library.
    * Provide clear instructions to Cline on the API endpoint, HTTP method, and any required parameters or headers.

## Beautiful Soup

* **Purpose:** Parsing HTML and XML documents.
* **Key Features:**
    * Navigates and searches the parse tree.
    * Handles poorly formatted HTML.
    * Extracts data from specific tags and attributes.
* **Tips:**
    * Documentation: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * Create a `BeautifulSoup` object by passing the HTML/XML content and the parser to use (e.g., `html.parser`).
    * Use methods like `find()`, `find_all()`, `select()` to navigate and search the document.
* **Cline Usage:**
    * Use Beautiful Soup when tasks involve scraping data from websites or parsing HTML/XML content.
    * Provide specific instructions to Cline on which elements or attributes to extract.

## NumPy

* **Purpose:** Fundamental library for numerical computing in Python.
* **Key Features:**
    * Powerful N-dimensional array objects.
    * Broadcasting functions.
    * Linear algebra, Fourier transform, and random number capabilities.
* **Tips:**
    * Documentation: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
    * Use NumPy arrays for efficient numerical operations.
    * Leverage broadcasting to perform operations on arrays of different shapes.
* **Cline Usage:**
    * Use NumPy when tasks involve numerical computations, matrix operations, or working with large datasets.

## Pandas

* **Purpose:** Data manipulation and analysis library.
* **Key Features:**
    * DataFrame object for tabular data.
    * Data alignment and handling of missing data.
    * Reshaping and pivoting of datasets.
    * Data aggregation and transformations.
    * Reading and writing data from various file formats (CSV, Excel, SQL, etc.).
* **Tips:**
    * Documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
    * Use DataFrames to represent and manipulate tabular data.
    * Learn the various methods for data selection, filtering, and transformation.
* **Cline Usage:**
    * Use Pandas when tasks involve working with structured data, especially when data cleaning, transformation, or analysis is required.

## Scikit-learn

* **Purpose:** Machine learning library.
* **Key Features:**
    * Classification, regression, clustering, dimensionality reduction algorithms.
    * Model selection and evaluation tools.
    * Preprocessing and feature extraction utilities.
* **Tips:**
    * Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
    * Familiarize yourself with the different types of machine learning algorithms available.
    * Use the `train_test_split` function for model evaluation.
    * Use pipelines to streamline preprocessing and model training.
* **Cline Usage:**
    * Use Scikit-learn when tasks involve building and evaluating machine learning models.
    * Provide clear instructions to Cline on the type of model to use, the features to include, and the evaluation metrics to optimize.

## Requests-cache

* **Purpose:** Transparent persistent cache for the `requests` library.
* **Key Features:**
    * Automatically caches responses to HTTP requests.
    * Reduces the number of API calls made.
    * Improves performance by serving cached responses.
* **Tips:**
    * Documentation: [https://requests-cache.readthedocs.io/en/stable/](https://requests-cache.readthedocs.io/en/stable/)
    * Install the library: `pip install requests-cache`
    * Configure the cache backend (e.g., SQLite, Redis, MongoDB).
    * Use `requests_cache.install_cache()` to enable caching globally.
    * Use `CachedSession` for more fine-grained control over caching behavior.
* **Cline Usage:**
    * Enable requests-cache to reduce the number of API calls made by Cline, especially when working with APIs that have rate limits or cost associated with usage.
    * Set an appropriate cache expiration time based on the frequency of data updates.

## OpenAI

* **Purpose:** Official Python library for interacting with OpenAI's API.
* **Key Features:**
    * Access to OpenAI models like GPT-4, DALL-E, etc.
    * Provides utilities for text generation, image generation, and more.
* **Tips:**
    * Documentation: [https://github.com/openai/openai-python](https://github.com/openai/openai-python)
    * Install the library: `pip install openai`
    * Set your OpenAI API key using `openai.api_key = "YOUR_API_KEY"`
* **Cline Usage:**
    * Although the primary interaction with LLMs in this project is through OpenRouter, the OpenAI library can be useful for tasks such as embedding generation or fine-tuning, when needed.
    * Also, this library is useful for its utilities. For instance, token counting using `tiktoken`.

## General Notes

* This list is not exhaustive. Other libraries may be added as needed based on project requirements.
* Always refer to the official documentation of each library for the most up-to-date information.
* Use virtual environments to manage project dependencies.
* Keep your `requirements.txt` file updated with the libraries and their versions used in your project.

By understanding the capabilities of these libraries, you can effectively guide Cline in utilizing them to accomplish various tasks.
