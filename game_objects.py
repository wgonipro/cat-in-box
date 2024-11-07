import numpy as np

class Box:
    def __init__(self, cat):
        self.max_mass = 20
        self.mass_total = cat.mass
        self.mass_food = 0
        self.mass_waste = 0

    def add_food(self, mass_flow_rate):
        self.mass_total += mass_flow_rate
        self.mass_food += mass_flow_rate

    def eat_food(self, mass_flow_rate):
        food_consumed = (mass_flow_rate + min(0,self.mass_food-mass_flow_rate))
        self.mass_food -= food_consumed
        return food_consumed

    def add_waste(self, mass_flow_rate):
        self.mass_waste += mass_flow_rate

    def remove_waste(self, mass_flow_rate):
        waste_removed = mass_flow_rate + min(0,self.mass_waste-mass_flow_rate)
        self.mass_total -= waste_removed
        self.mass_waste -= waste_removed

class Cat:
    def __init__(self):
        self.health = 100
        self.hunger = 100
        self.mass = 4.5
        self.diet = 0.180
        self.meals = 3
        self.box = None
        self.food_consumed = 0
        self.time_to_digest = 4
        self.digestion = 0

    def insert_in_box(self, box):
        self.box = box

    def get_mass(self):
        return(self.mass)

    def metabolism(self):
        self.hunger -= 1
        if self.hunger <= 100*(1 - 1/self.meals):
            self.food_consumed += self.box.eat_food(self.diet/self.meals)
            self.hunger += self.food_consumed/self.diet*100
            self.hunger = min(self.hunger, 100)

        if self.food_consumed > 0:
            self.digestion += 1

        if self.digestion > self.time_to_digest:
            self.box.add_waste(self.food_consumed)
            self.digestion = 0
            self.food_consumed = 0


class Input:
    def __init__(self, m_dot):
        self.status = False
        self.mass_flow_rate = m_dot

    def toggle(self):
        self.status = not self.status

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_status_str(self):
        output_dict = {False: "Closed",
                       True: "Open"}
        return output_dict[self.status]

# class Sensor()
