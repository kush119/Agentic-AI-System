import sys
from pathlib import Path

# ✅ Add mcp/client to PYTHONPATH
MCP_CLIENT_PATH = Path(__file__).resolve().parents[3] / "mcp" / "client"
sys.path.append(str(MCP_CLIENT_PATH))

from agent import Agent


class AgentService:
    def __init__(self):
        self.agent = Agent()

    async def process_query(self, query: str) -> dict:
        result = await self.agent.handle_query(query)

        # Normalize MCP result
        if hasattr(result, "data"):
            return result.data

        return result