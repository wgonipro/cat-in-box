from app.schemas import CommandResult
from .actuators import Actuator
from dataclasses import dataclass
from enum import Enum
from .box import Box
from pprint import pprint

class FeederState(Enum):
    OPEN = "open"
    CLOSED = "closed"

class FeederCommand(Enum):
    OPEN = "open"
    CLOSE = "close"

@dataclass
class Feeder(Actuator):
    name: str = "Feeder"
    feed_rate: float = 1.0  # units of food per clock cycle
    state: str = "closed"  # can be "open" or "closed"

    def execute(self, *args, **kwargs) -> CommandResult:
        if len(args) == 0 and len(kwargs) == 0:
            return CommandResult(success=False, message="No command arguments provided.")
        
        command = None
        if len(args) > 0:
            command = args[0]
        elif "command" in kwargs:
            command = kwargs["command"]

        if command not in FeederCommand:
            return CommandResult(success=False, message=f"Invalid command: {command}. Valid commands are: {[c.value for c in FeederCommand]}")

        if args[1] != '@':
            return CommandResult(success=False, message=f"Invalid command format. Expected format: <command> @ <timestamp>")

        timestamp = int(args[2])

        if timestamp > 10 or timestamp < 0:
            return CommandResult(success=False, message=f"Invalid timestamp: {args[2]}. Timestamp must be between 0 and 10.")

        self.commands[args[2]] = command
        msg = f"Command '{command}' scheduled for hour {args[2]}."

        pprint(self.commands)

        return CommandResult(success=True, message=msg)

    def handle(self, command: FeederCommand):
        # alter box state based on command or state

        pass

    ## if feeder is open provide food, else do not provide food
    # def actuate(self, box: Box)
    #     if self.state == "open":
    #         self.dispense_food()

    # def dispense_food(self, box: Box):
    #     pass
