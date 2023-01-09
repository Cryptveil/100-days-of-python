from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=250, starty=250)
screen.title("Pong")
screen.tracer(0)
screen.update
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


screen.exitonclick()
