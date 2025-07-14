import openai
from backend.core.config import settings
from langdetect import detect
import io

openai.api_key = settings.OPENAI_API_KEY

async def transcription(audio_bytes: bytes):
    try:
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav"
        transcript = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",
            response_format="verbose_json"  # enables language field
        )
        #print(dir(transcription),flush=True)
        detect_lang=str(transcript.language)
        print(f"Language: {detect_lang}",flush=True)
        if detect_lang != "english":
            print(f"Not english",flush=True)
            print(f"Lang:- {detect_lang}",flush=True)
            return None,detect_lang
        else:
            return transcript.text,"English"
    except Exception as e:
        return f"Transcription Failed : {e}"

