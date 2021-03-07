from turtle import Turtle
import random
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

    def change_angle_on_wall_bounce(self, target_height, target_width, direction):
        current_position = self.pos()
        target_y = ((current_position[0] / target_height) * target_height) * direction
        target_x = target_width * direction
        angle = self.towards(target_x, target_y)
        return angle

    def change_angle_on_paddle_bounce(self, direction, paddle_position):
        current_angle = self.towards(paddle_position)
        angle = current_angle + (direction * 180)
        return angle

    def change_angle_on_game_reset(self, direction):
        angle = self.towards(direction * 280, random.randint(-280, 280))
        return angle

    def reset(self):
        self.goto(0, 0)




