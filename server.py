# server.py
from mcp.server.fastmcp import FastMCP
import asyncio
import os
from crawl4ai import AsyncWebCrawler

# Set environment variables for host and port
os.environ["MCP_HOST"] = "0.0.0.0"
# Use the PORT environment variable provided by Render
port = os.environ.get("PORT", "8000")
os.environ["MCP_PORT"] = port
print(f"Starting server on port {port}")

# Create an MCP server
mcp = FastMCP("Demo")

# Add a web crawler tool
@mcp.tool()
async def crawl_web(url: str) -> str:
    """Crawl a web page and return the content as markdown"""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        return result.markdown

# Add a health check tool
@mcp.tool()
def health_check() -> dict:
    """Check if the server is healthy"""
    return {"status": "healthy"}

def main():
    # Start the server
    mcp.run()

# Start the server
if __name__ == "__main__":
    main()