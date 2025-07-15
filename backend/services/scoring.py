
def scale_0_to_10(value: float, min_val: float, max_val: float) -> int:
    value = max(min_val, min(max_val, value))
    scaled = 10 * (value - min_val) / (max_val - min_val)
    return round(scaled)


def score_fluency(pause_count: int, filler_count: int, duration_sec: float) -> int:
    pause_penalty = pause_count / max(1, duration_sec / 10)
    filler_penalty = filler_count / max(1, duration_sec / 10)
    score = 10 - (pause_penalty + filler_penalty) * 2
    return max(1, min(10, round(score)))


def score_clarity(pitch_var: float) -> int:
    if pitch_var < 0.01:
        return 3
    elif pitch_var < 0.02:
        return 5
    elif pitch_var < 0.05:
        return 8
    elif pitch_var < 0.1:
        return 6
    else:
        return 4


def score_emotion(pitch_var: float, energy_var: float) -> int:
    score = (pitch_var * 50 + energy_var * 3000)  # Heuristic combo
    return scale_0_to_10(score, 0.5, 6.0)


def score_confidence(wpm: float, pause_count: int, duration_sec: float) -> int:
    rate_score = scale_0_to_10(wpm, 80, 170)
    pause_penalty = pause_count / max(1, duration_sec / 10)
    return max(1, min(10, round(rate_score - pause_penalty * 2)))


def score_all(audio_features: dict) -> dict:
    return {
        "fluency": score_fluency(
            audio_features["pause_count"],
            audio_features["filler_count"],
            audio_features["duration_sec"]
        ),
        "clarity": score_clarity(audio_features["pitch_var"]),
        "emotion": score_emotion(
            audio_features["pitch_var"],
            audio_features["energy_var"]
        ),
        "confidence": score_confidence(
            audio_features["wpm"],
            audio_features["pause_count"],
            audio_features["duration_sec"]
        )
    }
