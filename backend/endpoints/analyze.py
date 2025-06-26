from fastapi import APIRouter
from backend.routers.analyze_router import router

@router.get(path="/analyze")
async def analyze_voice():
    return None