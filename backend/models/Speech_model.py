from pydantic import BaseModel

class SpeechModel(BaseModel):
    confidence : str
    speaking_rate: str
    filler_words: str
    accent: str
    personality: str
    tip: str