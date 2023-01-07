from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20,0), (-40, 0)]


class Snake():

    
    def __init__(self):
        self.snake_size = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.snake_size.append(new_segment)


    def move(self):
        for segment_number in range(len(self.snake_size)-1, 0, -1):
            new_x = self.snake_size[segment_number - 1].xcor()
            new_y = self.snake_size[segment_number - 1].ycor()
            self.snake_size[segment_number].goto(new_x, new_y)
        self.snake_size[0].forward(MOVE_DISTANCE)


    def up(self):
        CURRENT_POSITION = self.snake_size[0].heading()
        if CURRENT_POSITION == 0 or CURRENT_POSITION == 180:
            self.snake_size[0].setheading(90)


    def down(self):
        CURRENT_POSITION = self.snake_size[0].heading()
        if CURRENT_POSITION == 0 or CURRENT_POSITION == 180:
            self.snake_size[0].setheading(270)


    def left(self):
        CURRENT_POSITION = self.snake_size[0].heading()
        if CURRENT_POSITION == 90 or CURRENT_POSITION == 270:
            self.snake_size[0].setheading(180)


    def right(self):
        CURRENT_POSITION = self.snake_size[0].heading()
        if CURRENT_POSITION == 90 or CURRENT_POSITION == 270:
            self.snake_size[0].setheading(0)
 
