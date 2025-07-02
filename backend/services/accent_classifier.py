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
        #print(f"temp_path:- {temp_path}",flush=True)
        dest_dir = os.path.join(os.getcwd(), "audio")
        #print(f"Dest: {dest_dir}",flush=True)
        dest_path=os.path.join(dest_dir,audio_file)
        shutil.move(temp_path,dest_path)
        #print(f"✅ Moved to: {dest_path}", flush=True)
        relative_path = os.path.relpath(dest_path, os.getcwd())
        #print(relative_path,flush=True)
        out_prob, score, idx, label = classifier.classify_file(relative_path)

        return label, score.item()
    except Exception as e:
        print(f"❌ Accent detection failed: {e}")
        return None
