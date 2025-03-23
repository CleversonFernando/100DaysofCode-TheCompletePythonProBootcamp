import random
import turtle as t

tim = t
tim.shape("turtle")
tim.color("green")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# print(heroes.gen())
# print(villains.gen())

# for _ in range(30):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
angules = 3
circule = 360
list_of_colors = ["red", "blue", "Black", "purple", "pink", "orange", "yellow", "gray"]

for _ in range(len(list_of_colors)):
    angle_degree = int(circule / angules)
    for _ in range(angules):
        tim.forward(100)
        tim.right(angle_degree)

    angules += 1
    new_color = random.choice(list_of_colors)
    list_of_colors.remove(new_color)
    tim.color(new_color)

screen = t.Screen()
screen.exitonclick()
