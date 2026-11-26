# 04. Structured outputs

**Objetivo:** o LLM devolve um JSON em que o seu código pode confiar, validado pelo Pydantic.

## Checklist
- [ ] `TransactionCategory(category: Literal[...], confidence: float)`
- [ ] `classify(transaction) -> TransactionCategory`, JSON validado pelo Pydantic
- [ ] `POST /transactions/{id}/classify`
- [ ] Testar uma descrição estranha ("pix pro joão") e ver o que acontece
- [ ] Explicar em 1 min (perguntas abaixo)
- [ ] Minhas anotações
- [ ] Commit + push
- Dia ruim: 1 teste do `Transaction`

## Conceitos-chave
- Texto livre não serve para código. Você quer `{"category": "groceries", "confidence": 0.9}`.
- Três níveis, do mais fraco ao mais forte:
  1. Pedir JSON no prompt + fazer parse (quebra com frequência).
  2. **JSON mode** (`response_format={"type": "json_object"}`): JSON válido, formato qualquer.
  3. **JSON Schema** (`response_format` com schema, vindo do `Model.model_json_schema()`): JSON válido no SEU formato. Conferir se o modelo escolhido no NIM suporta.
- **Sempre validar** com `Model.model_validate_json(text)`. Se falhar: tentar de novo uma vez mandando o erro no prompt, depois falhar com erro claro.
- Restringir a saída: `Literal` nas categorias, para o modelo não inventar uma.

## Responder em voz alta
- Qual a diferença entre JSON mode e JSON Schema?
- O que você faz quando o modelo devolve JSON inválido?
- Por que `Literal` nas categorias?

## Links
- https://platform.openai.com/docs/guides/structured-outputs
- https://docs.api.nvidia.com/nim/docs/structured-generation

## Minhas anotações
-
