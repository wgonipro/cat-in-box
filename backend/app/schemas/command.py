from pydantic import BaseModel

class CommandInput(BaseModel):
    text: str

class CommandResult(BaseModel):
    success: bool
    message: str
