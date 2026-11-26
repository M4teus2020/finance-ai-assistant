from fastapi import APIRouter

router = APIRouter()

@router.get("/health", name="Health Check", description="Check the health of the API")
def health() -> dict:
    return {"status": "ok" }