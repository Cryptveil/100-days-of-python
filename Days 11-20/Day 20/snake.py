from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20,0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake():

    
    def __init__(self):
        self.snake_size = []
        self.create_snake()
        self.head = self.snake_size[0]


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
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        CURRENT_POSITION = self.head.heading()
        if CURRENT_POSITION == RIGHT or CURRENT_POSITION == LEFT:
            self.head.setheading(UP)


    def down(self):
        CURRENT_POSITION = self.head.heading()
        if CURRENT_POSITION == RIGHT or CURRENT_POSITION == LEFT:
            self.head.setheading(DOWN)


    def left(self):
        CURRENT_POSITION = self.head.heading()
        if CURRENT_POSITION == UP or CURRENT_POSITION == DOWN:
            self.head.setheading(LEFT)


    def right(self):
        CURRENT_POSITION = self.head.heading()
        if CURRENT_POSITION == UP or CURRENT_POSITION == DOWN:
            self.head.setheading(RIGHT)
 
