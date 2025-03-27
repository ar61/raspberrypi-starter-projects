from gpiozero import PWMLED
#from tkinter import *
from dataclasses import dataclass

@dataclass
class RGB:
    red: float
    green: float
    blue: float

def change_color(values: RGB):
    red.value = values.red
    green.value = values.green
    blue.value = values.blue
    print(values)


red = PWMLED(23)
green = PWMLED(24)
blue = PWMLED(25)

while True:
    print("Enter red, green, blue values:")
    print("(0 to 1 in float, x to stop)")
    inp = input()
    if inp == "x":
        break
    data = inp.split(',')
    values = RGB(float(data[0]), float(data[1]), float(data[2]))
    change_color(values)

