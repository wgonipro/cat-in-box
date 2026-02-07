import asyncio
from fastapi import FastAPI, WebSocket
from app.services import CommandProcessor
from app.schemas import CommandInput
from app.models import MassScale

app = FastAPI()

mass_scale = MassScale(name="Primary Scale")


@app.get("/")
async def root():
    return {"message": "Welcome to Cat in Box. Type something to begin."}


@app.post("/command")
async def command(input: CommandInput):
    processor = CommandProcessor(command=input.text)
    result = processor.process()
    return {"response": f"{result.success}: {result.message}"}


@app.websocket("/ws/sensors")
async def sensor_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        for _ in range(10):
            reading = mass_scale.read()
            await websocket.send_json({"mass": reading})
            await asyncio.sleep(1)
        await websocket.close()
    except Exception:
        pass

