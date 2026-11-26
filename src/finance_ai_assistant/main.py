from fastapi import FastAPI
from finance_ai_assistant.api.health import router as health_router

app = FastAPI(title="Finance AI Assistant", version="0.1.0")

app.include_router(health_router, tags=["Health"])