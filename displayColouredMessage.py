from sense_hat import SenseHat
from time import sleep
import random
import sys

sense = SenseHat()

rgb = []
digit_error = "Please input numbers only!"

def quit():
  print("Thank you for playing this game. Bye!")
  sleep(3)
  sys.exit()

def value_checker():
  while True:
    if len(rgb) == 0:
      current_colour = "red"
    elif len(rgb) == 1:
      current_colour = "green"
    elif len(rgb) == 2:
      current_colour = "blue"

    input_question = current_colour + " value? In between 0 and 255."
    value_string = input(input_question)

    if value_string.isdigit():
      value_int = int(value_string)
      if 0 <= value_int <= 255:
        return value_int
    elif value_string == "quit":
      quit()
    else:
      print(digit_error)

def colour_picker():
  while len(rgb) < 3:
    rgb.append(value_checker())
    if len(rgb) == 3:
      return_rgb = rgb
      rgb.clear()
      return tuple(return_rgb)

def speed_picker():
  while True:
    speed_string = input("At what speed?")
    if speed_string.isdigit():
      speed_float = float(speed_string)
      return speed_float
    elif value_string == "quit":
      quit()
    else:
      print(digit_error)

print("*enter 'quit' to exit!\nTEXT COLOUR")
random_text_colour = colour_picker()

print("BACKGROUND COLOUR")
random_back_colour = colour_picker()

random_scroll_speed = speed_picker()

sense.set_rotation(0)
sense.show_message("Displaying message in chosen colours and speed", text_colour = random_text_colour,\
                                                                      back_colour = random_back_colour,\
                                                                      scroll_speed = random_scroll_speed)
