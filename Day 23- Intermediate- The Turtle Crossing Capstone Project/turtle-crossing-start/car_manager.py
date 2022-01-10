from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    all_cars = []
    car_speed = STARTING_MOVE_DISTANCE

    def __int__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randrange(-250, 270, 20)
        new_car.goto(280, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
