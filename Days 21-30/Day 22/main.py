from turtle import Screen
from paddle import Paddle

# Creates the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=250, starty=250)
screen.title("Pong")
screen.tracer(0)  # Stops the animation

paddle2 = Paddle()  # Creates the paddle

screen.listen()  # Listens to input
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
game_is_on = True
while game_is_on:
    screen.update()  # Makes the animation runs again


screen.exitonclick()
