from fastmcp import Client
from config import MCP_SERVER_URL


class MCPClient:
    def __init__(self):
        self.server_url = MCP_SERVER_URL

    async def list_tools(self):
        async with Client(self.server_url) as client:
            return await client.list_tools()

    async def call_tool(self, tool_name: str, params: dict):
        async with Client(self.server_url) as client:
            return await client.call_tool(tool_name, params)
        