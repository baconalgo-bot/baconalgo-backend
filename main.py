from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="BaconAlgo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    return {"message": "BaconAlgo API LIVE!", "endpoints": ["/api/scanner/scan"]}

@app.post("/api/scanner/scan")
async def scan():
    signals = [
        {"ticker": "GOOGL", "timeframe": "1D", "direction": "LONG", "score": 98, "entry": 142.50, "target": 148.20, "stop": 140.10, "grade": "LEGENDARY"},
        {"ticker": "QQQ", "timeframe": "4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVLEGENDARY"},
        {"ticker": "TSLA", "timeframe": "1D", "direction": "LONG", "score": 87, "entry": 248.90, "target": 262.40, "stop": 245.00, "grade": "EPIC"},
        {"ticker": "AAPL", "timeframe": "1H", "direction": "LONG", "score": 95, "entry": 195.20, "target": 202.10, "stop": 192.80, "grade": "LEGENDARY"}
    ]
    return {"success": True, "signals": signals}

@app.post("/api/trading/ibkr/connect")
async def ibkr(mode: str = "paper"):
    return {"success": True, "status": "IBKR " + mode.upper() + " connected"}

@app.post("/api/trading/bitget/connect")
async def bitget(mode: str = "demo"):
    return {"success": True, "status": "Bitget " + mode.upper() + " connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
