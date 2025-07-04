from pydantic import BaseModel

class SpeechModel(BaseModel):
    confidence : str
    speaking_rate: str
    filler_words: str
    accent: str
    accent_score:float
    personality: str
    tip: str