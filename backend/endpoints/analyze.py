from fastapi import UploadFile, APIRouter
from backend.models.Speech_model import SpeechModel
from backend.services.audio_conversion import audio_conversion

router = APIRouter()

@router.post(path="/",response_model=SpeechModel)
async def analyze_voice(file: UploadFile):
    audio_bytes = await file.read()
    if audio_bytes:
        return "audio received"
    else:
        return "Not received"
    #converted_audio = audio_conversion(audio_bytes)