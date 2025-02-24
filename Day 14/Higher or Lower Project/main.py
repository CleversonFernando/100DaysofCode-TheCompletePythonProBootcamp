import random
from itertools import count
from random import Random

import art
import game_data


def choose():
    choice = random.choice(game_data.data)
    return choice


def check(first_choose, second_choose, choice, count):
    if choice == 'A':
        if first_choose['follower_count'] < second_choose['follower_count']:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score!:{count}")
            return False
        else:
            return True
    if choice == 'B':
        if first_choose['follower_count'] > second_choose['follower_count']:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score!: {count}")
            return False
        else:
            return True


def update_choice(first_choose, second_choose):
    if second_choose['follower_count'] > first_choose['follower_count']:
        first_choose = second_choose
    return first_choose


def play_game():
    continue_game = True
    count = 0
    while continue_game:
        first_choose = choose()
        print(art.logo)
        equal = True
        while equal:
            second_choose = choose()
            if second_choose['name'] != first_choose['name']:
                equal = False
        if count == 0:
            text = ""
        else:
            text = f"You're right! Current core: {count}"
        print(
            f"{text}\n Compare A: {first_choose['name']}, a {first_choose['description']}, from {first_choose['country']} , {first_choose['follower_count']}")
        print(art.vs)
        print(
            f"Against B: {second_choose['name']}, a {second_choose['description']}, from {second_choose['country']}, {second_choose['follower_count']}")
        choice = input("Type 'A' or 'B':").capitalize()
        right_answer = check(first_choose, second_choose, choice, count)
        first_choose = update_choice(first_choose, second_choose)
        if right_answer:
            count += 1
            if count < 10:
                continue_game = right_answer
            else:
                print(art.logo)
                print("You win!")
                continue_game = False
        else:
            continue_game = False


play_game()
