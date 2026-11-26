# Roadmap

Um projeto, quatro fases de 3 semanas. Cada fase termina com uma tag no git e algo visível (GitHub + LinkedIn).

**Ritmo:** 45 min por dia útil. Dia ruim: 15 min (1 teste, 1 linha do README ou pedir ao Claude para explicar o código de ontem) + 1 commit. Fim de semana livre. 4 semanas sem furo: sobe para 1 h.

| Fase | Datas | Aprende | Entregável |
|---|---|---|---|
| 1. Python + LLM | 26/11/2026 a 18/12/2026 | FastAPI, Pydantic, cliente de LLM (timeout, retry), structured outputs, tool calling, pytest | `v0.1`: API que classifica transações e responde "qual meu saldo?" chamando uma tool |
| Pausa | 19/12/2026 a 04/01/2027 | Sessões de 15 min, só se der | nada |
| 2. RAG | 05/01/2027 a 23/01/2027 | Ingestão, chunking, embeddings, pgvector, busca híbrida, reranking, citar a fonte | `v0.2`: `POST /ask` responde sobre documentos fictícios citando a fonte. 1º post no LinkedIn |
| 3. Agentes + MCP | 26/01/2027 a 13/02/2027 | LangGraph (estado, nós, arestas condicionais), human-in-the-loop, servidor MCP em Python, limite de loops | `v0.3`: agente que investiga uma transação suspeita e pede confirmação antes de agir. 2º post |
| 4. Avaliação + segurança + deploy | 16/02/2027 a 06/03/2027 | Dataset de avaliação, métricas de RAG e agente, LangSmith, testes de prompt injection, autorização no backend, Docker na AWS, CI | `v1.0` no ar + tabela de métricas no README. 3º post |

## Fase 1 em detalhe

- **Semana 1:** endpoint de health, models `Account` / `Transaction` + dados fake, cliente de LLM, structured output, primeira tool, testes, README.
- **Semana 2:** resposta em streaming, permissões da tool (quem pode ver qual conta), mais tools (`list_transactions`, `get_spending_by_category`), organizar módulos (`api/`, `llm/`, `tools/`, `models/`).
- **Semana 3:** caminhos de erro e testes com LLM mockado, config com `pydantic-settings`, README com exemplos de curl, tag `v0.1`.

## "Saber falar" (1 tema por fase, 30 min com o Claude)

- Fase 1: agentes vs workflows determinísticos (custo, autonomia, confiabilidade)
- Fase 2: RAG vs fine-tuning vs treinamento
- Fase 3: model routing, cache semântico, modelos menores
- Fase 4: Amazon Bedrock e inferência gerenciada

## Regras

- Revisar este roadmap no fim de cada fase, nunca no meio.
- Furou uma semana inteira? Corta escopo da fase, nunca o hábito. Não recomeça do zero.
