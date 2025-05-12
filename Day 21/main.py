class Animal:
    def __init__(self):
        self.number_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("under water")

    def swim(self):
        print("swimming")


nemo = Fish()

nemo.swim()
print(nemo.number_eyes)
nemo.breathe()
