from turtle import Turtle


FONT = ("Courier", 20, "normal")



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.value = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(0, 250)
        self.write(f"Your score: {self.value} High score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.value += 1
        self.update_score()

    # def game_over(self):
    #     self.color("white")
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write("Game Over", align="Center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.value > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.value))
        self.value = 0
        self.update_score()

    def update_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.clear()
        self.goto(0, 250)
        self.write(f"Your score: {self.value} High score: {self.high_score}", align="center", font=FONT)



