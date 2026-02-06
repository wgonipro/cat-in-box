from fastapi import FastAPI
from app.services import CommandProcessor

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Cat in Box. Type something to begin."}


@app.post("/command")
async def command(input: CommandInput):
    # Simple echo for now - game logic will go here
    return {"response": f"You said: {input.text}"}
