from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5


class CarManager:
    def __init__(self):
        self.list_cars = []
        self.create_cars()

        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_change = r.randint(1, 6)
        if random_change == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(r.choice(COLORS))
            new_car.goto(300, r.randint(-230, 250))
            # new_car.setheading(270)
            self.list_cars.append(new_car)

    def move(self):
        for car in self.list_cars:
            car.backward(self.car_speed)

    def incresing_speed(self):
        self.car_speed += MOVE_INCREMENT
