import time
from turtle import Screen
from player import Player
import random
from car import Car
from car_manager import CarManager

from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()


screen.onkey(player.up, "Up")

screen.listen()

game_is_on = True

car_list = []
car_list_2 = []
starting_speed = 5

while game_is_on:

    if len(car_list) < 1:
        car = car_manager.initiate_car()
        car_list.append(car)

    for i in car_list:
        if i.xcor() < random.randint(200, 300):
            car_list_2.append(car_list.pop())
        i.move(starting_speed)

    for i in car_list_2:
        if i.xcor() < -310:
            car_list_2.remove(i)
        i.move(starting_speed)

    if player.ycor() >= 280:
        player.reset()

    screen.update()


    time.sleep(.1)







