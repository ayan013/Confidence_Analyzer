import shutil

from speechbrain.inference.classifiers import EncoderClassifier
import tempfile
import os
#import torchaudio

classifier = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa",
    savedir="pretrained/accent")

def detect_accent(audio_bytes: bytes):
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
            temp.write(audio_bytes)
            temp.flush()
            temp_path = temp.name

        audio_file = os.path.basename(temp_path)
        dest_dir = os.path.join(os.getcwd(), "audio")
        dest_path=os.path.join(dest_dir,audio_file)
        shutil.move(temp_path,dest_path)
        relative_path = os.path.relpath(dest_path, os.getcwd())
        out_prob, score, idx, label = classifier.classify_file(relative_path)

        return label, score.item()
    except Exception as e:
        print(f"Accent detection failed: {e}")
        return None
