# src/backend/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from interfaces.routers.hello import router as hello_router # importa il router

app = FastAPI()

# Percorso statico
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(static_dir / "favicon.ico")

# Includi il router
app.include_router(hello_router)

@app.get("/")
def read_root():
    return {"status": "ok"}
