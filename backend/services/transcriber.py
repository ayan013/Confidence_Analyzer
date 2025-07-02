import openai
from backend.core.config import settings
from langdetect import detect
import io

openai.api_key = settings.OPENAI_API_KEY

def transcription(audio_bytes: bytes):
    try:
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav"
        transcript = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
        #print(dir(transcription),flush=True)
        detect_lang=detect(transcript.text)
        if detect_lang != "en":
            print(f"Not english",flush=True)
            return None
        else:
            return transcript.text
    except Exception as e:
        return f"Transcription Failed : {e}"

