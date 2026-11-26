# 01. Python, uv, FastAPI

**Objetivo:** uma API rodando com `GET /health`, sabendo por que cada peça existe.

## Conceitos-chave
- **uv:** gerenciador de pacotes + venv + versão do Python, numa ferramenta só e rápida. `pyproject.toml` (como o `composer.json`), `uv.lock` (como o `composer.lock`), `.venv/` (como o `vendor/`, mas guarda também o interpretador).
  - `uv add pkg`, `uv add --dev pkg`, `uv run <cmd>` (roda dentro do venv, sem precisar de `activate`), `uv sync`.
- **src layout:** o código fica em `src/finance_ai_assistant/`. O caminho de import é `finance_ai_assistant.main`, então o uvicorn roda `finance_ai_assistant.main:app`.
- **ASGI:** o padrão assíncrono dos servidores web em Python. O **uvicorn** é o servidor (como o php-fpm), o **FastAPI** é o framework (como o Laravel).
- **FastAPI:** rota é uma função com decorator (`@app.get("/health")`). Devolveu um dict, vira JSON.
- **`/docs`:** Swagger UI gerado a partir dos type hints e do schema OpenAPI (`/openapi.json`). Sem anotação de tipo, sem doc.
- **async def vs def:** use `async def` quando fizer `await` de I/O (HTTP, banco). `def` comum roda num pool de threads. Os dois funcionam.

## Ponte com PHP/Laravel
| Laravel | Aqui |
|---|---|
| `composer require` | `uv add` |
| `php artisan serve` | `uv run uvicorn ... --reload` |
| `Route::get('/health', fn() => [...])` | `@app.get("/health")` + função |
| Scribe / L5-Swagger | `/docs` já vem pronto |

## Exercício
1. Criar `src/finance_ai_assistant/main.py` com o `app` e o `GET /health`.
2. Rodar, abrir `/health` e `/docs`.
3. Bônus: dar ao `/health` um response model `{"status": str, "version": str}` e ver como o `/docs` muda.

## Responder em voz alta (1 min cada)
- Por que FastAPI e não Flask?
- O que o uv faz de diferente do pip?
- O que é o `/docs` e de onde ele sai?

## Links
- https://fastapi.tiangolo.com/pt/tutorial/first-steps/
- https://docs.astral.sh/uv/guides/projects/

## Minhas anotações
-
