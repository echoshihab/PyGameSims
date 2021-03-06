from turtle import Turtle

# constants
UP = 90
DOWN = 270
COLORS = ["yellow", "red"]

class Paddle:
    color_index = 0

    def __init__(self, x_coord):
        self.paddle = Turtle()
        self.paddle.setpos(x_coord, 0)
        self.paddle.penup()
        self.paddle.color(COLORS[Paddle.color_index])
        Paddle.color_index += 1
        self.paddle.shape("square")
        self.paddle.setheading(UP)
        self.paddle.turtlesize(1, 5)

    def up(self):
        self.paddle.setheading(UP)
        self.paddle.forward(20)

    def down(self):
        self.paddle.setheading(DOWN)
        self.paddle.forward(20)






