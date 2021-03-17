from turtle import Turtle


class StateTitle(Turtle):
    def __init__(self, state, starting_x, starting_y):
        super().__init__()
        self.penup()
        self.goto(starting_x, starting_y)
        self.hideturtle()
        self.pencolor("black")
        self.write(state)
