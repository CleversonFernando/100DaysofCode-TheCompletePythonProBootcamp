import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = 110
for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y)
    y -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = Turtle

while is_race_on:
    for turtle in all_turtles:
        turtle.pendown()
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you win! {winner_color}")
            else:
                print(f"You loose! {winner_color}")
        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)
        random_distance = random.randint(0, 45)
        turtle.left(random_distance)
        random_distance = random.randint(0, 45)
        turtle.right(random_distance)

screen.exitonclick()
