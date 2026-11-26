# TODO

Toda sessão começa aqui. Uma sessão = um bloco. Marca, commit, push.

## Fase 1, semana 1

### Qui 26/11: primeira API
- [x] Repo público no GitHub + clone
- [x] `uv init` + `uv add fastapi uvicorn`
- [ ] Escrever você mesmo `src/finance_ai_assistant/main.py`: `app = FastAPI()` + `GET /health` devolvendo `{"status": "ok"}`
- [ ] Rodar: `uv run uvicorn finance_ai_assistant.main:app --reload`
- [ ] Abrir http://localhost:8000/health e http://localhost:8000/docs
- [ ] Explicar em 1 min: o que é o FastAPI e de onde sai o `/docs`
- [ ] Commit `feat: health endpoint` + push
- Estudo: `docs/study/01-python-uv-fastapi.md`
- Dia ruim (15 min): README de 3 linhas + commit

### Sex 27/11: models + dados fake
- [ ] Models Pydantic `Account` e `Transaction` (`Decimal` para dinheiro, `date`, `Literal` para o tipo)
- [ ] `uv add --dev faker`, script que gera 200 transações fake em `data/transactions.json`
- [ ] `GET /transactions?start=&end=` com filtro por data
- Estudo: `docs/study/02-pydantic.md`
- Dia ruim: só o model `Transaction` + commit

### Seg 30/11: cliente de LLM
- [ ] Chave do NIM no `.env`, lida com `pydantic-settings`
- [ ] Cliente com timeout, retry com backoff, tratamento de erro
- [ ] `POST /chat` que repassa uma mensagem
- Estudo: `docs/study/03-llm-client.md`
- Dia ruim: pedir ao Claude para explicar o código de sexta, escrever 3 linhas em "Minhas anotações"

### Ter 01/12: structured output
- [ ] LLM classifica uma transação em categoria, JSON validado pelo Pydantic
- Estudo: `docs/study/04-structured-outputs.md`
- Dia ruim: 1 teste do `Transaction`

### Qua 02/12: primeira tool
- [ ] Tool `get_balance(account_id)`, o LLM decide quando chamar
- Estudo: `docs/study/05-tool-calling.md`
- Dia ruim: assinatura da tool + docstring

### Qui 03/12: testes
- [ ] pytest: a tool, o parser do structured output, uma falha do LLM simulada (mock)
- Estudo: `docs/study/06-pytest.md`
- Dia ruim: 1 teste

### Sex 04/12: README
- [ ] README em inglês: o que é, como rodar, exemplo de `curl`
- [ ] Print do gráfico de contribuições
- Dia ruim: só o "How to run"

## Fase 1, semanas 2 e 3
Ver `ROADMAP.md`. Quebrar em sessões aqui na sexta 04/12.

## Backlog (ideias, não agora)
- (vazio)
