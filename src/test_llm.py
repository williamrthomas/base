import yaml
from api.llm_client import LLMClient
from utils.helpers import load_yaml

def main():
    # Load config
    config = load_yaml("config/config.yaml")
    if not config or "llm" not in config:
        print("Error: Could not load LLM configuration")
        return

    # Initialize LLM client
    llm_client = LLMClient(config["llm"])

    # Test prompt
    test_prompt = "Say hello and confirm you're working properly."
    print("\nSending test prompt:", test_prompt)
    print("\nResponse:")
    response = llm_client.send_prompt(test_prompt)
    print(response)

if __name__ == "__main__":
    main()
