from .instruments import Instruments

class Sensors(Instruments):

    def read(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
