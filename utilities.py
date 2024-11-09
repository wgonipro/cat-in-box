import textwrap
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

IMAGE_PATH="resources/images/"
FONT_PATH="resources/fonts/"

MESSAGE_WIDTH = 40

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

def make_figure(time, mass, disp, extr):
    fig, ax = plt.subplots()
    ax.plot(time, mass, '-', color='#33FF00')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.tick_params(axis='x', labelrotation=70)
    ax.set_ylabel('Mass (kg)', color='#FFCC00')
    ax.grid()

    ax2 = ax.twinx()
    time_double = []
    disp_double = []
    extr_double = []
    for i in range(len(time)):
        time_double.append(time[i])
        time_double.append(time[i])
        disp_double.append(disp[i])
        disp_double.append(disp[min(i+1, len(time)-1)])
        extr_double.append(extr[i])
        extr_double.append(extr[min(i+1, len(time)-1)])
    ax2.plot(time_double, disp_double, '--', color='#00BFFF')
    ax2.plot(time_double, extr_double, '--', color='#DC143C')
    ax2.set_ylim(0.1,1.1)

    plt.tight_layout()
    return fig, ax

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')

def make_window(messages, clock_string, dialogue_index=0, day=1):
    # Create PySimpleGUI layout for LEFT Column consisting of non-user manipulated widgets.
    static_info = sg.Column([[sg.Push(), sg.Image(f"{IMAGE_PATH}console_image_resized.png", key="image"), sg.Push()],
                             [sg.Text(textwrap.fill(messages[dialogue_index], MESSAGE_WIDTH), key='-dialogue-',
                                      size=(MESSAGE_WIDTH, 3))],
                             [sg.Text('CONSOLE>_', visible=False, key='console')],
                             [sg.Text(clock_string.format(day), visible=False, key='clock')],
                             [sg.Text('CONTROLS: DISPENSER, EXTRACTOR', visible=False, key='disp_status')],
                             [sg.Text('SENSORS: MASS1', visible=False, key='scale')],
                             ])

    # Create PySimple GUI layout for Tab Window displaying commands.
    command_tab = sg.Tab('command_tab', [[sg.Text('COMMAND DISPENSER'),
                                          sg.Combo(['OPEN', 'CLOSE'], key='-DISP_STATUS-', default_value='OPEN'),
                                          sg.Text('WHEN'),
                                          sg.Combo(['TIME', 'MASS1'], default_value='TIME', key='-DISP_WHEN-'),
                                          sg.Text('READS'), sg.Input(default_text='', key='-DISP_VALUE-', size=(5, 1)),
                                          sg.Button("+", key='-DISP_ADD-')],
                                         [sg.Text('COMMAND EXTRACTOR'),
                                          sg.Combo(['OPEN', 'CLOSE'], key='-EXTR_STATUS-', default_value='OPEN'),
                                          sg.Text('WHEN'),
                                          sg.Combo(['TIME', 'MASS1'], default_value='TIME', key='-EXTR_WHEN-'),
                                          sg.Text('READS'), sg.Input(default_text='', key='-EXTR_VALUE-', size=(5, 1)),
                                          sg.Button("+", key='-EXTR_ADD-')],
                                         [sg.Listbox([], size=(53, 10), key='commandsList',
                                                     select_mode=sg.SELECT_MODE_EXTENDED)],
                                         [sg.Push(), sg.Button("Delete", key='-DELETE-'), sg.Submit()],
                                         ])

    # Create a PySimpleGUI layout for displaying results from simulation.
    report_tab = sg.Tab('report_tab', [[sg.Canvas(size=(5,5), key='CANVAS')]], visible=False, key='report')

    # Create a PySimpleGUI layout for RIGHT Column consisting of tabs
    variable_info = sg.Column([[sg.TabGroup([[command_tab, report_tab]])]
                               ],
                              visible=False, key="commands")

    # Create final PySimpleGUI layout structure
    layout = [
        [static_info, sg.vtop(variable_info)],
        [sg.VPush()],
        [sg.Text('<ENTER>')],
    ]

    # Create PySimpleGUI window object with established layout. finalize=True is needed to do keybinds.
    window = sg.Window('Cat In A Box Game', layout, finalize=True)  # , size=(WINDOW_WIDTH,WINDOW_WIDTH), finalize=True)

    return window