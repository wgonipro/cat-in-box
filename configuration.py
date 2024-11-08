import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib import use as use_agg

def configure_pysimplegui():
    sg.set_options(font=("Courier New", 12))
    sg.set_options(text_color="#33FF00")
    sg.set_options(button_color=('#FFCC00', sg.theme_background_color()))
    sg.set_options(input_elements_background_color='#353935')
    sg.set_options(input_text_color='#FFCC00')
    sg.set_options(border_width=0)
    sg.set_options(slider_border_width=0)
    # sg.set_options(text_element_background_color='#000000')

def configure_matplotlib():
    plt.rc('axes', edgecolor='#FFCC00')
    plt.rc('axes', facecolor=sg.theme_background_color())
    plt.rc('xtick', color='#FFCC00')
    plt.rc('ytick', color='#FFCC00')
    plt.rc('font', family='courier')
    plt.rc('font', size='9')
    plt.rc('grid', color='#FFCC00', alpha=0.8, linestyle='--')
    plt.rc('figure', figsize=(4,3), facecolor=sg.theme_background_color())
    plt.rc('patch', facecolor=sg.theme_background_color())
    use_agg('TkAgg')


