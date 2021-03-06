from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle_one = Paddle(x_coord=280)
paddle_two = Paddle(x_coord=-280)
ball = Ball()
ball.move()

screen.listen()
screen.tracer(0)
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")


screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

while True:
    screen.update()





screen.exitonclick()
