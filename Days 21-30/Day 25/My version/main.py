import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Estados do Brasil")
screen.setup(width=712, height=722, startx=0, starty=0)
image = "estados_brasil.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("estados.csv")
state_list = data.estado.tolist()
guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(state_list)} Estados Corretos",
        prompt="Qual o próximo estado?").title()

    if answer_state == "Sair":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("estados para aprender.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.estado == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
