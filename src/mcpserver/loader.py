from pathlib import Path
 
# Markdown Loader
def load_markdown(path: str) -> str:
    try:
        file_path = Path(path).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"{path} not found")
        return file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""