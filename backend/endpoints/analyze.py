print("✅ analyze.py loaded")
from fastapi import UploadFile, APIRouter,File
from fastapi.responses import StreamingResponse
from backend.models.Speech_model import SpeechModel
from backend.services.audio_conversion import audio_conversion
import io

router = APIRouter()

@router.post(path="/")
async def analyze_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    converted_audio = audio_conversion(audio_bytes)

