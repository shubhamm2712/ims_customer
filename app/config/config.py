from functools import lru_cache

from pydantic_settings import BaseSettings

from .consts import CONFIG_FILE

class AuthSettings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    class Config:
        env_file = CONFIG_FILE
        extra = "ignore"

class CorsSettings(BaseSettings):
    origin: str 

    class Config:
        env_file = CONFIG_FILE
        extra = "ignore"

class DBSettings(BaseSettings):
    db_url: str

    class Config:
        env_file = CONFIG_FILE
        extra = "ignore"

@lru_cache()
def get_auth_settings():
    return AuthSettings()

@lru_cache()
def get_cors_settings():
    return CorsSettings()

@lru_cache()
def get_db_settings():
    return DBSettings()