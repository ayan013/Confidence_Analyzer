from fastapi import APIRouter
#from backend.endpoints import analyze

router = APIRouter(prefix="/analyze",tags=["Analyze Voice"])

from backend.endpoints import analyze

