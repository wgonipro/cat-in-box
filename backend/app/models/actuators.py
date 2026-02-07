from .instruments import Instrument

class Actuator(Instrument):
    commands: dict = {}

    def __init__(self):
        super().__init__()
        for i in range(0, 10):
            self.command[i] = None

    def process_hour(self, hour: int):
        self.process_command(hour)
        self.process_state()

    def process_command(self, hour: int):
        command = self.commands.get(hour)
        if command is not None:
            print(f"Processing command for hour {hour}: {command}")
            result = self.handle(command)
            print(f"Command result: {result}")
        else:
            print(f"No command for hour {hour}.")

    def process_state(self):
        pass

    def handle(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def execute(self, *args, **kwargs) -> CommandResult:
            raise NotImplementedError("This method should be implemented by subclasses.")

