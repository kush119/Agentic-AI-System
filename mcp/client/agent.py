from client import MCPClient


class Agent:
    def __init__(self):
        self.mcp = MCPClient()

    async def handle_query(self, user_query: str):
        """
        Very naive routing logic for now.
        Later this will be replaced by LLM tool selection.
        """

        if "flight" in user_query.lower():
            return await self.mcp.call_tool(
                "get_flight_status",
                {"flight_number": "SQ123"}
            )

        if "cargo" in user_query.lower():
            return await self.mcp.call_tool(
                "get_cargo_status",
                {"cargo_id": "CGO-456"}
            )

        return {
            "message": "I don't know which tool to call for this query yet."
        }
