import datetime as dt
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

    if cat.hunger < 0:
        result = "DEAD"

    # plt.rc('axes',edgecolor='#FFCC00')
    # plt.rc('xtick', color='#FFCC00')
    # plt.rc('ytick', color='#FFCC00')
    # plt.rc('font', family='courier')
    # plt.rc('font', size='7')
    #
    # fig, ax = plt.subplots()
    # ax.plot(time_array, box_mass, '-', color='#33FF00')
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.set_facecolor((0,0,0))
    # fig.patch.set_facecolor((0,0,0))
    #
    # plt.xticks(rotation=70)
    # plt.grid(color='#FFCC00', alpha=0.8, linestyle='--')
    # #plt.xlabel('Time', color='#FFCC00')
    # plt.ylabel('Mass (kg)', color='#FFCC00')
    # fig.set_size_inches(5, 5)
    # plt.savefig('mass_scale_reading.png',bbox_inches='tight',dpi=100)

    return result, time_array, box_mass

    # image = Image.open('mass_scale_reading.png').resize((200,200))
    # image.save("mass_scale_reading.png")