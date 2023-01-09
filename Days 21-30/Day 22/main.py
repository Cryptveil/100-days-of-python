from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Creates the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=250, starty=250)
screen.title("Pong")
screen.tracer(0)  # Stops the animation

ball = Ball()
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
    time.sleep(0.07)
    ball.move()

    # Detects collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects collision with the right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detects collision with the left_paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Checks if the right_paddle missed the ball and resets the ball's position
    if ball.xcor() > 380:
        ball.reset_position()

    # Checks if the left_paddle missed the ball and resets the ball's position
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
