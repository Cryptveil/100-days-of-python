import turtle
import pandas

screen = turtle.Screen()
screen.title("Estados do Brasil")
screen.setup(width=712, height=722, startx=0, starty=0)
image = "estados_brasil.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coordinate(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coordinate)


turtle.mainloop()
