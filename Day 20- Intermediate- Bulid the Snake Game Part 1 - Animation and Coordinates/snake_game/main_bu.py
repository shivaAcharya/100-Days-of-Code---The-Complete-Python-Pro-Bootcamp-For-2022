import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# A list to store snake objects
snake_segments = []
positions = [(0, 0), (-20, 0), (-40, 0)]

for i in range(len(positions)):
    new_snake_segment = Turtle(shape="square")
    new_snake_segment.color("white")
    new_snake_segment.penup()
    snake_segments.append(new_snake_segment)
    new_snake_segment.goto(positions[i])


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move last segment to second to the last and so on.
    for segment in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[segment - 1].xcor()
        new_y = snake_segments[segment - 1].ycor()
        snake_segments[segment].goto(new_x, new_y)

    snake_segments[0].forward(20)
    snake_segments[0].right(60)

screen.exitonclick()
