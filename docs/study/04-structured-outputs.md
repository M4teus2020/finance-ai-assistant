# 04. Structured outputs

**Goal:** the LLM returns JSON that your code can trust, validated by Pydantic.

## Key concepts
- Free text is useless for code. You want `{"category": "groceries", "confidence": 0.9}`.
- Three levels, weakest to strongest:
  1. Ask for JSON in the prompt + parse (breaks often).
  2. **JSON mode** (`response_format={"type": "json_object"}`): valid JSON, any shape.
  3. **JSON Schema** (`response_format` with a schema, from `Model.model_json_schema()`): valid JSON in your shape. Check if the chosen NIM model supports it.
- **Always validate** with `Model.model_validate_json(text)`. On failure: retry once with the error in the prompt, then fail clearly.
- Constrain outputs: `Literal` for categories, so the model can't invent one.

## Exercise
1. `TransactionCategory(category: Literal[...], confidence: float)`.
2. `classify(transaction) -> TransactionCategory`.
3. `POST /transactions/{id}/classify`.
4. Try a weird description ("pix pro joão") and see what happens.

## Answer out loud
- Difference between JSON mode and JSON Schema mode?
- What do you do when the model returns invalid JSON?
- Why `Literal` for categories?

## Links
- https://platform.openai.com/docs/guides/structured-outputs
- https://docs.api.nvidia.com/nim/docs/structured-generation

## My notes
-
