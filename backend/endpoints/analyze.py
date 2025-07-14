import logging

print("✅ analyze.py loaded")
from fastapi import UploadFile, APIRouter,File

from backend.models.Speech_model import SpeechModel
from backend.services.audio_conversion import audio_conversion

from backend.services.transcriber import transcription
from backend.services.accent_classifier import detect_accent
from backend.services.audio_features import extract_audio_features
from backend.services.scoring import score_all

router = APIRouter()

@router.post(path="/analyze")
async def analyze_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    converted_audio = audio_conversion(audio_bytes)
    transcribed_audio,lang = await transcription(converted_audio)
    audio_features = extract_audio_features(converted_audio,transcribed_audio)
    score = score_all(audio_features)
    if lang != "English":
        print(f"language detected: {lang}",flush=True)
        return {"lang": lang}
    else:
        print(f"Transcription: {transcribed_audio}",flush=True)
        #label, accent_score = detect_accent(converted_audio)
        #logging.info("accent received")
        return {
            "lang": lang,
            "transcription": transcribed_audio,
            #"accent": label,
            #"accent_score": round(accent_score * 100, 2),
            "filler_count": audio_features['filler_count'],
            "filler_words": audio_features['filler_words'],
            "wpm": audio_features['wpm'],
            "duration": audio_features['duration_sec']

        }


