import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Cricket AI Editor")

API_KEY = os.environ.get("CRICKET_API_KEY", "")

@app.get("/")
def home():
    return {
        "service": "Cricket AI Editor",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/status")
def status(x_api_key: str = Header(default="")):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {"status": "online"}
