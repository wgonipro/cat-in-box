from app.models import MassScale, Feeder
from app.schemas import CommandResult

class CommandProcessor:
    command: str

    def __init__(self, command):
        self.command = command

        self.handler = {
            'scale': MassScale,
            'feeder': Feeder
        }

    def process(self) -> CommandResult:
        command_parts = self.command.split()

        if not command_parts:
            return CommandResult(success=False, message="No command provided")

        action = command_parts[0].lower()
        if action not in self.handler:
            return CommandResult(success=False, message=f"Unknown command: {action}")

        handler = self.handler[action]()
        print(f"Processing command: {self.command} with handler: {handler.name}")
        print(f"Command parts: {command_parts}")
        response = handler.execute(*command_parts[1:])

        return response



