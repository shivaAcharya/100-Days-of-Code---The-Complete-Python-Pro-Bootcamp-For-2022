from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counterclockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=move_counterclockwise, key="a")
screen.onkeypress(fun=move_clockwise, key="d")
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()

