import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491, startx=0, starty=0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coordinate(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coordinate)


turtle.mainloop()
