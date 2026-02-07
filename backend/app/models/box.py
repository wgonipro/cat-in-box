from dataclasses import dataclass

class Box:
    contents: list = []
    food_mass: int = 0

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)
        else:
            print(f"Item '{item}' not found in the box.")
