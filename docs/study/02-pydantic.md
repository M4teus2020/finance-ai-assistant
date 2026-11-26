# 02. Pydantic

**Goal:** typed, validated domain models for `Account` and `Transaction`.

## Key concepts
- `BaseModel`: a class with typed fields that **validates and converts** input (`"10.50"` becomes `Decimal("10.50")`).
- **Money is `Decimal`, never `float`** (`0.1 + 0.2 != 0.3`). Same rule as `decimal` columns in MySQL.
- `Field(gt=0, max_length=...)`, `Literal["credit", "debit"]`, `date`, `UUID`, `Optional` / `X | None`.
- `model_validate(dict)`, `model_dump()`, `model_dump_json()`, `model_json_schema()` (this schema is what you give the LLM later).
- `@field_validator` / `@model_validator` for custom rules.
- In FastAPI, a model as parameter = request body validation; as `response_model` = output filter. Invalid input returns 422 automatically.

## PHP/Laravel bridge
- Pydantic model ~ Form Request rules + Eloquent `$casts` + API Resource, in one class.
- 422 with error list ~ Laravel validation exception.

## Exercise
1. `Account(id, name, balance: Decimal)` and `Transaction(id, account_id, date, description, amount: Decimal, type: Literal[...], category: str | None)`.
2. Script with Faker: 200 transactions, save to `data/transactions.json`.
3. `GET /transactions?start=2026-01-01&end=2026-01-31`, query params typed as `date`.

## Answer out loud
- Why `Decimal` and not `float` for money?
- What happens when the client sends `amount: "abc"`?
- What is `model_json_schema()` useful for in an LLM app?

## Links
- https://docs.pydantic.dev/latest/concepts/models/
- https://fastapi.tiangolo.com/tutorial/query-params/

## My notes
-
