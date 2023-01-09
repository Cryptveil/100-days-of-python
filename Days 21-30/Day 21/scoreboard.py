from turtle import Turtle

class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("Score: ", False, align="center", font=("Arial", 20, "normal"))
        self.goto(0, 280)
