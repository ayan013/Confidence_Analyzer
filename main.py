from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import analyze_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse



app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Mount frontend folder as static
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Serve index.html at root URL
@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

app.include_router(analyze_router.router)