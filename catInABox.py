import PySimpleGUI as sg
import game_objects, simulation, configuration, dialogue, utilities
from utilities import IMAGE_PATH

# Configure settings of PySimpleGUI
sg.theme('DarkBlack1')
configuration.configure_pysimplegui()

# Configure settings of matplotlib
configuration.configure_matplotlib()

# Make PySimpleGUI Window
messages = dialogue.get_introduction_text()
clock_string = 'DAY: {}     TIME: 09:00'
window = utilities.make_window(messages, clock_string)

# Enable a few useful key binds
window.bind("<Escape>", "-ESCAPE-") # Escape can be used to terminate game
window.bind("<Return>", "-RETURN-") # Return can be used to advance dialogue/messages
window.bind("<Tab>", "-TAB-")       # Tab can be used to enter developer test data

# Create essential game objects
dispenser = game_objects.Input(0.03)
extractor = game_objects.Input(0.20)
cat = game_objects.Cat()
box = game_objects.Box(cat)
cat.insert_in_box(box)

# Handful of variables that need to be initialized
day = 1
list_commands = []
intro_index = 0
trigger = None
fig_agg = None

# Main Loop for PySimpleGUI Window
while True:

    event, values = window.read()
    # print(event, values)

    if event in (None, 'Exit', "-ESCAPE-"):
        break
    elif event == "-TAB-":
        list_commands = ["DISPENSER-OPEN-TIME-10:00", "DISPENSER-CLOSE-TIME-11:00",
                         "EXTRACTOR-OPEN-TIME-23:00", "EXTRACTOR-CLOSE-TIME-23:30"]
        window['commandsList'].update(list_commands)
        intro_index = len(messages)-1
        window["console"].update(visible=True)
        window["clock"].update(visible=True)
        window["disp_status"].update(visible=True)
        window['scale'].update(visible=True)
        window['commands'].update(visible=True)

    elif event == "-DISP_ADD-":
        list_commands.append('DISPENSER-{}-{}-{}'.format(
            values['-DISP_STATUS-'],values['-DISP_WHEN-'],values['-DISP_VALUE-']))
        window['commandsList'].update(list_commands)
    elif event == "-EXTR_ADD-":
        list_commands.append('EXTRACTOR-{}-{}-{}'.format(
            values['-EXTR_STATUS-'],values['-EXTR_WHEN-'],values['-EXTR_VALUE-']))
        window['commandsList'].update(list_commands)
    elif event == "-DELETE-":
        list_commands = [command for command in list_commands if command not in values['commandsList']]
        window['commandsList'].update(list_commands)
    elif event == "Submit":
        dispenser_commands, extractor_commands = utilities.parse_commands(list_commands)
        result, t, mass = simulation.run_day(box, cat, dispenser, extractor,  dispenser_commands, extractor_commands)
        if fig_agg is not None:
            utilities.delete_fig_agg(fig_agg)
        fig, ax = utilities.make_figure(t, mass)
        fig_agg = utilities.draw_figure(window['CANVAS'].TKCanvas, fig)

        window['report'].update(visible=True)
        window['report'].select()
        day+=1
        window['clock'].update(clock_string.format(day))
        window.Refresh()

        if result == "DEAD":
            window['image'].update(filename=f"{IMAGE_PATH}game_over_resized.png")
            messages.append("Messages: GAME OVER")
            window['commands'].update(visible=False)
            event = "-RETURN-"

    if event == "-RETURN-":
        intro_index = min(intro_index+1, len(messages)-1)
        if intro_index<len(messages):
            current_message = messages[intro_index]
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
