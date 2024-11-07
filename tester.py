import simulation
import game_objects

dispenser = game_objects.Input(0.03)
extractor = game_objects.Input(0.20)
cat = game_objects.Cat()
box = game_objects.Box(cat)
cat.insert_in_box(box)

dispenser_commands = {
    True: ['10:00'],
    False: ['11:00'],
}

extractor_commands = {
    True: ['23:00'],
    False: ['24:00'],
}

simulation.run_day(box, cat, dispenser, extractor,  dispenser_commands, extractor_commands)