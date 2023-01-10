import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates the screen
screen = Screen()
screen.setup(width=600, height=600, startx=300, starty=300)
screen.tracer(0)

# Initializes all the objects
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# Listens for player input
screen.listen()
screen.onkey(player.move, "Up")

# Main loop
game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detects if the turtle has crossed the road
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Detects if a car has hit the turtle
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
