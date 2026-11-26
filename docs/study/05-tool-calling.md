# 05. Tool calling

**Goal:** the LLM decides to call `get_balance(account_id)`, your code runs it, the LLM answers with the result.

## Key concepts
- You send `tools=[{name, description, parameters (JSON Schema)}]`. The model **does not run anything**: it returns a `tool_call` with name + arguments.
- **The loop:** user msg -> model returns tool_call -> you run the function -> append `{"role": "tool", ...}` -> call the model again -> final answer.
- **Validate arguments** with Pydantic before running. The model can send wrong types or ids that don't exist.
- **Authorization lives in the backend**, not in the prompt: the tool checks if this user can see this account (week 2).
- Limit the loop (max N tool calls) so it can't spin forever.
- The tool `description` is a prompt: be precise about when to use it.

## Bridge to what you already do
The Brain already does this with MCP. Here you write the loop by hand, so you understand what MCP and agent frameworks hide.

## Exercise
1. `tools/balance.py`: `get_balance(account_id: str) -> Decimal` over the fake data.
2. Tool schema (try generating it from a Pydantic model).
3. `POST /chat` handles the loop. Ask "what's the balance of account X?".

## Answer out loud
- Who executes the tool, the model or your code?
- Why validate tool arguments?
- Where do you enforce that a user can't read someone else's balance?

## Links
- https://platform.openai.com/docs/guides/function-calling
- https://docs.api.nvidia.com/nim/docs/function-calling

## My notes
-
