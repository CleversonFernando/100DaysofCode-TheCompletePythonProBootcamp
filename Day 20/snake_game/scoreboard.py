from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)
