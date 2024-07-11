from functools import lru_cache

from pydantic_settings import BaseSettings

from .consts import CONFIG_FILE

class Settings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    class Config:
        env_file = CONFIG_FILE


@lru_cache()
def get_settings():
    return Settings()