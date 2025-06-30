print("✅ analyze.py loaded")
from fastapi import UploadFile, APIRouter,File
from fastapi.responses import StreamingResponse
from backend.models.Speech_model import SpeechModel
from backend.services.audio_conversion import audio_conversion
import io
from backend.services.transcriber import transcription
from backend.services.accent_classifier import detect_accent

router = APIRouter()

@router.post(path="/")
async def analyze_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    converted_audio = audio_conversion(audio_bytes)
    transcribed_audio = transcription(converted_audio)
    label, accent_score = detect_accent(converted_audio)
    if label and accent_score:
        print(f"{label} - {accent_score}",flush=True)
    else:
        print("Failed",flush=True)
    return None
