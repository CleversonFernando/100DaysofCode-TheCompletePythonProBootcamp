from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


def read_high_score_file():
    with open("High Score.txt", mode='r') as file:
        return int(file.read().strip())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score_file()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.update_high_score()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High Score.txt", mode="w") as file:
                file.write(str(self.high_score))
