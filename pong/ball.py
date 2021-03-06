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

    def move(self):
        self.setheading(45)
        self.goto((-310, 310))


