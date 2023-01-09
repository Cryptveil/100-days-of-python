from turtle import Turtle

class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write("Score: ", False, align="center", font=("Arial", 20, "normal"))
