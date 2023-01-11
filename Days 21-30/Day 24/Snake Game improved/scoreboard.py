from turtle import Turtle
from food import Food
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as save_file:
            self.high_score = int(save_file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as save_file:
                save_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


