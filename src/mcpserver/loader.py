import importlib.resources
import os

# Markdown Loader
def load_markdown(path: str) -> str:
    env_path = os.getenv("SKILL_PATH")
    print(f"[DEBUG] SKILL_PATH env: {env_path}")
    if env_path:
        if os.path.exists(env_path):
            try:
                with open(env_path, encoding="utf-8") as f:
                    print(f"[DEBUG] Loaded skill.md from SKILL_PATH: {env_path}")
                    return f.read()
            except Exception as e:
                print(f"[ERROR] Could not read skill.md from SKILL_PATH: {e}")
                return ""
        else:
            print(f"[ERROR] SKILL_PATH is set but file does not exist: {env_path}")
    # Fallback to provided path
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                print(f"[DEBUG] Loaded skill.md from default path: {path}")
                return f.read()
        except Exception as e:
            print(f"[ERROR] Could not read skill.md from default path: {e}")
            return ""
    # Try to load from package resources
    try:
        rel_path = path.lstrip("./\\")
        parts = rel_path.split(os.sep)
        if len(parts) >= 3:
            package = f"mcpserver.{parts[0]}.{parts[1]}"
            resource = parts[2]
            with importlib.resources.files(package).joinpath(resource).open("r", encoding="utf-8") as f:
                print(f"[DEBUG] Loaded skill.md from package resources: {package}/{resource}")
                return f.read()
    except Exception as e:
        print(f"[ERROR] Could not read skill.md from package resources: {e}")
    print("[ERROR] skill.md could not be loaded from any location.")
    return ""