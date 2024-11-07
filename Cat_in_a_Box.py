import re
import sys
import random
import pygame
import pygame_menu
from pygame.locals import *
import Console
import game_objects
import simulation

pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)

SCREEN_WIDTH =  500
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# console_surface = pygame.display.set_mode((400,400))

black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey  = pygame.Color(128, 128, 128)   # Grey
red   = pygame.Color(255, 0, 0)       # Red

number = int(random.random()*10000)
intro_text = [
    "Hello, Employee #{}. Welcome to your new position here at Schrodinger "
    "Inc.!".format(number),

    "You have been entrusted with the care of Cheshire, our office cat.",

    "The catch: he's locked in this box. And, under no condition, are you "
    "permitted to look inside.",

    "To interact with the box, you have access to this console. You can submit "
    "instructions for the day, and a report will be generated.*Console",

    "Currently, the console can control the caloric enrichment dispenser, and "
    "metabolic byproduct remover.",

    "The box has been set upon a mass scale. For your convenience, this data "
    "is connected to your terminal.*Scale",

    "It is up to you to ensure that Cheshire is alive. Good luck!",

    "Messages:*Dispenser"
]

class Dialogue(pygame.sprite.Sprite):
    def __init__(self, text_array, font, color, screen, buffer):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.lines = [None] +  text_array
        self.font = pygame.font.Font(font, 16)
        self.color = color
        self.screen = screen
        self.buffer = buffer
        self.trigger = None

        self.current_message = ''
        self.surface = self.font.render(self.current_message, True, self.color)
        self.rect = self.surface.get_rect()

        self.update()

    def blit(self, surface):
        for line in self.current_message:
            self.surface = self.font.render(line, True, self.color)
            surface.blit(self.surface, self.rect)
            self.rect.top += self.surface.get_height()
        self.rect.top = self.buffer[1]

    def update(self):
        if len(self.lines) > 1:
            self.lines.pop(0)
            self.current_message = self.lines[0]
            # print(self.current_message)
            if "*" in self.current_message:
                self.current_message, self.trigger = self.current_message.split('*')

            self.surface = self.font.render(self.current_message, True, self.color)
            self.rect.left, self.rect.top = self.buffer
            self.wrap_text(self.screen[0]-self.buffer[0])

    def wrap_text(self, max_width):
        words = self.current_message.split(' ')
        space = self.font.render(' ', True, self.color).get_width()
        cursor = self.rect.left

        words_wrapped = []
        line = []

        for word in words:
            word_surface = self.font.render(word, True, self.color)
            word_width = word_surface.get_width()
            if cursor + space + word_width >= max_width:
                cursor = self.rect.left
                line.append(' '.join(words_wrapped))
                words_wrapped = []

            cursor += space + word_width
            words_wrapped.append(word)

        line.append(' '.join(words_wrapped))
        self.current_message = line

    def set_trigger(self, value):
        self.trigger = value

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def transform(self, scale):
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()


background_1 = Background("console_image.png",(0,0))
background_1.transform((500,500))

dialogue_1 = Dialogue(intro_text,'courier.ttc', white,
                      (SCREEN_WIDTH, SCREEN_HEIGHT),
                      (20, SCREEN_HEIGHT-90))

dispenser = game_objects.Input(0.06)
extractor = game_objects.Input(0.20)
cat = game_objects.Cat()
box = game_objects.Box(cat)
cat.insert_in_box(box)

console_1 = Console.Console(dispenser, extractor)
# Game loop begins:
i=0
while True:
    display_surface.fill(black)
    display_surface.blit(background_1.image, background_1.rect)
    dialogue_1.blit(display_surface)
    # print(dialogue_1.trigger)
    if dialogue_1.trigger == "Console":
        console_1.menu.enable()
    elif dialogue_1.trigger == "Scale":
        console_1.add_global_scale(cat.get_mass())
    elif dialogue_1.trigger == "Dispenser":
        console_1.add_dispenser()
        console_1.add_submit()

    if console_1.submit:
        print(console_1.dispenser_command)
    #pygame.draw.line(display_surface,white,(480, 500), (480, 600))

    events = pygame.event.get()
    for event in events:
        print(events)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # print(event.key)
            if event.key == 13:
                dialogue_1.update()
            elif event.key == 27:
                pygame.quit()
                sys.exit()

    if console_1.menu.is_enabled():
        console_1.menu.draw(display_surface)
        console_1.menu.update(events)
    pygame.display.update()