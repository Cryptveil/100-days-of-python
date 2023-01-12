import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491, startx=0, starty=0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()
