import random

import art


def do_you_want_a_new_card():
    answer = input("Type 'y' to get another card, type 'n' to pass:\n")
    if answer == 'y':
        return True
    else:
        return False


def check_if_win(total_score):
    if total_score == 21:
        print("You win!")
        return False
    if total_score > 21:
        print("You lost!")
        return False


def computer_choosing_cards(computer_cards):
    new_card = computer_cards.append(choose_cards())
    if sum(computer_cards) > 21:
        return print("You win!")


def show_result(total_score, total_computer):
    if total_score > total_computer:
        print("You win!")
    else:
        print("You lost!")


def choose_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


def initiate_program():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")

    start_play = True

    if play == 'y':
        start_play = True
    else:
        start_play = False
        initiate_program()

    # while start_play:
    print(art.logo)
    player_cards = [choose_cards(), choose_cards()]
    computer_cards = [choose_cards(), choose_cards()]
    total_score = sum(player_cards)
    print(f"Your cards are [{player_cards[0]}][{player_cards[1]}], current score: {total_score}")
    print(f"Computer first card: {computer_cards[0]}")

    continue_the_game = do_you_want_a_new_card

    while do_you_want_a_new_card():
        player_cards.append(choose_cards())
        total_score = sum(player_cards)
        text = ""
        for item in player_cards:
            text += f"[{item}]"
        print(f"Your cards are {text}, current score: {total_score}")
        win = check_if_win(total_score)
        continue_the_game = win

    computer_choosing_cards(computer_cards)
    total_computer = sum(computer_cards)
    show_result(total_score, total_computer)


initiate_program()
