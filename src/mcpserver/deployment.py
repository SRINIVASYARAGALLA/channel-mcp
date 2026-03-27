import os
from mcp.server.fastmcp import FastMCP
from loader import load_markdown
from datetime import datetime
import logging

# Configurable file path
SKILL_PATH = os.getenv("SKILL_PATH", "./config/user-permissions/skill.md")

# Load skill content
skill_content = load_markdown(SKILL_PATH)

if not skill_content:
    raise RuntimeError("skill.md could not be loaded")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def ensure_instactions_section():
    """Ensure skill.md has a Custom Instactions section."""
    if not os.path.exists(SKILL_PATH):
        with open(SKILL_PATH, 'w', encoding='utf-8') as f:
            f.write('## Custom Instactions\n\n')
    else:
        with open(SKILL_PATH, 'r+', encoding='utf-8') as f:
            content = f.read()
            if '## Custom Instactions' not in content:
                # Append at the end instead of prepending
                if not content.endswith('\n'):
                    content += '\n'
                f.seek(0)
                f.write(content + '\n## Custom Instactions\n\n')
                f.truncate()

def log_skill_change(change_desc, status):
    """Append a change under Instactions section."""
    ensure_instactions_section()
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f'- {now}: {change_desc} (Status: {status})\n'
    with open(SKILL_PATH, 'r+', encoding='utf-8') as f:
        content = f.read()
        if '## Custom Instactions' in content:
            parts = content.split('## Custom Instactions', 1)
            before = parts[0] + '## Custom Instactions\n'
            after = parts[1].lstrip('\n')
            new_content = before + '\n' + entry + after
            f.seek(0)
            f.write(new_content)
            f.truncate()
        else:
            f.seek(0, 2)
            f.write('\n## Custom Instactions\n\n' + entry)

# Create MCP Server with Auto System Prompt Injection (no app argument)
mcp = FastMCP(
    name="channel-mcp",
    instructions=skill_content
)

@mcp.tool()
def user_permissions() -> str:
    """Create or update user permissions tab functional components based on the skill.md content, or answer any questions about the user permissions setup."""
    return "MCP Server running with injected skill.md"

@mcp.tool()
def add_custom_Instactions(change: str) -> str:
    """Log a custom change request to skill.md."""
    log_skill_change(change, "applied")
    logging.info(f"Logged custom change to skill.md: {change}")
    return f"Logged change: {change}"

if __name__ == "__main__":
    mcp.run()