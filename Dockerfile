FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY . /app/

# Create logs directory
RUN mkdir -p /app/logs && chmod 777 /app/logs

# Install Python dependencies and the package
RUN pip install --no-cache-dir "mcp[cli]" && \
    pip install --no-cache-dir -e .

# Set environment variables (can be overridden at runtime)
ENV ODOO_URL=""
ENV ODOO_DB=""
ENV ODOO_USERNAME=""
ENV ODOO_PASSWORD=""
ENV ODOO_TIMEOUT="30"
ENV ODOO_VERIFY_SSL="1"
ENV DEBUG="0"

# Make run_server.py executable
RUN chmod +x run_server.py

# Set stdout/stderr to unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run the custom MCP server script instead of the module
ENTRYPOINT ["python", "run_server.py"] 