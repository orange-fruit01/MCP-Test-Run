# server.py
from mcp.server.fastmcp import FastMCP
import asyncio
from crawl4ai import AsyncWebCrawler

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

def main():
    import uvicorn
    uvicorn.run(mcp.app, host="0.0.0.0", port=8000)

# Start the server
if __name__ == "__main__":
    main()