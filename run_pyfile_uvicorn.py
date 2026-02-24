"""Run a Python file that defines a FastAPI `app` with Uvicorn.

Usage:
  python run_pyfile_uvicorn.py 151HelloWorldAPI.py --host 127.0.0.1 --port 8000

Notes:
- This loads the file by path (so you don't need to rename numbered files).
- Auto-reload (`--reload`) is not supported when loading modules this way.
"""
import argparse
import importlib.util
import os
import sys


def load_app_from_file(path: str):
    path = os.path.abspath(path)
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "app"):
        raise RuntimeError(f"No 'app' found in {path}")
    return module.app


def main():
    parser = argparse.ArgumentParser(description="Run a FastAPI app from a .py file using Uvicorn")
    parser.add_argument("file", help="Python file that defines `app` (e.g. 151HelloWorldAPI.py)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    args = parser.parse_args()

    try:
        app = load_app_from_file(args.file)
    except Exception as e:
        print("Error loading app:", e)
        sys.exit(1)

    import uvicorn

    print(f"Starting app from {args.file} on http://{args.host}:{args.port} (no reload)")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
