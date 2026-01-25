import turtle


class GameUI:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("US States Game")
        self.screen.addshape("blank_states_img.gif")
        turtle.shape("blank_states_img.gif")

        self.scoreboard = turtle.Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-280, 250)

    def ask_state(self):
        return self.screen.textinput(title="Make a guess", prompt="What's another state's name?")

    def draw_state(self, name, x, y):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(name)

    def update_score(self, score, total):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {score} / {total}")
