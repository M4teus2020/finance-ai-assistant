# 06. pytest

**Goal:** tests for the tool, the structured output parser and an LLM failure, without calling the real LLM.

## Key concepts
- Test = function named `test_*` with plain `assert`. Run with `uv run pytest`.
- **Fixtures** (`@pytest.fixture`): reusable setup, injected by parameter name.
- `@pytest.mark.parametrize`: same test, many inputs.
- **FastAPI `TestClient`:** calls your endpoints in-process.
- **Mock the LLM** (`monkeypatch` or `unittest.mock`): tests must be fast, free and deterministic. Real-LLM checks are **evals** (phase 4), not unit tests.
- `app.dependency_overrides` swaps a dependency (like the LLM client) in tests.

## PHP/Laravel bridge
- Fixture ~ `setUp()` + factories. `TestClient` ~ `$this->getJson()`. Mock ~ `Http::fake()` / `Mockery`.

## Exercise
1. `uv add --dev pytest`. `tests/test_balance.py`: known account returns known balance; unknown account raises.
2. `tests/test_classify.py`: fake LLM returns valid JSON -> parsed; invalid JSON -> clear error.
3. `tests/test_chat.py`: LLM times out -> endpoint returns 503, not 500.

## Answer out loud
- Why mock the LLM in unit tests?
- Difference between a test and an eval?
- What is a fixture?

## Links
- https://docs.pytest.org/en/stable/getting-started.html
- https://fastapi.tiangolo.com/tutorial/testing/

## My notes
-
