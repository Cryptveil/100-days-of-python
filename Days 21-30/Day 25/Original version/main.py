import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491, startx=0, starty=0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(state_list)} States Correct",
        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)


turtle.mainloop()
