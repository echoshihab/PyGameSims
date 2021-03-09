from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:
    def __init__(self, screen_height):
        self.screen_height = screen_height
        self.starting_speed = 5
        self.move_increment = 10

    def initiate_car(self):
        entry_point = random.randint(1, self.screen_height)
        car = Car()
        car.color(random.choice(COLORS))
        car.goto(280, entry_point)
        car.move(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += self.move_increment






