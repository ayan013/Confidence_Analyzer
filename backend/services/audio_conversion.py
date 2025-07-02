from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError, CouldntEncodeError
import tempfile
import os

#Manually specify path to ffmpeg and ffprobe executables
AudioSegment.converter = os.path.abspath("ffmpeg.exe")
AudioSegment.ffprobe   = "ffprobe.exe"

def audio_conversion(raw_bytes: bytes) -> bytes:
    webm_path, wav_path = None, None
    try:

        # Validate input bytes (optional but good practice)
        if not raw_bytes or len(raw_bytes) < 10:
            print("Invalid audio bytes.",flush=True)
            return None

        # Step 1: Write raw bytes to a temporary .webm file
        with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as webm_file:
            webm_file.write(raw_bytes)
            webm_path = webm_file.name

        # Step 2: Use pydub to decode the temporary .webm file
        audio = AudioSegment.from_file(webm_path, format="webm")

        # Step 3: Export the audio to a temporary .wav file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wav_file:
            audio.export(wav_file.name, format="wav")
            wav_path = wav_file.name
        #print(f"In Audio conversion file {wav_path}",flush=True)
        # Step 4: Read the .wav file bytes and return
        with open(wav_path, "rb") as f:
            file=f.read()

        return file


    except (CouldntDecodeError, CouldntEncodeError) as codec_error:
        print(  f"❌ FFmpeg error during conversion: {codec_error}")
    except FileNotFoundError as fnf_error:
        print(f"❌ File not found: {fnf_error}")
    except PermissionError as perm_error:
        print(f"❌ Permission error: {perm_error}")
    except Exception as e:
        print(f"❌ Unexpected error during audio conversion: {e}")

    finally:
        for path in (webm_path, wav_path):
            try:
                if path and os.path.exists(path):
                    os.remove(path)
            except Exception as cleanup_error:
                 print(f"⚠️ Temp cleanup failed for {path}: {cleanup_error}")
    return None

