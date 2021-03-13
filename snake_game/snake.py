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
            self.add_snake_segment()

    def create_snake_block(self):
        square = Turtle()
        square.color("white")
        square.shape("square")
        square.penup()
        return square

    def add_snake_segment(self):
        snake_segment = self.create_snake_block()
        snake_segment.penup()
        snake_segment.setx(self.x_pos)
        self.x_pos -= 20
        self.snake_list.append(snake_segment)

    def extend_snake(self):
        snake_segment = self.create_snake_block()
        snake_segment.goto(self.snake_list[-1].xcor(), self.snake_list[-1].ycor())
        self.snake_list.append(snake_segment)

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

    def reset_snake(self):
        for snake in self.snake_list:
            snake.color("black")
        self.snake_list.clear()
        self.x_pos = 0
        self.snake_list = []
        self.create_snake_list()
        self.head = self.snake_list[0]
