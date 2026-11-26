# 03. Cliente de LLM

**Objetivo:** uma função pequena e confiável que chama o LLM e aguenta falhas.

## Checklist
- [ ] `uv add openai pydantic-settings`; `Settings` com `nim_api_key`, `nim_base_url`, `model`; chave no `.env`
- [ ] `llm/client.py`: `chat(messages) -> str` com timeout e retry com backoff (loop de retry escrito na mão antes de usar `tenacity`)
- [ ] `POST /chat {"message": "..."}` devolve a resposta
- [ ] Explicar em 1 min (perguntas abaixo)
- [ ] Minhas anotações
- [ ] Commit + push
- Dia ruim: pedir ao Claude para explicar o código da lição anterior e escrever 3 linhas nas anotações

## Conceitos-chave
- O **NVIDIA NIM** expõe uma API **compatível com a da OpenAI**: use o pacote `openai` com `base_url` + `api_key`. O mesmo código serve para vários provedores.
- **Formato de chat:** lista de mensagens `{"role": "system" | "user" | "assistant", "content": ...}`. O modelo não guarda estado (stateless): você manda o histórico toda vez.
- **Segredos:** chave no `.env`, carregada com `pydantic-settings` (`BaseSettings`). O `.env` está no `.gitignore`.
- **Timeout:** sempre definir. Chamada travada segura o worker.
- **Retry com backoff exponencial + jitter:** só em erro transitório (429 rate limit, 5xx, timeout). Nunca repetir 400/401.
- **Tokens:** custo e limite de contexto. Logar o `usage` da resposta.
- **Streaming:** os tokens chegam conforme são gerados (semana 2).

## Ponte com PHP/Laravel
- `BaseSettings` ~ `config()` + `env()`.
- Retry ~ `Http::retry(3, 100)`; timeout ~ `Http::timeout(10)`.

## Responder em voz alta
- Em quais erros você faz retry e em quais não? Por quê?
- Por que o modelo é "stateless" e o que isso muda no histórico do chat?
- Onde fica a chave da API e como você garante que ela nunca vai para o git?

## Links
- https://build.nvidia.com (modelos + chave)
- https://github.com/openai/openai-python
- https://docs.pydantic.dev/latest/concepts/pydantic_settings/

## Minhas anotações
-
