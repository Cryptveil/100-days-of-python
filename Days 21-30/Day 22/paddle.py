from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.penup()
        self.color("white")
        self.goto(350, 0)


    def up(self):
        self.setheading(UP)


    def down(self):
        self.setheading(DOWN)
