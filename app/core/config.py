from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    This class loads configuration settings from environment variables
    Pydantic's BaseSettings does it by itself.
    """
    DATABASE_URL : str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env")

configs = Settings()
