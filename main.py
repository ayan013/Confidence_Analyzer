from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import analyze_router



app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router.router)