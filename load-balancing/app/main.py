from fastapi import FastAPI
import socket
import time
import asyncio
app = FastAPI()
hostname = socket.gethostname()


@app.get("/")
async def root():
    await asyncio.sleep(1)

    return {"server": hostname, "status": "busy",}
    
