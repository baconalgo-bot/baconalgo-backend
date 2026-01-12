from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="🥓 BaconAlgo API", version="1.0.0")

# CORS FIX POUR DASHBOARD
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:8000", "https://baconalgo.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Signal(BaseModel):
    ticker: str
    timeframe: str
    direction: str
    score: int
    entry: float
    target: float
    stop: float
    grade: str

@app.get("/")
async def root():
    return {"message": "🥓 BaconAlgo API LIVE!", "endpoints": ["/api/scanner/scan"]}

@app.post("/api/scanner/scan")
async def scan():
    signals = [
        {"ticker": "GOOGL", "timeframe": "1D", "direction": "LONG", "score
