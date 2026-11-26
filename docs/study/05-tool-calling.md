# 05. Tool calling

**Objetivo:** o LLM decide chamar `get_balance(account_id)`, o seu código executa e o LLM responde com o resultado.

## Conceitos-chave
- Você manda `tools=[{name, description, parameters (JSON Schema)}]`. O modelo **não executa nada**: ele devolve um `tool_call` com nome + argumentos.
- **O loop:** mensagem do usuário -> modelo devolve tool_call -> você roda a função -> adiciona `{"role": "tool", ...}` -> chama o modelo de novo -> resposta final.
- **Validar os argumentos** com Pydantic antes de rodar. O modelo pode mandar tipo errado ou id que não existe.
- **Autorização fica no backend**, não no prompt: a tool confere se esse usuário pode ver essa conta (semana 2).
- Limitar o loop (no máximo N chamadas de tool) para não girar para sempre.
- O `description` da tool é um prompt: seja preciso sobre quando usar.

## Ponte com o que você já faz
O Brain já faz isso via MCP. Aqui você escreve o loop na mão, para entender o que o MCP e os frameworks de agente escondem.

## Exercício
1. `tools/balance.py`: `get_balance(account_id: str) -> Decimal` sobre os dados fake.
2. Schema da tool (tente gerar a partir de um model Pydantic).
3. `POST /chat` trata o loop. Pergunte "qual o saldo da conta X?".

## Responder em voz alta
- Quem executa a tool, o modelo ou o seu código?
- Por que validar os argumentos da tool?
- Onde você garante que um usuário não lê o saldo de outro?

## Links
- https://platform.openai.com/docs/guides/function-calling
- https://docs.api.nvidia.com/nim/docs/function-calling

## Minhas anotações
-
