from turtle import Turtle

FONT = ("Courier", 10, "normal")
STARTING_COORDINATE_X = 100
STARTING_COORDINATE_Y = 285
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self, winning_score, player_lives):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(STARTING_COORDINATE_X, STARTING_COORDINATE_Y)
        self.hideturtle()
        self.pencolor("black")
        self.player_lives = player_lives
        self.update_text()
        self.winning_score = winning_score

    def update_text(self):
        self.write(f"Score: {self.score}, lives: {self.player_lives}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_text()

    def update_lives(self):
        self.player_lives -= 1
        self.clear()
        self.update_text()

    def game_over(self, win=True):
        self.goto(0, 0)
        self.write(f"GAME OVER!, You {'Win!' if win else 'Lose!' }", font=FONT, align=ALIGNMENT)
