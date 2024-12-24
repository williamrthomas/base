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
