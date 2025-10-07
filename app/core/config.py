from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Demo FastAPI"
    APP_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"  # útil si luego quieres versionar: /api/v1

    # CORS: orígenes permitidos (desarrollo + producción)
    CORS_ORIGINS: list[str] = [
        "http://localhost:4200",           # Angular desarrollo
        "http://localhost:3000",           # Alternativo desarrollo
        "https://frontend-ae-rf.vercel.app",  # Producción Vercel
    ]

    class Config:
        env_file = ".env"

settings = Settings()
