import turtle

import pandas as pd

from data import repository
from domain import game
from presentation import ui

repo = repository.Repository("50_states.csv")
game = game.Game(repo.get_states())
ui = ui.GameUI()

while True:
    answer = ui.ask_state()
    if not answer:
        continue

    if answer.lower() == "exit":
        pd.DataFrame(game.missing_states()).to_csv("missing_states.csv")
        break

    state = answer.title()
    if game.guess(state):
        x, y = repo.get_coordinates(state)
        ui.draw_state(state, x, y)

    score, total = game.score()
    ui.update_score(score, total)

turtle.mainloop()
