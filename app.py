from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.resources.health_check import health_router


def create_app():
    app = FastAPI()
    app.include_router(health_router)
    return app
