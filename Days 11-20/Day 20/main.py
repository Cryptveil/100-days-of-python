from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake_size = []
position = 0
game_is_on = True

for _ in range(0, 3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x=position, y=0)
    snake_size.append(new_segment)
    position -= 20
    
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(len(snake_size)-1, 0, -1):
        new_x = snake_size[segment_number - 1].xcor()
        new_y = snake_size[segment_number - 1].ycor()
        snake_size[segment_number].goto(new_x, new_y)
    snake_size[0].forward(20)

screen.exitonclick()
