# Production run (Docker)

Quick steps to run the FastAPI app in a production-like container locally.

Build the image:

```bash
docker build -t python-project:prod .
```

Run with Docker:

```bash
docker run --rm -p 8000:8000 python-project:prod
```

Or with docker-compose:

```bash
docker-compose up --build
```

API will be available at http://127.0.0.1:8000/

Notes:
- The image uses Gunicorn with Uvicorn workers, which is the common production pattern.
- For cloud or servers, run the container under a process manager or orchestration (systemd, Docker, Kubernetes).
- For local dev, keep using `uvicorn "151HelloWorldAPI:app" --reload`.
