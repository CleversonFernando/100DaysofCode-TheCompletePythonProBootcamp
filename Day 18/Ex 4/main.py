# import colorgram
#
# color_list = []
# raw_color_list = colorgram.extract('dots.jpg', 30)
#
# for item in raw_color_list:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     rgb = (r, b, g)
#     color_list.append(rgb)
# print(color_list)
import random
import turtle

final_list = [(2, 1, 2), (1, 4, 1), (140, 45, 85), (212, 213, 226), (181, 135, 163), (0, 3, 6), (10, 177, 113),
              (111, 62, 33), (215, 15, 173), (173, 92, 55), (216, 143, 209), (5, 73, 94), (232, 220, 213),
              (200, 118, 77), (84, 57, 24), (203, 224, 217), (65, 70, 118), (193, 158, 141), (80, 39, 77),
              (2, 109, 103), (124, 195, 169), (176, 197, 202), (173, 204, 201), (206, 60, 89), (134, 148, 169),
              (211, 179, 183), (226, 186, 169), (219, 12, 206), (6, 143, 65)]

# table length 10 dots by 10 dots, each dot has the size of 20 steps , and are separated by 50 steps
tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)
blank_space = 50
dot_size = 20
initial_position = 450
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for _ in range(10):
    for _ in range(9):
        color = random.choice(final_list)
        tim.color(color)
        tim.dot(dot_size)
        tim.forward(blank_space)
        tim.dot(dot_size)
    tim.back(initial_position)
    tim.sety(tim.ycor() + blank_space)

screen = turtle.Screen()
screen.exitonclick()
