import colorgram
import random
import turtle
from turtle import Screen

colors = colorgram.extract("image.jpg", 30)

rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

rgb_hirst = rgb[4:]

tim = turtle.Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.speed("fastest")

def random_color():
    color = random.choice(rgb_hirst)
    return color


def draw_ten_dots(x, y):
    tim.pu()
    tim.goto(x, y)
    for i in range(10):
        tim.color(random_color())
        tim.dot(20)
        tim.pu()
        tim.forward(50)

for i in range(0, 500, 50):
    draw_ten_dots(- 230, i - 230)


screen = Screen()
screen.exitonclick()
