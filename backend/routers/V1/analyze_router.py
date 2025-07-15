from fastapi import APIRouter
from backend.endpoints.analyze import router as analyze_endpoint
from backend.endpoints.transcription import router as transcription_endpoint
from backend.endpoints.transcribe_faster import router as transcribe_faster_endpoint

print("✅ analyze_router loaded")
router = APIRouter(prefix="/V1",tags=["Analyze Voice"])
router.include_router(analyze_endpoint)
router.include_router(transcription_endpoint)
router.include_router(transcribe_faster_endpoint)

