# Cline Tips

This document provides tips for working effectively with Cline.

## General Tips

* **Be Specific:** Provide clear and specific instructions to Cline. The more context you give, the better it will understand your requests.
* **Break Down Tasks:** Divide complex tasks into smaller, more manageable subtasks. This helps Cline stay within its context window and produce more accurate results.
* **Iterate:** Use Cline iteratively. Start with a basic implementation and refine it based on Cline's feedback and suggestions.
* **Use Comments:**  Write clear comments in your code to explain your logic and intent to Cline.
* **Leverage System Prompt:**  Utilize the `SYSTEM_PROMPT.md` file to guide Cline's overall behavior and understanding of the project.
* **Review and Refactor:** Regularly review and refactor your code with Cline's help to maintain code quality.
* **Context Window:** Keep in mind the model's context window limitations.
* **Use @ Mentions:** In the Cline chat, use @mentions to provide context: `@file`, `@folder`, `@problems`, `@url`.

## File Handling

* **Chunk Large Files:** For large files, provide instructions on how to split them into smaller chunks. For example:
    ```
    "Split the file 'large_file.txt' into chunks of 100 lines each. 
    Process each chunk separately and then combine the results."
    ```
* **Provide Context:** When asking Cline to modify a specific part of a file, provide sufficient surrounding context to ensure it understands where the changes should be made.
* **Explicitly State the Whole File:** If asking for edits and the edits involve the whole file (like adding imports), tell Cline to include the whole file in it's response.

## Prompting Strategies

* **Chain-of-Thought:** Encourage Cline to "think step-by-step" or explain its reasoning before providing a solution.
* **Few-Shot Learning:** Provide examples of the desired output format or behavior in your prompts.
* **Role-Playing:** Assign Cline a specific role (e.g., "You are an expert Python developer") to guide its responses.
* **Prompt Chaining:** Structure your interactions with Cline as a series of connected prompts, where the output of one prompt becomes the input for the next.

## Debugging

* **Use `print()` Statements:** Ask Cline to add `print()` statements to your code to help you understand the flow of execution and identify potential issues.
* **Leverage Error Messages:** Provide Cline with error messages or stack traces to help it diagnose and fix bugs.
* **Ask for Explanations:** If Cline's code doesn't work as expected, ask it to explain its reasoning and suggest alternative approaches.
* **Inspect Intermediate Outputs:** If Cline is performing a multi-step operation, ask it to show its intermediate outputs to verify that each step is working correctly.

## Tools

* **Use `list_files_top_level` and `list_files_recursive` to get a comprehensive view of the project's directory structure.**
* **Use `search_files` to quickly find relevant files based on keywords or patterns.**
* **Use `view_source_code_definitions_top_level` to explore function and class definitions in your code.**
* **Use `read_file`, `edit_file`, and `create_new_file` with clear instructions on file paths and content.**
* **Utilize the `execute_command` tool with caution, always reviewing the command before approving it.**
* **Use `inspect_site` to provide Claude with information from websites. Use clear directions on what you want Claude to do or find on the site.**

## Example Prompts

* "Create a Python function called `calculate_sum` that takes a list of numbers as input and returns their sum. Add a docstring to explain the function's purpose and parameters. Save it in `src/utils/helpers.py`"
* "Refactor the `process_data` function in `src/data/data_loader.py` to improve its readability and efficiency. Consider using list comprehensions where appropriate."
* "I'm getting a `TypeError` on line 42 of `main.py`. Here's the error message: `TypeError: 'int' object is not iterable`. Can you help me fix it?"
* "What are the potential security vulnerabilities in the `api_client.py` file? Suggest improvements to make it more secure."
* "Generate unit tests for the `utils.py` module and save them in `tests/test_utils.py`."
* "Search for the definition of the `User` class in the project and show me its methods and attributes."
* "Find all files that import the `requests` library."
* "Find all files that contain the string `TODO` and list them."
* "Using the `inspect_site` tool, go to `https://www.example.com`, find the search bar, and search for 'climate change'. Return the first 5 search results."
* "Using the `inspect_site` tool, launch a browser and navigate to `http://localhost:3000`. Click on the button with the label 'Submit'."
* "Analyze the `process_data` function in `src/data/data_loader.py` and suggest improvements to its time complexity."

## Limitations

* **Context Window:** Be mindful of the model's context window limitations.
* **State:** Cline doesn't have long-term memory between tasks. Provide all necessary context in each task.
* **External Dependencies:** If your code relies on external libraries or services, make sure they are properly installed and configured.
* **Nondeterministic Behavior:** LLMs can sometimes produce slightly different outputs for the same input. Be prepared to iterate and refine your prompts.

By following these tips and understanding Cline's capabilities and limitations, you can work together more effectively to build high-quality software.
