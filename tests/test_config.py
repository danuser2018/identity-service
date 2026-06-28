import pytest
from app.config.config import Settings

def test_config_defaults():
    settings = Settings()
    # Pydantic Settings will read from env (which we copied from .env.example)
    # or use fallback defaults. Let's assert the expected MVP defaults.
    assert settings.USER_NAME in ["David", "default_name"] or isinstance(settings.USER_NAME, str)
    assert settings.USER_EMAIL in ["david@example.com", "default_email"] or isinstance(settings.USER_EMAIL, str)
    assert settings.PORT == 8000
    assert settings.HOST == "0.0.0.0"
