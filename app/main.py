from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routes import health as health_routes
from app.api.routes import predict as predict_routes

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

    # CORS (ajusta origins cuando conectes tu Angular)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(health_routes.router, prefix=settings.API_PREFIX)
    app.include_router(predict_routes.router, prefix=settings.API_PREFIX)

    return app

app = create_app()
