# US States Games implementation for day 25 of 100 days of Code by Dr. Angela.

import turtle
import pandas as pd
from state_title import StateTitle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")

game_on = True
score = 0
max_score = 50

guessed_states = []
all_states = data.state.to_list()


def already_guessed(state):
    if state in guessed_states:
        return True


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Score: {str(score)}/{str(max_score)}", prompt="Name a state").title()
    screen.update()
    state_data = data[data.state == answer_state]
    if answer_state == "Exit":
        need_to_learn_states = [state for state in all_states if state not in guessed_states]
        pd.Series(need_to_learn_states).to_csv("need_to_learn_states.csv", index=False, header=None)
        break

    if state_data.state.count() > 0 and not already_guessed(answer_state):
        guessed_states.append(answer_state)
        score += 1
        screen.update()
        x_coordinate = int(state_data.x)
        y_coordinate = int(state_data.y)
        StateTitle(state=answer_state, starting_x=x_coordinate, starting_y=y_coordinate)

screen.exitonclick()
