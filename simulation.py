import datetime as dt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image

def convert_str_to_time(string):
    array = string.split(":")
    if int(array[0]) > 8:
        time = dt.datetime(2024,9,25,hour=int(array[0]),minute=int(array[1]))
    else:
        time = dt.datetime(2024,9,26,hour=int(array[0]),minute=int(array[1]))
    return time

def convert_time_to_string(dt_object):
    return "{:02d}:{:02d}".format(dt_object.hour,dt_object.minute)

def run_day(box, cat, dispenser, extractor, dispenser_commands, extractor_commands):
    # matplotlib.use('TkAgg')

    step_interval = 15  # minutes per step
    min_per_day = 24*60 # minutes per day
    step_per_day = int(min_per_day/step_interval)
    time_start = dt.datetime(2024,9,25,hour=9,minute=0)
    time_interval = dt.timedelta(minutes=step_interval)
    time = time_start
    time_array = []
    box_mass = []
    hunger = []
    food = []
    waste = []
    disp = []
    extr = []
    result = None

    for step in range(step_per_day):
        time_array.append(time)

        if convert_time_to_string(time) in dispenser_commands[True]:
            dispenser.set_status(True)

        if convert_time_to_string(time) in dispenser_commands[False]:
            dispenser.set_status(False)

        if convert_time_to_string(time) in extractor_commands[True]:
            extractor.set_status(True)

        if convert_time_to_string(time) in extractor_commands[False]:
            extractor.set_status(False)

        if dispenser.status:
            box.add_food(dispenser.mass_flow_rate)

        if extractor.status:
            box.remove_waste(extractor.mass_flow_rate)

        # print(time.time(), dispenser.status, extractor.status, box.mass_total, box.mass_food, box.mass_waste, cat.food_consumed, cat.digestion)

        cat.metabolism()

        time = time + time_interval

        box_mass.append(box.mass_total)
        hunger.append(cat.hunger)
        food.append(box.mass_food)
        waste.append(box.mass_waste)
        disp.append(int(dispenser.status))
        extr.append(int(extractor.status))

    if cat.hunger < 0:
        result = "DEAD"

    # plt.rcdefaults()
    # fig, ax = plt.subplots(1, 3)
    # # ax2 = ax[0].twinx()
    # ax[0].plot(time_array, hunger)
    # ax[0].set_ylabel('Hunger Score')
    #
    # ax[1].plot(time_array, np.array([food, waste]).transpose(),
    #            label=['Food Mass', 'Waste Mass'])
    # ax[1].plot(time_array, extr, '--k')
    # ax[1].plot(time_array, disp, '--b')
    # ax[1].set_ylabel('Mass')
    # ax[1].set_ylim([0, 0.2])
    #
    # ax[2].plot(time_array, np.array(box_mass),
    #            label=['Box Mass'])
    # ax[2].plot(time_array, np.array(extr)*10, '--k')
    # ax[2].plot(time_array, np.array(disp)*10, '--b')
    # ax[2].set_ylabel('Mass')
    # ax[2].set_ylim([4.0, 4.8])
    # plt.xticks(rotation=70)
    # plt.legend()
    # plt.show()
    return result, time_array, box_mass

    # image = Image.open('mass_scale_reading.png').resize((200,200))
    # image.save("mass_scale_reading.png")