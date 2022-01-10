from turtle import Turtle, Screen
import random

is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What turtle will win the race? Enter a color: \n red, blue, "
                                                          "orange, yellow, green, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-120 + i * 50)
    turtles.append(new_turtle)

winning_turtle_color = ""

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle_color = turtle.pencolor()
            is_game_on = False
        turtle.forward(random.randint(0, 10))

    if not is_game_on:
        if winning_turtle_color == user_bet:
            print(f"You've won. The {winning_turtle_color} turtle is the winner.")
        else:
            print(f"You've lost. The {winning_turtle_color} turtle is the winner.")


screen.exitonclick()
