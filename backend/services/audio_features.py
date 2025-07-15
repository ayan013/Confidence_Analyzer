import librosa.feature
import numpy as np
import io

FILLERS = {"um", "uh", "ah", "like", "you know", "i mean", "actually", "kind of"}

def extract_audio_features(audio_bytes: bytes, transcription: str):
    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
    total_time = librosa.get_duration(y=y, sr=sr)
    print(f"Total Time: {total_time}",flush=True)

    # Pitch features
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[magnitudes > np.median(magnitudes)]
    pitch_mean = np.mean(pitch_values) if pitch_values.size > 0 else 0
    pitch_var = np.var(pitch_values) if pitch_values.size > 0 else 0

    # Energy features
    rms = librosa.feature.rms(y=y)
    energy_mean = np.mean(rms) if rms.size > 0 else 0
    energy_var = np.var(rms) if rms.size > 0 else 0

    # Pause detection (based on silence between intervals)
    intervals = librosa.effects.split(y, top_db=25)
    pauses = 0
    last_end = 0
    for start, end in intervals:
        pause_dur = (start - last_end) / sr
        if pause_dur > 0.8:
            pauses += 1
        last_end = end

    # Filler word detection
    transcript = transcription.lower()
    filler_words = []
    filler_count = 0

    for filler in FILLERS:
        count = transcript.count(filler)
        if count > 0:
            filler_words.append((filler, count))
            filler_count += count


    # Words per minute (WPM)
    word_count = len(transcription.strip().split())
    wpm = round((word_count / total_time) * 60, 2) if total_time > 0 else 0

    return {
        "pitch_mean": round(pitch_mean, 2),
        "pitch_var": round(pitch_var, 4),
        "energy_mean": round(energy_mean, 4),
        "energy_var": round(energy_var, 6),
        "pause_count": pauses,
        "filler_count": filler_count,
        "filler_words": filler_words,
        "duration_sec": total_time,
        "wpm": wpm
    }
