# SriniMcp

Sample MCP server using `FastMCP` (Python) for basic user-permissions operations.

## Run

From this folder:

- Run via `uv` (recommended on Windows):
	- stdio (waits for an MCP client):
		- `uv run -- python user-permissions.py`
	- SSE (HTTP transport):
		- `uv run -- python user-permissions.py --transport sse`

- Run the server (stdio):
	- `./.venv/Scripts/mcp.exe run user-permissions.py`

- Run with the MCP Inspector:
	- `./.venv/Scripts/mcp.exe dev user-permissions.py`

Note: `mcp dev` uses the Node-based MCP Inspector and requires a newer Node.js
than v16 (your logs show the inspector currently requires Node >= 22.7.5).

## What it exposes

Tools:

- `echo(text)`
- `get_user_permissions(user_id)`
- `set_user_role(user_id, role, overwrite_permissions=True)`
- `grant_permission(user_id, permission)`
- `revoke_permission(user_id, permission)`
- `list_roles()`

Resources:

- `permissions://users`
- `permissions://users/{user_id}`
