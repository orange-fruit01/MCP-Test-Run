# MCP Service

This is a Model Control Protocol (MCP) service that provides tools for Cursor and Claude applications.

## Connecting to the Service

### For Cursor Users

1. Open Cursor
2. Go to Settings > AI > Advanced
3. Under "MCP Endpoint", enter: `https://your-render-url.onrender.com`
4. Save settings and restart Cursor

### For Claude App Users

1. Open Claude App
2. Go to Settings > Advanced
3. Under "MCP Connection", enter: `https://your-render-url.onrender.com`
4. Save settings

## Available Tools

- **Web Crawler**: Crawls web pages and returns content as markdown

## Deployment

This service is deployed on Render.com as a Docker container. The service is accessible at:

```
https://your-render-url.onrender.com
```

Replace `your-render-url.onrender.com` with the actual URL provided by Render after deployment.

## Environment Variables

- `MCP_HOST`: Host to bind the server (default: 0.0.0.0)
- `MCP_PORT`: Port to bind the server (default: 8000)

## Monitoring

A health endpoint is available at `/health` for monitoring the service status. 

