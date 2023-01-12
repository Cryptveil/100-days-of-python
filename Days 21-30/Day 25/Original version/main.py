import turtle
import pandas as pd
from titlecase import titlecase

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491, startx=0, starty=0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

answer_state = titlecase(screen.textinput(title="Guess the State", prompt="What's"
                                "another state's name?"))

state_list = data.state.tolist()
if answer_state in state_list:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state)


turtle.mainloop()
