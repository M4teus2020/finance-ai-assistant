# Roadmap

One project, four phases of 3 weeks. Each phase ends with a git tag and something visible (GitHub + LinkedIn).

**Pace:** 45 min per weekday. Bad day: 15 min (1 test, 1 README line, or ask Claude to explain yesterday's code) + 1 commit. Weekends free. 4 weeks without a miss: go to 1 h.

| Phase | Dates | Learn | Deliverable |
|---|---|---|---|
| 1. Python + LLM | 2026-11-26 to 2026-12-18 | FastAPI, Pydantic, LLM client (timeout, retry), structured outputs, tool calling, pytest | `v0.1`: API that classifies transactions and answers "what's my balance?" via a tool |
| Break | 2026-12-19 to 2027-01-04 | 15 min sessions, only if possible | nothing |
| 2. RAG | 2027-01-05 to 2027-01-23 | Ingestion, chunking, embeddings, pgvector, hybrid search, reranking, citing sources | `v0.2`: `POST /ask` answers about fake docs citing the source. 1st LinkedIn post |
| 3. Agents + MCP | 2027-01-26 to 2027-02-13 | LangGraph (state, nodes, conditional edges), human-in-the-loop, MCP server in Python, loop limits | `v0.3`: agent that investigates a suspicious transaction and asks before acting. 2nd post |
| 4. Eval + security + deploy | 2027-02-16 to 2027-03-06 | Eval dataset, RAG/agent metrics, LangSmith, prompt injection tests, backend authz, Docker on AWS, CI | `v1.0` live demo + metrics table in README. 3rd post |

## Phase 1 detail

- **Week 1:** health endpoint, `Account` / `Transaction` models + fake data, LLM client, structured output, first tool, tests, README.
- **Week 2:** streaming response, tool permissions (which account can see what), more tools (`list_transactions`, `get_spending_by_category`), module layout (`api/`, `llm/`, `tools/`, `models/`).
- **Week 3:** error paths and tests with mocked LLM, config via `pydantic-settings`, README with curl examples, tag `v0.1`.

## "Know how to talk about" (1 topic per phase, 30 min with Claude)

- Phase 1: agents vs deterministic workflows (cost, autonomy, reliability)
- Phase 2: RAG vs fine-tuning vs training
- Phase 3: model routing, semantic cache, smaller models
- Phase 4: Amazon Bedrock and managed inference

## Rules

- Review this roadmap at the end of each phase, never in the middle.
- Missed a whole week? Cut phase scope, never the habit. Do not restart from zero.
