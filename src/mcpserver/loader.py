import importlib.resources
import os

# Markdown Loader
def load_markdown(path: str) -> str:
    # Try to load from environment path first
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading file from path: {e}")
            return ""
    # If not found, try to load from package resources
    try:
        # Remove leading ./ or / if present
        rel_path = path.lstrip("./\\")
        # Split into package and resource
        parts = rel_path.split(os.sep)
        if len(parts) >= 3:
            package = f"mcpserver.{parts[0]}.{parts[1]}"
            resource = parts[2]
            with importlib.resources.files(package).joinpath(resource).open("r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print(f"Error loading file from package resources: {e}")
    return ""