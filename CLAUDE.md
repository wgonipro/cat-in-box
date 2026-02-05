# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cat-in-box is a web application with a Python FastAPI backend and a frontend (structure TBD).

## Development Commands

### Backend Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .           # install project + dependencies
pip install -e ".[dev]"    # include dev dependencies (pytest, ruff)
```

### Running the Backend
```bash
cd backend
fastapi dev app/main.py    # development server with hot reload
```

### Linting
```bash
cd backend
ruff check .               # check for issues
ruff check --fix .         # auto-fix issues
ruff format .              # format code
```

### Testing
```bash
cd backend
pytest                     # run all tests
pytest tests/test_foo.py   # run specific test file
pytest -k "test_name"      # run tests matching pattern
```

## Architecture

- **backend/**: FastAPI application (Python 3.14+)
  - `app/main.py`: FastAPI app entry point
  - Uses Pydantic for data validation
- **frontend/**: Frontend application (Dockerfile present, implementation TBD)
- **docker-compose.yml**: Container orchestration for local development
