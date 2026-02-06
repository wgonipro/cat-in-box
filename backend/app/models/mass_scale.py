from .instruments import Instrument

class MassScale(Instrument):
    mass: float

    def __init__(self, name):
        super().__init__(name)
        self.mass = 0.0

    def execute(self, *args, **kwargs):
        if 'mass' in kwargs:
            self.mass = kwargs['mass']
            print(f"Mass set to {self.mass} kg.")
        else:
            print("No mass provided. Mass remains unchanged.")
