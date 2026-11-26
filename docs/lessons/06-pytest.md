# 06. pytest

**Objetivo:** testes para a tool, para o parser do structured output e para uma falha do LLM, sem chamar o LLM de verdade.

## Checklist
- [ ] `uv add --dev pytest`
- [ ] `tests/test_balance.py`: conta conhecida devolve saldo conhecido; conta desconhecida levanta erro
- [ ] `tests/test_classify.py`: LLM fake com JSON válido -> parse ok; JSON inválido -> erro claro
- [ ] `tests/test_chat.py`: LLM dá timeout -> endpoint devolve 503, não 500
- [ ] Explicar em 1 min (perguntas abaixo)
- [ ] Minhas anotações
- [ ] Commit + push
- Dia ruim: 1 teste

## Conceitos-chave
- Teste = função com nome `test_*` usando `assert` puro. Roda com `uv run pytest`.
- **Fixtures** (`@pytest.fixture`): setup reaproveitável, injetado pelo nome do parâmetro.
- `@pytest.mark.parametrize`: o mesmo teste com várias entradas.
- **`TestClient` do FastAPI:** chama seus endpoints sem subir servidor.
- **Mockar o LLM** (`monkeypatch` ou `unittest.mock`): teste tem que ser rápido, grátis e determinístico. Checagem com o LLM real é **eval** (fase 4), não teste unitário.
- `app.dependency_overrides` troca uma dependência (como o cliente de LLM) nos testes.

## Ponte com PHP/Laravel
- Fixture ~ `setUp()` + factories. `TestClient` ~ `$this->getJson()`. Mock ~ `Http::fake()` / `Mockery`.

## Responder em voz alta
- Por que mockar o LLM em teste unitário?
- Qual a diferença entre teste e eval?
- O que é uma fixture?

## Links
- https://docs.pytest.org/en/stable/getting-started.html
- https://fastapi.tiangolo.com/pt/tutorial/testing/

## Minhas anotações
-
