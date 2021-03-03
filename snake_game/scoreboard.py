from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("white")
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}")

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_text()