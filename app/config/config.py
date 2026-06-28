from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    USER_NAME: str = "David"
    USER_EMAIL: str = "david@example.com"
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
