from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random
from datetime import datetime
import os

app = FastAPI(title="🥓 BaconAlgo API", version="1.0.0")

# CORS pour ton frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://baconalgo.com", "https://baconalgo.vercel.app", "*"],
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
    confluence: int

@app.get("/")
async def root():
    return {
        "message": "🥓 BaconAlgo API LIVE!",
        "status": "🚀 Ready to scan!",
        "endpoints": ["/api/scanner/scan", "/api/signals", "/api/trading/ibkr/connect"]
    }

@app.post("/api/scanner/scan")
async def scan_markets():
    """Génère signaux mock parfaits pour ton dashboard"""
    signals = [
        Signal(
            ticker="GOOGL",
            timeframe="1D",
            direction="LONG",
            score=98,
            entry=142.50,
            target=148.20,
            stop=140.10,
            grade="LEGENDARY",
            confluence=5
        ),
        Signal(
            ticker="QQQ",
            timeframe="4H", 
            direction="SHORT",
            score=92,
            entry=412.80,
            target=398.50,
            stop=416.20,
            grade="LEGENDARY",
            confluence=4
        ),
        Signal(
            ticker="TSLA",
            timeframe="1D",
            direction="LONG",
            score=87,
            entry=248.90,
            target=262.40,
            stop=245.00,
            grade="EPIC",
            confluence=3
        ),
        Signal(
            ticker="AAPL",
            timeframe="1H",
            direction="LONG",
            score=95,
            entry=195.20,
            target=202.10,
            stop=192.80,
            grade="LEGENDARY",
            confluence=5
        )
    ]
    
    return {
        "success": True,
        "signals": [s.dict() for s in signa
