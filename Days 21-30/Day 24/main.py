from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()

    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_size[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
