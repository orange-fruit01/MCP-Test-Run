# server.py
from mcp.server.fastmcp import FastMCP
import asyncio
import os
from crawl4ai import AsyncWebCrawler
from fastapi import FastAPI

# Set environment variables for host and port
os.environ["MCP_HOST"] = "0.0.0.0"
os.environ["MCP_PORT"] = "8000"

# Create an MCP server
mcp = FastMCP("Demo")
app = mcp.app

# Add a health endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Add a web crawler tool
@mcp.tool()
async def crawl_web(url: str) -> str:
    """Crawl a web page and return the content as markdown"""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        return result.markdown

def main():
    # Use the default run method without parameters
    mcp.run()

# Start the server
if __name__ == "__main__":
    main()