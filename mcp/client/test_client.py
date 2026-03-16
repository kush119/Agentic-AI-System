import asyncio
from agent import Agent


async def test():
    agent = Agent()

    print("\n🧪 Test 1 — Flight query")
    result = await agent.handle_query("What is the flight status?")
    print(result)

    print("\n🧪 Test 2 — Cargo query")
    result = await agent.handle_query("Where is my cargo?")
    print(result)

    print("\n🧪 Test 3 — Unknown query")
    result = await agent.handle_query("Hello there")
    print(result)


if __name__ == "__main__":
    asyncio.run(test())