from pydantic.env_settings import Basesettings
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings(Basesettings):
    OPENAI_API_KEY: str
    CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()