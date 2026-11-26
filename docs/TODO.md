# TODO

Pendências do **projeto** (código, repo, infra, README). O que é de estudo fica no checklist de cada lição em `lessons/`.

**Lição atual:** [01. Python, uv, FastAPI](lessons/01-python-uv-fastapi.md)

## Agora
- [ ] Push do commit pendente (`feat: health endpoint with router`)
- [ ] `pyproject.toml`: tirar o `[project.scripts]` (aponta para o `main()` que foi apagado)

## Fase 1 (até `v0.1`)
- [ ] `.env.example` com as variáveis sem valor (quando entrar o cliente de LLM)
- [ ] Pasta `data/` com as transações fake (decidir: commitar o JSON ou gerar pelo script)
- [ ] README em inglês: o que é, como rodar, exemplo de `curl`
- [ ] Organizar módulos: `api/`, `schemas/`, `services/`, `llm/`, `tools/` (criar cada um quando precisar)
- [ ] Tag `v0.1` + print do gráfico de contribuições

## Depois
- [ ] GitHub Actions rodando `pytest` a cada push
- [ ] Docker (fase 2, junto com o Postgres + pgvector)

## Backlog (ideias, não agora)
- (vazio)
