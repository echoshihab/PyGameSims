from turtle import Screen, Turtle

# constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, move_speed):
        self.x_pos = 0
        self.snake_list = []
        self.create_snake_list()
        self.head = self.snake_list[0]
        self.move_speed = move_speed

    def create_snake_list(self):
        for _ in range(3):
            square = Turtle()
            square.penup()
            square.color("white")
            square.shape("square")
            square.setx(self.x_pos)
            self.x_pos -= 20
            self.snake_list.append(square)

    def move(self):
        for seg in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg - 1].xcor()
            new_y = self.snake_list[seg - 1].ycor()
            self.snake_list[seg].goto(new_x, new_y)
        self.snake_list[0].forward(self.move_speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
