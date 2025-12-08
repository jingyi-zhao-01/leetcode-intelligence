#!/usr/bin/env python3
"""Test the MCP client directly"""

import asyncio
from fastmcp import Client


async def test_client():
    client = Client("http://127.0.0.1:8000/mcp")

    try:
        async with client:
            # Test calling the get_submission_evolution tool
            result = await client.call_tool(
                "get_submission_evolution",
                {"title_slug": "best-time-to-buy-and-sell-stock"},
            )
            print(f"✅ MCP call successful!")
            print(f"Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_client())
