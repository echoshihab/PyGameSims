from turtle import Turtle

FINISH_LINE_X = -280

class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(1, 2)
        self.setheading(180)
        self.penup()

    def move(self, speed):
        self.forward(speed)


