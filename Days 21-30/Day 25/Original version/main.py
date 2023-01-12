import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
# Some screen size shenanigans
# ---------------------------
screen_width, screen_height = turtle.screensize()  
center_x = screen_width / 2
center_y = screen_height / 2
# ---------------------------
screen.setup(width=725, height=491, startx=center_x, starty=center_y)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Opens the csv containing the states name
data = pd.read_csv("50_states.csv")
state_list = data.state.tolist()
guessed_states = []

# Main loop of the game
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(state_list)} States Correct",
        prompt="What's another state's name?").title()

    # Puts the missing states on another csv to review later
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing states.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Gets the states data comparing it to the input state
        state_data = data[data.state == answer_state]
        # Goes to the corresponding coordinates
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
