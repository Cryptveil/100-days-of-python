from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:


    def __init__(self):
        """Initializes our cars"""
        self.car_list = []
        self.create_car()
        

    def create_car(self):
        """Creates a new car"""
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.goto(random.randint(-280, 280), random.randint(-250, 250))
        self.car_list.append(new_car)


    def move(self):
        """Moves the car"""
        pass
