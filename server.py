# server.py
from mcp.server.fastmcp import FastMCP
import asyncio
from crawl4ai import *

# Run "mcp dev first-mcp.py"

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

# Start the server
if __name__ == "__main__":
    mcp.run()