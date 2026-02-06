from fastapi import FastAPI
from app.services import CommandProcessor
from app.schemas import CommandInput

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Cat in Box. Type something to begin."}


@app.post("/command")
async def command(input: CommandInput):
    processor = CommandProcessor(command=input.text)
    result = processor.process()
    return {"response": f"{result.success}: {result.message}"}
