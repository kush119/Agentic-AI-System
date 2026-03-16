import asyncio
from fastmcp import Client

async def test():
    async with Client("http://localhost:9000/mcp/") as client:
        
        # List all tools
        tools = await client.list_tools()
        print("\n✅ Available Tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        # Call get_flight_status
        print("\n✅ Calling get_flight_status...")
        result = await client.call_tool(
            "get_flight_status",
            {"flight_number": "SQ123"}
        )
        print(f"  Result: {result}")

        # Call get_cargo_status
        print("\n✅ Calling get_cargo_status...")
        result = await client.call_tool(
            "get_cargo_status",
            {"cargo_id": "CGO-456"}
        )
        print(f"  Result: {result}")

if __name__ == "__main__":
    asyncio.run(test())