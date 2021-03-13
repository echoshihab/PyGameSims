from car import Car
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.move_increment = 10

    def initiate_car(self):
        entry_point_y = random.randint(-240, 280)
        entry_point_x = random.randint(280, 320)
        car = Car()
        car.color(random.choice(COLORS))
        car.goto(entry_point_x, entry_point_y)
        return car

    def increase_speed(self):
        self.starting_speed += self.move_increment
