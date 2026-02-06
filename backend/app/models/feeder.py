from app.schemas import CommandResult
from .instruments import Instrument
from dataclasses import dataclass

@dataclass
class Feeder(Instrument):
    name: str = "Feeder"
    feed_rate: float = 0.0

    def execute(self, *args, **kwargs) -> CommandResult:
        print(f"{self.name} received command with arguments: {args} and keyword arguments: {kwargs}")
        if len(args) == 0 and len(kwargs) == 0:
            return CommandResult(success=False, message="No command arguments provided.")

        msg = f"Feeder {self.name} executing command with arguments: {args} and keyword arguments: {kwargs}"
        return CommandResult(success=True, message=msg)

    def feed(self, material):
        print(f"{self.name} is feeding {material} at a rate of {self.feed_rate} units per second.")
