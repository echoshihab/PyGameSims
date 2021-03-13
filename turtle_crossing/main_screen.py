import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(winning_score=5, player_lives=3)

screen.onkey(player.up, "Up")

screen.listen()

game_is_on = True

starting_cars_list = []
cars_till_finish_list = []

starting_speed = 5

while game_is_on:

    if len(starting_cars_list) < 1:
        car = car_manager.initiate_car()
        starting_cars_list.append(car)

    for i in starting_cars_list:
        if i.xcor() < random.randint(200, 300):
            cars_till_finish_list.append(starting_cars_list.pop())
        i.move(starting_speed)

    for i in cars_till_finish_list:
        if i.xcor() < -310:
            cars_till_finish_list.remove(i)
        i.move(starting_speed)
        if i.distance(player) < 20:
            player.reset()
            scoreboard.update_lives()

    # Update score
    if player.ycor() >= 280:
        player.reset()
        scoreboard.update_score()

    # Check to see if game should continue
    if scoreboard.player_lives < 0:
        scoreboard.game_over(win=False)
        game_is_on = False
    if scoreboard.score >= scoreboard.winning_score:
        scoreboard.game_over()
        game_is_on = False

    screen.update()

    time.sleep(.1)

screen.exitonclick()
