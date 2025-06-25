from fastapi import APIRouter
from backend.endpoints import analyze

router = APIRouter()

router.include_router(analyze.router,prefix="/analyze",tags=["analyze_voice"])

