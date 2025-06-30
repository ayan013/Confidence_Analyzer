from speechbrain.inference import EncoderClassifier
import tempfile
import os

classifier = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa"
)

def detect_accent(audio_bytes: bytes):
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
            temp.write(audio_bytes)
            temp.flush()
            out_prob, score, idx, label = classifier.classify_file(temp.name)
            os.remove(temp.name)
        return label, score.item()
    except Exception as e:
        print(f"❌ Accent detection failed: {e}")
        return "Unknown", 0.0