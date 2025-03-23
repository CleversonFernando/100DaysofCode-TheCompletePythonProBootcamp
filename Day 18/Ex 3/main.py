import random
import turtle
from turtle import Screen

tim = turtle.Turtle()
tim.color("blue")
tim.speed("fastest")
for _ in range(36):
    color = random.choice(["purple", "blue"])
    tim.circle(100)
    heading = tim.heading()
    tim.setheading(heading + 10)
    tim.color(color)

screen = Screen()
screen.exitonclick()
