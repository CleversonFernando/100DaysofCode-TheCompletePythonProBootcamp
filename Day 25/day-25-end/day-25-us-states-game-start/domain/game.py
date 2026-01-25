class Game:
    def __init__(self, states):
        self.states = states
        self.guessed = []

    def guess(self, state):
        if state in self.states and state not in self.guessed:
            self.guessed.append(state)
            return True
        return False

    def missing_states(self):
        return [state for state in self.states if state not in self.guessed]

    def score(self):
        return len(self.guessed), len(self.states)
