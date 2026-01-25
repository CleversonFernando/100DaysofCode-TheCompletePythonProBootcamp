import pandas as pd


class Repository:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def get_states(self):
        return self.df["state"].tolist()

    def get_coordinates(self, state):
        row = self.df[self.df["state"] == state]
        return int(row.x), int(row.y)
