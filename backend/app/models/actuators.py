from .instruments import Instrument

class Actuator(Instrument):
    def activate(self):
        print(f"{self.name} is activated.")

    def deactivate(self):
        print(f"{self.name} is deactivated.")

    def execute(self, *args, **kwargs) -> CommandResult:
            raise NotImplementedError("This method should be implemented by subclasses.")

