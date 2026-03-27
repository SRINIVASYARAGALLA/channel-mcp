import importlib.resources
import os

# Markdown Loader
def load_markdown(path: str) -> str:
    # Check for SKILL_PATH environment variable
    env_path = os.getenv("SKILL_PATH")
    if env_path and os.path.exists(env_path):
        try:
            with open(env_path, encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading file from SKILL_PATH env: {e}")
            return ""
    # Fallback to provided path
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading file from path: {e}")
            return ""
    # If not found, try to load from package resources
    try:
        rel_path = path.lstrip("./\\")
        parts = rel_path.split(os.sep)
        if len(parts) >= 3:
            package = f"mcpserver.{parts[0]}.{parts[1]}"
            resource = parts[2]
            with importlib.resources.files(package).joinpath(resource).open("r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print(f"Error loading file from package resources: {e}")
    return ""