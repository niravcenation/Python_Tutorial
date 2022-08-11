from art import logo
import random
import os

number_list = []
for n in range(1, 101):
    number_list.append(n)

target_number = random.randint(0, len(number_list) - 1)


# print(target_number)


def level_difficulty(level):
    global target_number
    print(f"You have total {level} attempts to guess a number")
    for i in range(level, 0, -1):
        print(f"You have {i} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess < 100:
            if user_guess > target_number:
                print("Too high")
                print("Guess again")
            elif user_guess < target_number:
                print("Too low")
                print("Guess again")
            elif user_guess == target_number:
                print("\nYou Win!.\nYou got the right number.")
                break
        elif user_guess > 100:
            print("Your guess is out of the range please try again")
        elif user_guess < 0:
            print("Your guess is out of the range please try again")


while True:
    os.system("cls")

    print(logo)

    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")

    difficulty = input("Choose a difficulty level. type 'easy' or 'hard' :")

    if difficulty == 'easy':
        level_difficulty(10)
    elif difficulty == 'hard':
        level_difficulty(5)

    play_again = input("Do oyu want to play again? Type 'y' or 'n': ")

    if play_again == 'n' or play_again == 'N':
        break
