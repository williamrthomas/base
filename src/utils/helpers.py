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
        
        with open(filepath, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"An error occurred while writing to {filepath}: {e}")

def load_yaml(filepath: str) -> dict:
    """Loads a YAML file and returns its contents as a dictionary."""
    try:
        with open(filepath, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: YAML file not found: {filepath}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {filepath}: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred while loading YAML file {filepath}: {e}")
        return {}
