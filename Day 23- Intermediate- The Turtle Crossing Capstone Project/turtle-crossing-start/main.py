import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, "Up")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    count += 1

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(tim) < 15:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
