import random, textwrap
from PIL import Image
import PySimpleGUI as sg
import game_objects
import simulation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import use as use_agg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

IMAGE_PATH="resources/images/"
FONT_PATH="resources/fonts/"

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
dialogue_width = 40
number = int(random.random()*10000)
intro_text = [
    "Hello, Employee #{}. Welcome to your new position here at Schrodinger "
    "Inc.!".format(number),

    "You have been entrusted with the care of Cheshire, our office cat.",

    "However, he's locked in this box. And, under no condition, are you "
    "permitted to look inside.*Box",

    "To interact with the box, you have access to this console. You can submit "
    "instructions for the day, and a report will be generated.*Console",

    "Currently, the console can control the caloric enrichment dispenser, and "
    "metabolic byproduct remover.*Dispenser",

    "The box has been set upon a mass scale. For your convenience, this data "
    "is connected to your terminal.*Scale",

    "It is up to you to ensure that Cheshire is alive. Good luck!",

    "Messages:*Commands"
]
intro_index = 0
image = Image.open(f"{IMAGE_PATH}box2.png").resize((200,200))
image.save(f"{IMAGE_PATH}box2_resized.png")
sg.theme('DarkBlack1')
sg.set_options(font=("Courier New", 12))
sg.set_options(text_color="#33FF00")
sg.set_options(button_color=('#FFCC00', sg.theme_background_color()))
sg.set_options(input_elements_background_color='#353935')
sg.set_options(input_text_color='#FFCC00')
sg.set_options(border_width=0)
sg.set_options(slider_border_width=0)
# sg.set_options(text_element_background_color='#000000')

plt.rc('axes',  edgecolor='#FFCC00')
plt.rc('xtick', color='#FFCC00')
plt.rc('ytick', color='#FFCC00')
plt.rc('font',  family='courier')
plt.rc('font',  size='9')

list_commands = ["DISPENSER-OPEN-TIME-10:00", "DISPENSER-CLOSE-TIME-11:00",
                 "EXTRACTOR-OPEN-TIME-23:00", "EXTRACTOR-CLOSE-TIME-23:30"]

list_commands = ["EXTRACTOR-OPEN-TIME-23:00", "EXTRACTOR-CLOSE-TIME-23:30"]

clock_string = 'DAY: {}     TIME: 09:00'
day = 1
static_info = sg.Column([[sg.Push(), sg.Image(f"{IMAGE_PATH}console_image_resized.png", key="image"), sg.Push()],
                        [sg.Text(textwrap.fill(intro_text[intro_index],dialogue_width), key='-dialogue-',
                        size=(dialogue_width,3))],
                        [sg.Text('CONSOLE>_', visible=False, key='console')],
                        [sg.Text(clock_string.format(day), visible=False, key='clock')],
                        [sg.Text('CONTROLS: DISPENSER, EXTRACTOR', visible=False, key='disp_status')],
                        [sg.Text('SENSORS: MASS1', visible=False, key='scale')],
                        ])

command_tab = sg.Tab('command_tab',[[sg.Text('COMMAND DISPENSER'),
                            sg.Combo(['OPEN','CLOSE'], key='-DISP_STATUS-', default_value='OPEN'),
                            sg.Text('WHEN'),
                            sg.Combo(['TIME', 'MASS1'], default_value='TIME', key='-DISP_WHEN-'),
                            sg.Text('READS'), sg.Input(default_text='', key='-DISP_VALUE-',size=(5,1)),
                            sg.Button("+", key='-DISP_ADD-')],
                           [sg.Text('COMMAND EXTRACTOR'),
                            sg.Combo(['OPEN','CLOSE'], key='-EXTR_STATUS-', default_value='OPEN'),
                            sg.Text('WHEN'),
                            sg.Combo(['TIME', 'MASS1'], default_value='TIME', key='-EXTR_WHEN-'),
                            sg.Text('READS'), sg.Input(default_text='', key='-EXTRVALUE-',size=(5,1)),
                            sg.Button("+", key='-EXTR_ADD-')],
                            [sg.Listbox(list_commands,size=(53,10), key='commandsList', select_mode=sg.SELECT_MODE_EXTENDED)],
                           [sg.Push(), sg.Button("Delete", key='-DELETE-'), sg.Submit()],
                           ])
report_tab = sg.Tab('report_tab',
                    [[sg.Graph((50, 50), (0, 0),
                               (50, 50), background_color='white', key='Graph1')]], visible=False, key='report')

variable_info = sg.Column([[sg.TabGroup([[command_tab, report_tab]])]
                            ],
                            visible=False,key="commands")

layout = [
          [static_info, sg.vtop(variable_info)],
          [sg.VPush()],
          [sg.Text('<ENTER>')],
          ]

window = sg.Window('Cat In A Box Game', layout, finalize=True)#, size=(WINDOW_WIDTH,WINDOW_WIDTH), finalize=True)
window.bind("<Escape>", "-ESCAPE-")
window.bind("<Return>", "-RETURN-")
graph1 = window['Graph1']

dispenser = game_objects.Input(0.03)
extractor = game_objects.Input(0.20)
cat = game_objects.Cat()
box = game_objects.Box(cat)
cat.insert_in_box(box)

def parse_commands(commands):
    disp_commands = {True: [], False: []}
    extr_commands = {True: [], False: []}
    for command in commands:
        if 'DISPENSER' in command:
            if 'OPEN' in command:
                disp_commands[True]  = command.split('-')[-1]
            elif 'CLOSE' in command:
                disp_commands[False] = command.split('-')[-1]
        elif 'EXTRACTOR' in command:
            if 'OPEN' in command:
                extr_commands[True]  = command.split('-')[-1]
            elif 'CLOSE' in command:
                extr_commands[False] = command.split('-')[-1]
    return disp_commands,extr_commands

def pack_figure(graph, figure):
    canvas = FigureCanvasTkAgg(figure, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)
    return plot_widget

def make_figure():
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.set_facecolor(sg.theme_background_color())
    fig.patch.set_facecolor(sg.theme_background_color())
    plt.xticks(rotation=70)
    plt.grid(color='#FFCC00', alpha=0.8, linestyle='--')
    plt.ylabel('Mass (kg)', color='#FFCC00')
    fig.set_size_inches(4, 3)
    plt.tight_layout()
    return fig, ax

use_agg('TkAgg')

trigger = None
while True:

    event, values = window.read()
    # current_message = intro_text[intro_index]
    # print(event, values)

    if event in (None, 'Exit', "-ESCAPE-"):
        break

    if event == "-DISP_ADD-":
        list_commands.append('DISPENSER-{}-{}-{}'.format(
            values['-DISP_STATUS-'],values['-DISP_WHEN-'],values['-DISP_VALUE-']))
        window['commandsList'].update(list_commands)
    elif event == "-EXTR_ADD-":
        list_commands.append('EXTRACTOR-{}-{}-{}'.format(
            values['-EXTR_STATUS-'],values['-EXTR_WHEN-'],values['-EXTR_VALUE-']))
        window['commandsList'].update(list_commands)
    elif event == "Submit":
        dispenser_commands, extractor_commands = parse_commands(list_commands)
        result, t, mass = simulation.run_day(box, cat, dispenser, extractor,  dispenser_commands, extractor_commands)
        # sg.popup(image="mass_scale_reading.png")
        fig1, ax1 = make_figure()
        pack_figure(graph1, fig1)
        window['report'].update(visible=True)
        window['report'].select()

        # for i in range(len(t)):
        #     ax1.plot(t[:i], mass[:i], '-', color='#33FF00')
        #     fig1.canvas.draw()
        #     time.sleep(0.1)

        ax1.plot(t, mass, '-', color='#33FF00')
        fig1.canvas.draw()


        day+=1
        window['clock'].update(clock_string.format(day))
        if result == "DEAD":
            window['image'].update(filename=f"{IMAGE_PATH}game_over_resized.png")
            intro_text.append("Messages: GAME OVER")
            window['commands'].update(visible=False)


    if event == "-RETURN-":
        intro_index = min(intro_index+1, len(intro_text))
        if intro_index<len(intro_text):
            current_message = intro_text[intro_index]
            if "*" in current_message:
                current_message, trigger = current_message.split('*')
            window["-dialogue-"].update(current_message)

    if trigger == "Box":
        window["image"].update(filename=f"{IMAGE_PATH}box2_resized.png")
    elif trigger == "Console":
        window["console"].update(visible=True)
        window["clock"].update(visible=True)
    elif trigger == "Dispenser":
        window["disp_status"].update(visible=True)
        window["image"].update(filename=f"{IMAGE_PATH}console_image_resized.png")
        # window["extr_status"].update(visible=True)
    elif trigger == "Scale":
        window['scale'].update(visible=True)
    elif trigger == "Commands":
        window['commands'].update(visible=True)

window.close()
