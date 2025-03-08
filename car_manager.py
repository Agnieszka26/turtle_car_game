from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 300

class CarManager:
    def __init__(self):
        self.cars = []
        self.counter = 0
        self.speed_car = STARTING_MOVE_DISTANCE

    def create_car(self):
        if self.counter % 6 == 0:  # Only create a car every 6th iteration
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            start_y = randint(-240, 240)
            new_car.goto(START_X,  start_y)
            self.cars.append(new_car)

        self.counter +=1

    def move_car(self):
        for car in self.cars:
            x = car.xcor() - self.speed_car
            y = car.ycor()
            car.goto(x, y)
