from fastapi import APIRouter
from backend.endpoints.analyze import router as analyze_endpoint

print("✅ analyze_router loaded")
router = APIRouter(prefix="/analyze",tags=["Analyze Voice"])
router.include_router(analyze_endpoint)

