from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        """Initializes the turtle"""
        super().__init__() 
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        """Moves the turtle"""
        self.forward(MOVE_DISTANCE)


    def reset_position(self):
        """Resets turtle position when game over or when next level"""
        self.goto(STARTING_POSITION)

