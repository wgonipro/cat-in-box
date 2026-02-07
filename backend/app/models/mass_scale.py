import random
from .sensors import Sensor

class MassScale(Sensor):
    mass: float

    def __init__(self, name):
        super().__init__(name)
        self.mass = 0.0

    def read(self):
        self.mass = random.uniform(0.0, 100.0)  # Simulate reading mass from the scale
        return self.mass

