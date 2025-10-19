from car_manager import CarManager
import time
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car = CarManager()
score = ScoreBoard()

screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for car_item in car.car_list:
        if car_item.distance(player) < 20:
            game_is_on = False
            score.game_over()
            time.sleep(5)

    if player.crossed():
        player.initial_position()
        car.level_up()
        score.level_up()
