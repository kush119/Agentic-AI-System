from fastmcp import FastMCP
from core.config import SERVER_NAME, SERVER_PORT

# Import tools (important: this registers them)
from tools.mock_tools import mcp as tools_mcp

mcp = FastMCP(
    name=SERVER_NAME,
    instructions="""
    You are a tool server that provides SATS real-time data.
    Use the available tools to fetch flight and cargo information.
    """
)

# Mount tools
mcp.mount(tools_mcp)

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=SERVER_PORT
    )