from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle_one = Paddle(x_coord=280)
paddle_two = Paddle(x_coord=-280)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.tracer(0)
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")

screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

angle = 60
direction = 1
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move(angle)

    # wall bounce logic
    if ball.ycor() >= screen.canvheight - 10 or ball.ycor() <= -(screen.canvheight + 10):
        current_position = ball.pos()
        target_y = ((current_position[0] / screen.canvwidth) * screen.canvheight) * direction
        target_x = screen.canvwidth * direction
        angle = ball.towards(target_x, target_y)

    # paddle one bounce logic
    if ball.distance(paddle_one) < 50 and ball.xcor() < 280:
        direction = -1
        current_angle = ball.towards(paddle_one.pos())
        angle = current_angle + 180

    # paddle two bounce logic
    if ball.distance(paddle_two) < 50 and ball.xcor() < 280:
        direction = 1
        current_angle = ball.towards(paddle_two.pos())
        angle = current_angle - 180

    # check winner
    if ball.xcor() > 290:
        scoreboard.update_score(winner="left")
        ball.reset()
        direction = -1
        current_angle = ball.towards(-280, random.randint(-280, 280))
        angle = current_angle

    elif ball.xcor() < -290:
        scoreboard.update_score(winner="right")
        ball.reset()
        direction = 1
        current_angle = ball.towards(280, random.randint(-280, 280))
        angle = current_angle

    if scoreboard.paddle_one_score >= 3:
        scoreboard.game_over(paddle_one.color())
        game_on = False
    elif scoreboard.paddle_two_score >= 3:
        scoreboard.game_over(paddle_two.color())
        game_on = False

screen.exitonclick()
