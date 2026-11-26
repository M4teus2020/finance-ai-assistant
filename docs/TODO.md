# TODO

Start every session here. One session = one block. Tick, commit, push.

## Phase 1, week 1

### Thu 2026-11-26: first API
- [x] Public repo on GitHub + clone
- [x] `uv init` + `uv add fastapi uvicorn`
- [ ] Write `src/finance_ai_assistant/main.py` yourself: `app = FastAPI()` + `GET /health` returning `{"status": "ok"}`
- [ ] Run: `uv run uvicorn finance_ai_assistant.main:app --reload`
- [ ] Open http://localhost:8000/health and http://localhost:8000/docs
- [ ] Explain in 1 min: what FastAPI is and where `/docs` comes from
- [ ] Commit `feat: health endpoint` + push
- Study: `docs/study/01-python-uv-fastapi.md`
- Bad day (15 min): README with 3 lines + commit

### Fri 2026-11-27: models + fake data
- [ ] Pydantic models `Account` and `Transaction` (`Decimal` for money, `date`, `Literal` for type)
- [ ] `uv add --dev faker`, script that generates 200 fake transactions into `data/transactions.json`
- [ ] `GET /transactions?start=&end=` with date filter
- Study: `docs/study/02-pydantic.md`
- Bad day: only `Transaction` model + commit

### Mon 2026-11-30: LLM client
- [ ] NIM key in `.env`, read it with `pydantic-settings`
- [ ] Client with timeout, retry with backoff, error handling
- [ ] `POST /chat` that forwards one message
- Study: `docs/study/03-llm-client.md`
- Bad day: ask Claude to explain Friday's code, write 3 lines in "My notes"

### Tue 2026-12-01: structured output
- [ ] LLM classifies a transaction into a category, JSON validated by Pydantic
- Study: `docs/study/04-structured-outputs.md`
- Bad day: 1 test for `Transaction`

### Wed 2026-12-02: first tool
- [ ] Tool `get_balance(account_id)`, the LLM decides when to call it
- Study: `docs/study/05-tool-calling.md`
- Bad day: tool signature + docstring

### Thu 2026-12-03: tests
- [ ] pytest: the tool, the structured output parser, a simulated LLM failure (mock)
- Study: `docs/study/06-pytest.md`
- Bad day: 1 test

### Fri 2026-12-04: README
- [ ] README in English: what it is, how to run, `curl` example
- [ ] Screenshot of the contributions graph
- Bad day: only "How to run"

## Phase 1, weeks 2 and 3
See `ROADMAP.md`. Break into sessions here on Friday 2026-12-04.

## Backlog (ideas, not now)
- (empty)
