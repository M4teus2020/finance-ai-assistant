# 01. Python, uv, FastAPI

**Goal:** a running API with `GET /health`, and knowing why each piece exists.

## Key concepts
- **uv:** package + venv + Python version manager, in one fast tool. `pyproject.toml` (like `composer.json`), `uv.lock` (like `composer.lock`), `.venv/` (like `vendor/`, but also holds the interpreter).
  - `uv add pkg`, `uv add --dev pkg`, `uv run <cmd>` (runs inside the venv, no `activate` needed), `uv sync`.
- **src layout:** code in `src/finance_ai_assistant/`. Import path is `finance_ai_assistant.main`, so uvicorn runs `finance_ai_assistant.main:app`.
- **ASGI:** the async standard for Python web servers. **uvicorn** is the server (like php-fpm), **FastAPI** is the framework (like Laravel).
- **FastAPI:** routes are decorated functions (`@app.get("/health")`). Return a dict, it becomes JSON.
- **`/docs`:** Swagger UI generated from your type hints and the OpenAPI schema (`/openapi.json`). No annotations, no docs.
- **async def vs def:** use `async def` when you await I/O (HTTP, DB). Plain `def` runs in a thread pool. Both work.

## PHP/Laravel bridge
| Laravel | Here |
|---|---|
| `composer require` | `uv add` |
| `php artisan serve` | `uv run uvicorn ... --reload` |
| `Route::get('/health', fn() => [...])` | `@app.get("/health")` + function |
| Scribe / L5-Swagger | built-in `/docs` |

## Exercise
1. Create `src/finance_ai_assistant/main.py` with `app` and `GET /health`.
2. Run it, open `/health` and `/docs`.
3. Bonus: add `GET /health` response model `{"status": str, "version": str}`, see how `/docs` changes.

## Answer out loud (1 min each)
- Why FastAPI and not Flask?
- What does uv do differently from pip?
- What is `/docs` and where does it come from?

## Links
- https://fastapi.tiangolo.com/tutorial/first-steps/
- https://docs.astral.sh/uv/guides/projects/

## My notes
-
