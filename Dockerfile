FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl && apt-get clean

COPY . .

# Set environment variables
ENV MCP_HOST=0.0.0.0
# PORT will be provided by Render

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${PORT:-8000}/mcp/tools/health_check || exit 1

# Expose the port (Render will set PORT env var)
EXPOSE ${PORT:-8000}

CMD ["python", "server.py"]