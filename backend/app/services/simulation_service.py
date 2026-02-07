import datetime
import time
from app.models import Sensor, Actuator, Cat, Box

class SimulationService:
    sim_day: int = 1

    def simulate:
        print(f"Simulating day {self.sim_day}...")
        # TODO...
        self.sim_day += 1

    # TODO what is the right way to get sensors and actuators in here? Should we
    # pass them in as arguments? Or should we have a reference to the game
    # state?
    def simulate_day(self, sensors: list[Sensor], actuators: list[Actuator],
                     cat: Cat, box: Box):
        hours_in_day = 10 

        for hour in range(hours_in_day):
            print(f"Simulating hour {hour} of day {self.sim_day}...")

            # check actuators
            for actuator in actuators:
                actuator.process_command(hour)

            # read from sensors
            # push to UI
            for sensor in sensors:
                data = sensor.read()
                print(f"Sensor {sensor.name} read data: {data}")

            # process animal actions


        # return report
