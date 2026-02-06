# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cat-in-box is a web application with a Python FastAPI backend and a React TypeScript frontend.

## Development Commands

### Backend
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"        # install with dev dependencies

fastapi dev app/main.py        # run dev server (port 8000)
ruff check . && ruff format .  # lint and format
pytest                         # run tests
```

### Frontend
```bash
cd frontend
npm install                    # install dependencies

npm run dev                    # run dev server (port 5173)
npm run lint                   # lint
npm run test                   # run tests in watch mode
npm run test:run               # run tests once
```

### Running Both
Run backend on port 8000, frontend on port 5173. The Vite dev server proxies `/api/*` to the backend.

## Architecture

- **backend/**: FastAPI application (Python 3.14+)
  - `app/main.py`: FastAPI app entry point
  - Uses Pydantic for data validation
- **frontend/**: React TypeScript application (Vite)
  - Uses Chakra UI for components
  - Vitest + React Testing Library for tests
  - Vite proxies `/api/*` requests to backend
- **docker-compose.yml**: Container orchestration
