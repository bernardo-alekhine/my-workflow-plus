# Base build stage with virtualenv
FROM python:3.12-slim AS base

WORKDIR /app

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app:$PYTHONPATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client && rm -rf /var/lib/apt/lists/*

# Upgrade pip and create virtualenv
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip


# Builder Stage
FROM base AS builder
COPY requirements/ /app/requirements/
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements/base-requirements.txt

# Tester stage
FROM builder AS tester
COPY . /app/
RUN pip install --no-cache-dir -r requirements/dev-requirements.txt
WORKDIR /app

# Production stage
FROM base AS production
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user and app directory
RUN useradd -m -r appuser && \
    mkdir -p /app/logs && \
    chown -R appuser:appuser /app

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder --chown=appuser:appuser /opt/venv /opt/venv

COPY --chown=appuser:appuser . /app/

# Switch to non-root user
USER appuser
WORKDIR /app/backend

# Expose port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

# Run gunicorn
CMD ["gunicorn", "-c", "gunicorn.conf.py"]
