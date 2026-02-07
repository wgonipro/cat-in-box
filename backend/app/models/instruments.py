from dataclasses import dataclass
from app.schemas import CommandResult

@dataclass
class Instrument:
    name: str = "Generic Instrument"
    description: str = ""
    reliabiliy: float = 1.0  # Reliability score between 0 and 1

