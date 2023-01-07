from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake_size = []
position = 0

for segments in range(0, 3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x=position, y=0)
    snake_size.append(new_segment)
    position -= 20


screen.exitonclick()
