def add(*args):
    sum_ = 0
    list_ = []
    for number in args:
        list_.append(number)
        sum_ += number

    # print(list_)
    # print(sum_)


add(1,2,3,4)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    # print(n)


calculate(2, add=3, multiply=4)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Ford")

# print(my_car.make)