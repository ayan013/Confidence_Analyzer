from faster_whisper import WhisperModel
import tempfile
import os
import time

start = time.time()
# Set up the model only once — reuse across calls
MODEL_SIZE = "base"  # or "tiny"
DEVICE = "cuda"      # or "cpu"
COMPUTE_TYPE = "int8_float16" if DEVICE == "cuda" else "int8"

# Load model at module level
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

def transcribe_wav(wav_bytes:bytes) -> dict:
    """
    Transcribes a 16kHz mono .wav file using faster-whisper.

    Args:
        wav_bytes: Path to the .wav audio file.

    Returns:
        dict: Transcription output with duration, language, and full text.
    """
    # Save bytes to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
        tmp_wav.write(wav_bytes)
        tmp_wav.flush()
        wav_path = tmp_wav.name

    try:

        segments, info = model.transcribe(wav_path, beam_size=1, language="en")

        transcription = "".join([segment.text for segment in segments])
        end = time.time()
        return {
            "duration": info.duration,
            "language": info.language,
            "transcription": transcription.strip(),
            "processing_time_sec": round(end - start, 4)
        }
    finally:
        os.remove(wav_path)
