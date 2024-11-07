import pygame
import pygame_menu as pm

font = pm.font.FONT_DIGITAL
font_green = pygame.Color(51, 255, 0)
cursor_white = pygame.Color(255, 255, 255)
my_theme = pm.themes.Theme(background_color=(0, 0, 0), title=False, widget_font=font,
                           widget_font_color=font_green, cursor_color=cursor_white,
                           widget_selection_effect=pm.widgets.LeftArrowSelection())
# my_theme.background_color = color_opaque = (50, 100, 200)

class Console:

    def __init__(self, dispenser, extractor):
        self.menu = pm.Menu('Console', 395, 290,
                               theme=my_theme, enabled=False, center_content=False,
                               position=(58, 35, False))
        self.date = (1, 9, 0)
        self.dispenser_status = dispenser.get_status_str()
        self.extractor_status = extractor.get_status_str()
        header = self.menu.add.label("CONSOLE>_", max_char=-1, font_size=12,
                                     align=pm.locals.ALIGN_LEFT)
        header_rect = header.get_rect()
        header_rect.top = 5

        self.label_clock = self.add_clock()
        self.label_dispenser_status = self.add_dispenser_status()
        self.label_extractor_status = self.add_extractor_status()
        self.label_global_scale = None
        self.label_dispenser = None
        self.button_submit = None
        self.submit = False
        self.menu.add.vertical_margin(10)
        # self.add_global_scale(4.1)

        self.dispenser_command = {True:[],False:[]}
        self.extractor_command = {True:[],False:[]}

    def add_clock(self):
        clock = self.menu.add.label("Day: {}     Time: {:02d}:{:02d}".format(self.date[0],
                                                                self.date[1], self.date[2]),
                            max_char=-1, font_size=12, align=pm.locals.ALIGN_LEFT)
        return clock

    def add_dispenser_status(self):
        dispenser_status = self.menu.add.label("Dispenser Status: <{}>".format(self.dispenser_status),
                            max_char=-1, font_size=12, align=pm.locals.ALIGN_LEFT)

        return dispenser_status

    def add_extractor_status(self):
        extractor_status = self.menu.add.label("Extractor Status: <{}>".format(self.extractor_status),
                            max_char=-1, font_size=12, align=pm.locals.ALIGN_LEFT)

        return extractor_status

    def add_global_scale(self, mass):
        if self.label_global_scale is None:
            self.label_global_scale = self.menu.add.label("Scale: {:.2f} KG".format(mass),
                                max_char=-1, font_size=12, align=pm.locals.ALIGN_LEFT)
            self.menu.add.vertical_margin(10)

    def add_dispenser(self):
        if self.label_dispenser is None:
            self.label_dispenser = True
            dispenser_open  = self.menu.add.text_input("Command Dispenser Open:  ",
                                     default="HH:MM",
                                     border_color=None, font_color=font_green,
                                     font_size=12, align=pm.locals.ALIGN_LEFT,
                                     onreturn=self.command_dispenser_open)#, cursor_size=(12,24))
            dispenser_close = self.menu.add.text_input("Command Dispenser Close: ",
                                     default="HH:MM",
                                     border_color=None, font_color=font_green,
                                     font_size=12, align=pm.locals.ALIGN_LEFT,
                                     onreturn=self.command_dispenser_closed)#, cursor_size=(12,24))

    def add_submit(self):
        if self.button_submit is None:
            self.button_submit = True
            self.menu.add.vertical_fill()
            self.menu.add.button('Submit', self.submit_commands(),
                                 font_size=12, align=pm.locals.ALIGN_RIGHT,
                                 )

    def command_dispenser_open(self, value):
        self.dispenser_command[True].append(value)

    def command_dispenser_closed(self, value):
        self.dispenser_command[False].append(value)

    def submit_commands(self):
        self.submit = True