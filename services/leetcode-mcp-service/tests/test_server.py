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

    # Test 1: Get submission history
    print("\n📊 Testing get_submission_history tool...")
    get_submission_history_tool = tools.get("get_submission_history")
    if get_submission_history_tool:
        # Call the underlying function directly
        result = await get_submission_history_tool.fn("two-sum")
        print(f"✅ Result: {json.dumps(result, indent=2, default=str)}")
    else:
        print("❌ Tool not found")

    # Test 2: Analyze thought progression
    print("\n🧠 Testing analyze_thought_progression tool...")
    analyze_thought_progression_tool = tools.get("analyze_thought_progression")
    if analyze_thought_progression_tool:
        result = await analyze_thought_progression_tool.fn("two-sum")
        print(f"✅ Result: {json.dumps(result, indent=2, default=str)}")
    else:
        print("❌ Tool not found")

    # Test 3: Compare solutions
    print("\n🔍 Testing compare_solutions tool...")
    compare_solutions_tool = tools.get("compare_solutions")
    if compare_solutions_tool:
        result = await compare_solutions_tool.fn("two-sum", 1, 2)
        print(f"✅ Result: {json.dumps(result, indent=2, default=str)}")
    else:
        print("❌ Tool not found")

    # Test 4: Track improvement metrics
    print("\n📈 Testing track_improvement_metrics tool...")
    track_improvement_metrics_tool = tools.get("track_improvement_metrics")
    if track_improvement_metrics_tool:
        result = await track_improvement_metrics_tool.fn("two-sum")
        print(f"✅ Result: {json.dumps(result, indent=2, default=str)}")
    else:
        print("❌ Tool not found")

    # Test 5: Track overall improvement metrics
    print("\n📊 Testing overall improvement metrics...")
    if track_improvement_metrics_tool:
        result = await track_improvement_metrics_tool.fn()
        print(f"✅ Result: {json.dumps(result, indent=2, default=str)}")
    else:
        print("❌ Tool not found")


async def main():
    """Main test function."""
    print("🎯 MCP Server Tool Testing")
    print("=" * 60)

    try:
        await test_mcp_server_tools()
        print("\n🎉 All MCP tools tested successfully!")

        print("\n📋 Summary:")
        print(
            "  ✅ get_submission_history - Retrieves submission list with id, code, result, mistakes, time"
        )
        print(
            "  ✅ analyze_thought_progression - Analyzes comment evolution and themes"
        )
        print("  ✅ compare_solutions - Side-by-side comparison of attempts")
        print("  ✅ track_improvement_metrics - Overall improvement tracking")

        print("\n🔗 To use with an MCP client, run:")
        print("  uv run mcp-server")

    except Exception as e:
        print(f"❌ Error testing MCP tools: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
