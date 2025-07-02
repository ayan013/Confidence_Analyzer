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
    if transcribed_audio is None:
        print("Please speak in English",flush=True)
        return f"Please speak in English"
    else:
        print(f"Transcription: {transcribed_audio}",flush=True)
        label, accent_score = detect_accent(converted_audio)
        if label and accent_score:
            print(f"Accent - {label} - {accent_score*100:.2f}%",flush=True)
        else:
            print("Analyze Failed",flush=True)
        return f"Successful"


