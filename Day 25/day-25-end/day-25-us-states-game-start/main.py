import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# check the position by clicking
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

states_csv = pd.read_csv("./50_states.csv")
states_dict = states_csv.to_dict()
states_df = pd.DataFrame(states_dict)
guessed = []

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-280, 250)


def get_answer():
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

    # Convert the guess to title case
    title = answer_state.title()
    return title


def check_guess(title):
    # check if the guess is among the 50 states
    if title not in guessed:
        if title in states_df["state"].values:
            # Record the correct guesses in a list
            state_row = states_df[states_df["state"] == title]
            x = state_row.x.item()
            y = state_row.y.item()

            # write the correct guesses onto the map
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x, y)
            new_turtle.write(title)

            guessed.append(title)
    check_score()


# keep track of the score
def check_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {len(guessed)} / {len(states_df)}")


# use a loop to allow the user to keep guessing
continue_game = True
while len(guessed) < 50:
    check_guess(get_answer())

turtle.mainloop()
