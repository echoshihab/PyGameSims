# turtle_race implementation from 100 days of code

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the rance? Enter a color: ")
print(user_bet)

colors = ["red", "yellow", "blue", "purple", "green"]
turtle_dict = {}
starting_y = 0
starting_x = -240

race_on = True

for item in colors:
    turtle_dict[item] = Turtle(shape="turtle")
    turtle_dict[item].color(item)
    turtle_dict[item].penup()
    turtle_dict[item].goto(starting_x, starting_y)
    starting_y -= 20

while race_on:
    for item in colors:
        if turtle_dict[item].position()[0] < 250:
            turtle_dict[item].forward(random.randint(0, 10))
        else:
            if turtle_dict[item] != user_bet:
                print("You loose")
                print(f"{item} has won")
            else:
                print(f"You win!!")
                print(f'Winner is {item}')
            race_on = False

screen.exitonclick()
