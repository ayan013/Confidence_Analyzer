from fastapi import APIRouter,UploadFile,File
from backend.services.fast_transcription import transcribe_wav

router = APIRouter()

@router.post(path="/faster-transcription")
async def transcription_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcribed_text = transcribe_wav(audio_bytes)
    return transcribed_text