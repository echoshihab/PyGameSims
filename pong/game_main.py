from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


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
speed = 0.1

while game_on:
    screen.update()
    time.sleep(speed)
    ball.move(angle)

    # wall bounce logic
    if ball.ycor() >= screen.canvheight - 10 or ball.ycor() <= -(screen.canvheight + 10):
        angle = ball.change_angle_on_wall_bounce(target_height=screen.canvheight,
                                                 target_width=screen.canvwidth, direction=direction)

    # paddle one bounce logic
    if ball.distance(paddle_one) < 50 and ball.xcor() < 280:
        direction = -1
        angle = ball.change_angle_on_paddle_bounce(direction=direction,
                                                   paddle_position=paddle_one.pos())

    # paddle two bounce logic
    if ball.distance(paddle_two) < 50 and ball.xcor() < 280:
        direction = 1
        angle = ball.change_angle_on_paddle_bounce(direction=direction,
                                                   paddle_position=paddle_two.pos())

    # reset game board on win
    if ball.xcor() > 290:
        scoreboard.update_score(winner="left")
        ball.reset()
        direction = -1
        speed /= 1.5
        angle = ball.change_angle_on_game_reset(direction=direction)

    elif ball.xcor() < -290:
        scoreboard.update_score(winner="right")
        ball.reset()
        direction = 1
        speed /= 1.5
        angle = ball.change_angle_on_game_reset(direction=direction)

    # end game
    if scoreboard.paddle_one_score >= 3:
        scoreboard.game_over(paddle_one.color())
        game_on = False
    elif scoreboard.paddle_two_score >= 3:
        scoreboard.game_over(paddle_two.color())
        game_on = False

screen.exitonclick()
