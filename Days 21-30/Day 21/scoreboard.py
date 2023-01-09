from turtle import Turtle

class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.write(align="center", font=("Arial", 8, "normal"))
