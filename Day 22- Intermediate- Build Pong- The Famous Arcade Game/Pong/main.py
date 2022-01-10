from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
# screen.screensize(800, 600, "black")
screen.title("Pong")

screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")

screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

game_is_one = True
sleep_time = 0.1

while game_is_one:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_time *= 0.9

    # Ball goes beyond paddle_left
    if ball.xcor() < -360:
        ball.reset_position()
        score.r_point()

    # Ball goes beyond paddle_right
    if ball.xcor() > 360:
        ball.reset_position()
        score.l_point()

screen.exitonclick()
