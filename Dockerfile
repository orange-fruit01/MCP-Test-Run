# Use a Python base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port (default for FastMCP)
EXPOSE 8000

# Run your MCP server
CMD ["python", "server.py"]
