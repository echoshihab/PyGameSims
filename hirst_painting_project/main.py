# solution to 100 days code creating a Damien Hirst painting with python

import colorgram
import turtle as t
import random
import math

rgb_colors = []
colors = colorgram.extract('image.jpg', 20)

for color in colors:
    # removes white background colors
    if not (color.rgb.r > 245 and color.rgb.g > 245 and color.rgb.b > 245):
        rgb_colors.append((color.rgb.r, color.rgb.b, color.rgb.g))


def get_random_color():
    # choose random color from rgb color list
    return random.choice(rgb_colors)


def make_line():
    # make one line of dots
    for _ in range(1, 10):
        tim.color(get_random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.dot(20)


def go_to_next_line_end():
    tim.left(90)
    tim.forward(50)
    tim.left(90)


def go_to_next_line_start():
    tim.right(90)
    tim.forward(50)
    tim.right(90)


def make_image(num):
    num_of_lines = math.floor(num/2)
    for _ in range(num_of_lines):
        make_line()
        go_to_next_line_end()
        make_line()
        go_to_next_line_start()


# create turtle and screen
tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

# initial set up
tim.penup()
tim.goto(-250, -250)
make_image(10)

screen.exitonclick()

# 10 x 10 rows of spots
# should be 20 in size
# spaced around by 50 spaces
