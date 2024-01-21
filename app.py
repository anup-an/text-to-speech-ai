from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.resources.health_check import health_router
from src.resources.generate_audio import audio_router


def create_app():
    app = FastAPI()
    app.include_router(health_router)
    app.include_router(audio_router)
    return app
