import random

def get_introduction_text():
    number = int(random.random()*10000)
    introduction_text = [
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
    return introduction_text