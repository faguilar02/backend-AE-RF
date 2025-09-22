from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Demo FastAPI"
    APP_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"  # útil si luego quieres versionar: /api/v1

    # Configs futuras (CORS, DB, etc.)
    CORS_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
