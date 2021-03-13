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
        self.high_score = self.get_high_score()
        self.goto(STARTING_COORDINATE_X, STARTING_COORDINATE_Y)
        self.hideturtle()
        self.pencolor("white")
        self.update_text()

    def get_high_score(self):
        with open("high_score.txt", mode="r") as high_score:
            contents = high_score.read()
            return(int(contents))

    def set_high_score(self, score):
        with open("high_score.txt", mode="w") as high_score:
            high_score.write(str(score))

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.update_text()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score(self.score)
        self.score = 0
        self.update_text()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", font=FONT, align=ALIGNMENT)
