from turtle import Screen
from paddle import Paddle

# Creates the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=250, starty=250)
screen.title("Pong")
screen.tracer(0)  # Stops the animation

left_paddle = Paddle((-350, 0))  # Creates the paddle
right_paddle = Paddle((350, 0))  # Creates the paddle

screen.listen()  # Listens to input
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Main loop of the game
game_is_on = True
while game_is_on:
    screen.update()  # Makes the animation runs again


screen.exitonclick()
