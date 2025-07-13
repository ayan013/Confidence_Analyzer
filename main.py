from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import analyze_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import logging.config
from backend.core.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.routing import APIRoute

@app.on_event("startup")
def show_routes():
    print("\n--- Registered Routes ---")
    for route in app.routes:
        try:
            print(f"{route.path} [{', '.join(route.methods)}]")
        except AttributeError:
            print(f"{route.path} [non-method route: {type(route)}]")

# Mount frontend folder as static
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Serve index.html at root URL
@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

app.include_router(analyze_router.router)

