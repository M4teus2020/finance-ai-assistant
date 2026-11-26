# 02. Pydantic

**Objetivo:** models de domínio tipados e validados para `Account` e `Transaction`.

## Conceitos-chave
- `BaseModel`: classe com campos tipados que **valida e converte** a entrada (`"10.50"` vira `Decimal("10.50")`).
- **Dinheiro é `Decimal`, nunca `float`** (`0.1 + 0.2 != 0.3`). Mesma regra da coluna `decimal` no MySQL.
- `Field(gt=0, max_length=...)`, `Literal["credit", "debit"]`, `date`, `UUID`, `Optional` / `X | None`.
- `model_validate(dict)`, `model_dump()`, `model_dump_json()`, `model_json_schema()` (esse schema é o que você vai passar para o LLM depois).
- `@field_validator` / `@model_validator` para regras próprias.
- No FastAPI, model como parâmetro = validação do body; como `response_model` = filtro da saída. Entrada inválida devolve 422 sozinho.

## Ponte com PHP/Laravel
- Model Pydantic ~ regras do Form Request + `$casts` do Eloquent + API Resource, numa classe só.
- 422 com lista de erros ~ a validation exception do Laravel.

## Exercício
1. `Account(id, name, balance: Decimal)` e `Transaction(id, account_id, date, description, amount: Decimal, type: Literal[...], category: str | None)`.
2. Script com Faker: 200 transações, salvar em `data/transactions.json`.
3. `GET /transactions?start=2026-01-01&end=2026-01-31`, com os query params tipados como `date`.

## Responder em voz alta
- Por que `Decimal` e não `float` para dinheiro?
- O que acontece quando o cliente manda `amount: "abc"`?
- Para que serve o `model_json_schema()` num app com LLM?

## Links
- https://docs.pydantic.dev/latest/concepts/models/
- https://fastapi.tiangolo.com/pt/tutorial/query-params/

## Minhas anotações
-
