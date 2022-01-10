from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Constants for setheading directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []  # A list to store snake objects
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        # Move last segment to second to the last and so on.
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        self.snake_segments.append(new_snake_segment)
        new_snake_segment.goto(position)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())  # position method comes from turtle class to get position

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

