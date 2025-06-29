from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv

#load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()