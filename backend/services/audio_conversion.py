from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError, CouldntEncodeError
import tempfile
import os


AudioSegment.converter = os.path.abspath("ffmpeg.exe")
AudioSegment.ffprobe   = "ffprobe.exe"

def audio_conversion(raw_bytes: bytes) -> bytes:
    try:
        with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as webm_file:
            webm_file.write(raw_bytes)
            webm_path = webm_file.name

        audio = AudioSegment.from_file(webm_path, format="webm")
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wav_file:
            audio.export(wav_file.name, format="wav")
            wav_path = wav_file.name

        with open(wav_path, "rb") as f:
            return f.read()
    except (CouldntDecodeError, CouldntEncodeError) as codec_error:
        print(f"❌ FFmpeg error during conversion: {codec_error}")
    except FileNotFoundError as fnf_error:
        print(f"❌ File not found: {fnf_error}")
    except PermissionError as perm_error:
        print(f"❌ Permission error: {perm_error}")
    except Exception as e:
        print(f"❌ Unexpected error during audio conversion: {e}")

    return None