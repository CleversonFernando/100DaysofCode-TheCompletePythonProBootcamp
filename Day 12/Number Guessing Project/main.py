import random
import art


# Computer will choose a random number
def computer_guess():
    number = random.randrange(1, 101)
    return number


# Check the difficulty
def choose_a_difficulty():
    number_of_tries = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == "easy":
        number_of_tries = 10
        return number_of_tries
    elif difficulty == "hard":
        number_of_tries = 5
        return number_of_tries
    else:
        print(f"This {number_of_tries} option doesn't exist!")
        choose_a_difficulty()


# Check if won
def check_if_won(guess, computer_guess):
    give_tip(guess, computer_guess)
    if guess == computer_guess:
        return True


# Give a tip
def give_tip(guess, computer_guess):
    if guess > computer_guess:
        print("Too high!")
    elif guess < computer_guess:
        print("Too low!")


# The game
def make_a_guess(number_of_tries, computer_guess):
    while number_of_tries > 0:
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if check_if_won(guess, computer_guess):
            print("You win!")
            number_of_tries = 0
        number_of_tries -= 1
        if number_of_tries == 0:
            print(f"You lose! The number was {computer_guess}")
    play_the_game()


# Start the game
def play_the_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    computer = computer_guess()
    print("I'm thinking in a number between 1 and 100.")
    number_of_tries = choose_a_difficulty()
    make_a_guess(number_of_tries, computer)


play_the_game()
