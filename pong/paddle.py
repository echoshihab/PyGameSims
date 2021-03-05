from turtle import Turtle

# constants
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, x_coord):
        self.paddle = Turtle()
        self.paddle.setpos(x_coord, 0)
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.turtlesize(5, 1)

    def up(self):
        self.paddle.setheading(UP)
        self.paddle.forward(20)

    def down(self):
        self.paddle.setheading(DOWN)
        self.paddle.forward(20)






