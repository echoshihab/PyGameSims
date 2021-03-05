from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle_one = Paddle(x_coord=280)
paddle_two = Paddle(x_coord=-280)



screen.tracer(0)

screen.listen()
screen.update()

screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")


screen.exitonclick()

