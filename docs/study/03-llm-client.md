# 03. LLM client

**Goal:** a small, reliable function that calls an LLM and survives failures.

## Key concepts
- **NVIDIA NIM** exposes an **OpenAI-compatible** API: use the `openai` package with `base_url` + `api_key`. Same code works for many providers.
- **Chat format:** list of messages `{"role": "system" | "user" | "assistant", "content": ...}`. The model is stateless: you send the history every time.
- **Secrets:** key in `.env`, loaded with `pydantic-settings` (`BaseSettings`). `.env` is in `.gitignore`.
- **Timeouts:** always set one. A hung call blocks your worker.
- **Retry with exponential backoff + jitter:** only on transient errors (429 rate limit, 5xx, timeout). Never retry 400/401.
- **Tokens:** cost and context limit. Log `usage` from the response.
- **Streaming:** tokens arrive as they are generated (week 2).

## PHP/Laravel bridge
- `BaseSettings` ~ `config()` + `env()`.
- Retry ~ `Http::retry(3, 100)`; timeout ~ `Http::timeout(10)`.

## Exercise
1. `uv add openai pydantic-settings`. `Settings` with `nim_api_key`, `nim_base_url`, `model`.
2. `llm/client.py`: `chat(messages) -> str` with timeout and retry (try writing the retry loop yourself before using `tenacity`).
3. `POST /chat {"message": "..."}` returns the answer.

## Answer out loud
- Which errors do you retry and which you don't? Why?
- Why is the model "stateless" and what does that mean for chat history?
- Where does the API key live and how do you guarantee it never hits git?

## Links
- https://build.nvidia.com (models + key)
- https://github.com/openai/openai-python
- https://docs.pydantic.dev/latest/concepts/pydantic_settings/

## My notes
-
