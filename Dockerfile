FROM python:3.11-slim

WORKDIR /app

# Install build/runtime deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY . /app

# Use Gunicorn with Uvicorn workers for production
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "hello_world_api:app", "--bind", "0.0.0.0:8000", "--workers", "4", "--log-level", "info"]
