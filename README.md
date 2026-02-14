# BorgCal Scaffold

This repository now includes a runnable BorgCal scaffold:
- `frontend/` static web UI (starter)
- `backend/` FastAPI service (starter)
- `infra/nginx/default.conf` reverse proxy config
- `docker-compose.yml` to run all services

## Quick start
1. Copy `.env.example` to `.env`
2. Run:
   ```bash
   docker compose up --build
   ```
3. Open app at `http://localhost:8080`
4. API health at `http://localhost:8080/api/health`

## Notes
- This is an MVP scaffold for iterative implementation.
- It already supports one mood entry per date via `PUT /api/moods/{day}`.
