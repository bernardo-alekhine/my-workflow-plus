# Base build stage with virtualenv
FROM python:3.12-slim AS builder

WORKDIR /app

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Upgrade pip and create virtualenv
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip

# Install dependencies
COPY requirements/base-requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r base-requirements.txt

# Production stage
FROM python:3.12-slim

# Install curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user and app directory
RUN useradd -m -r appuser && \
    mkdir -p /app/logs && \
    chown -R appuser:appuser /app

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app/backend/:$PYTHONPATH"

# Copy Python dependencies from builder
COPY --from=builder --chown=appuser:appuser /opt/venv /opt/venv

COPY --chown=appuser:appuser . /app/

WORKDIR /app/backend

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Run gunicorn
CMD ["gunicorn", "-c", "gunicorn.conf.py"]
