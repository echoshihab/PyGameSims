import time
from turtle import Screen
from player import Player
from car_manager import CarManager

from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager(screen.canvheight)
screen.onkey(player.up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    car_manager.initiate_car()
    time.sleep(0.1)
    screen.update()
