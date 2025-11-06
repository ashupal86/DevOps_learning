from fastapi import FastAPI
import socket
import asyncio

app = FastAPI()
hostname = socket.gethostname()
active_requests = 0  # simple in-memory counter



@app.middleware("http")
async def count_active_requests(request, call_next):
    global active_requests
    active_requests += 1
    try:
        response = await call_next(request)
        return response
    finally:
        active_requests -= 1

@app.get("/")
async def root():
    global active_requests
    await asyncio.sleep(1)  # simulate backend load
    return {
        "server": hostname,
        "active_requests": active_requests,
        "status": "processing",
    }
