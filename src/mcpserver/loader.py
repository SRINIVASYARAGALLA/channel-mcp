import importlib.resources
import os

# Markdown Loader
def load_markdown() -> str:
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
    else:
        print("[ERROR] SKILL_PATH environment variable is not set.")
    print("[ERROR] skill.md could not be loaded from SKILL_PATH.")
    return ""