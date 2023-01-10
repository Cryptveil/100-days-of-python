import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

for _ in range(20):
    car_manager.create_car()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()

