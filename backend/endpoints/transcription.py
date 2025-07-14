from fastapi import APIRouter,UploadFile,File
from backend.services.transcriber import transcription

router = APIRouter()

async def transcription_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    text, lang = await transcription(audio_bytes)
    return {"transcription": text, "language": lang}