#!/usr/bin/env python3
"""
Test script that simulates MCP client interaction with our server.
This demonstrates how the MCP tools would be called.
"""

import asyncio
import json
import sys
import os

# Add project root to the Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)


async def test_mcp_server_tools():
    """Test the MCP server tools through the server process."""
    print("🚀 Testing MCP Server Tools")
    print("=" * 50)

    # We can't easily test the actual MCP protocol without a full client,
    # but we can test our functions directly by importing the actual function implementations

    # Import the MCP module and extract the actual functions from the tools
    from server import mcp, ensure_db_connected

    print("🔧 Ensuring database connection...")
    await ensure_db_connected()

    # Get the actual function from the MCP tool registry
    # For FastMCP, the tools are stored in the mcp object

    # Extract actual functions from the registered tools
    tools = await mcp.get_tools()  # This returns a dict already

    print(f"Available tools: {list(tools.keys())}")
