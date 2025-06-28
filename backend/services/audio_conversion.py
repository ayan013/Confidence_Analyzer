from pydub import AudioSegment
import tempfile

def audio_conversion(raw_bytes: bytes) -> bytes:
    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as webm_file:
        webm_file.write(raw_bytes)
        webm_path = webm_file.name

    audio = AudioSegment.from_file(webm_path, format="webm")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wav_file:
        audio.export(wav_file.name, format="wav")
        wav_path = wav_file.name

    with open(wav_path, "rb") as f:
        return f.read()
