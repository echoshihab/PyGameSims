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
        self.score = 0
        self.goto(STARTING_COORDINATE_X, STARTING_COORDINATE_Y)
        self.hideturtle()
        self.pencolor("white")
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_text()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", font=FONT, align= ALIGNMENT)
