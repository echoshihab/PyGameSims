from turtle import Turtle

# constants
FONT = ("Arial", 8, "bold")
STARTING_COORDINATE_X = 0
STARTING_COORDINATE_Y = 270
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_COORDINATE_X, STARTING_COORDINATE_Y)
        self.hideturtle()
        self.pencolor("white")
        self.paddle_one_score = 0
        self.paddle_two_score = 0
        self.update_text()

    def update_text(self):
        self.write(f"{self.paddle_one_score}: {self.paddle_two_score}", font=FONT, align=ALIGNMENT)

    def update_score(self, winner):
        if winner == "left":
            self.paddle_one_score += 1
        elif winner == "right":
            self.paddle_two_score += 1
        self.clear()
        self.update_text()

    def game_over(self, color):
        self.goto(0, 0)
        self.write(f"GAME OVER! Winner is {color[0].upper()}!!", font=FONT, align=ALIGNMENT)

