from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.speed = STARTING_MOVE_DISTANCE
        self.level = 1
        self.cars = []

    def next_level(self):

        self.speed += MOVE_INCREMENT

    def create_car(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:

            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))

            random_lane = random.randint(1, 8) * 30 * random.choice([1, -1])
            car.penup()
            car.goto(x=300, y=random_lane)
            car.setheading(180)
            self.cars.append(car)

    def update(self):

        for car in self.cars:

            car.forward(self.speed)

            if car.xcor() < -320:

                self.cars.remove(car)

        self.create_car()