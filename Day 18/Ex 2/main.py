import random
import turtle

tim = turtle.Turtle()
tim.color("green")

directions = ["right", "left", "forward"]
list_of_colors = ["red", "blue", "Black", "purple", "pink", "orange", "brown", "gray"]
tim.width(10)
tim.speed(10)


def turn():
    direction = random.choice(directions)
    if direction == "right":
        return tim.right(90)
    elif direction == "left":
        return tim.left(90)
    else:
        return tim.forward(10)


for _ in range(100):
    tim.color(random.choice(list_of_colors))
    turn()
    tim.forward(10)

screen = turtle.Screen()
screen.exitonclick()
