from turtle import Turtle


FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.value = 0
        self.goto(-200, 250)
        self.write(f"Score: {self.value}", align="center", font=FONT)

    def increase_score(self):
        self.value += 1

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score: {self.value}", align="center", font=FONT)


