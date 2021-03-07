from turtle import Turtle


# constants
UP = 90
DOWN = 270
COLORS = ["yellow", "red"]


class Paddle(Turtle):
    color_index = 0

    def __init__(self, x_coord):
        super().__init__()
        self.setpos(x_coord, 0)
        self.penup()
        self.color(COLORS[Paddle.color_index])
        Paddle.color_index += 1
        self.shape("square")
        self.setheading(UP)
        self.turtlesize(1, 5)

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
