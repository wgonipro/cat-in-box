from .instruments import Instrument

class Sensor(Instrument):

    def read(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
