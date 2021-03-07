from turtle import Turtle

# constants
UP = 90
DOWN = 270
COLORS = ["yellow", "red"]


class Ball(Turtle):

    def __init__(self, ):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self, heading):
        self.setheading(heading)
        self.forward(10)

    def reset(self):
        self.goto(0, 0)




