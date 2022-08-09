from art import logo, original_cards
import random
import os
import time

cards = []
user_cards = []


def user(n):
    global cards, user_cards, original_cards
    cards = original_cards
    i = 0
    if n >= 2:
        while i < n:
            i = i + 1
            card_1 = cards[random.randint(0, len(cards) - 1)]
            cards.remove(card_1)
            user_cards.append(card_1)
            if sum(user_cards) >= 21:
                cards = original_cards
                user_cards = []
                i = 0
    else:
        while i < n:
            i = i + 1
            card_1 = cards[random.randint(0, len(cards) - 1)]
            cards.remove(card_1)
            user_cards.append(card_1)


total_robo_cards = []
robo_cards = []


def computer(n):
    global total_robo_cards, robo_cards, original_cards
    total_robo_cards = original_cards
    i = 0
    if n >= 2:
        while i < n:
            i = i + 1
            card_1 = total_robo_cards[random.randint(0, len(total_robo_cards) - 1)]
            total_robo_cards.remove(card_1)
            robo_cards.append(card_1)
            if sum(robo_cards) >= 21:
                total_robo_cards = original_cards
                robo_cards = []
                i = 0
    else:
        while i < n:
            i = i + 1
            card_1 = total_robo_cards[random.randint(0, len(total_robo_cards) - 1)]
            total_robo_cards.remove(card_1)
            robo_cards.append(card_1)


length_of_robo_cards = 0


def deal_card(number_of_cards):
    global user_cards, robo_cards
    user(number_of_cards)
    print(f"Your cards: {user_cards}, current score:{sum(user_cards)}")

    computer(number_of_cards)
    # print(robo_cards)
    global length_of_robo_cards
    length_of_robo_cards = len(robo_cards)
    print(f"Computer's first card: {robo_cards[:length_of_robo_cards - 1]}")


continuous = input("Do you want to play BlackJack game? Type 'y' or 'n' : ")

if continuous == 'y' or continuous == 'Y':
    while True:
        os.system("cls")
        print(logo)

        deal_card(2)

        while True:
            if sum(user_cards) > 21:
                if 11 not in user_cards:
                    break
                else:
                    i = user_cards.index(11)
                    user_cards = user_cards[:i] + [1] + user_cards[i + 1:]

            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y' or another_card == 'Y':

                user(1)
                print(f"Your cards after getting another card: {user_cards}, current score: {sum(user_cards)}")

                print(f"Computer's first card: {robo_cards[:length_of_robo_cards - 1]}")
            elif another_card == 'n' or another_card == 'N':
                break

        while True:

            if sum(robo_cards) <= 17 and sum(user_cards) <= 21:
                computer(1)
                print(robo_cards)
                print(f"Computer's card after getting another card: {robo_cards[:len(robo_cards) - 1]}")
            elif sum(robo_cards) > 21:
                if 11 not in user_cards:
                    break
                else:
                    i = user_cards.index(11)
                    user_cards = user_cards[:i] + [1] + user_cards[i + 1:]
            else:
                break
        print("\n")

        user_score = sum(user_cards)
        computer_score = sum(robo_cards)
        if user_score > 21 and computer_score <= 21:
            print(f"Your final hand {user_cards},with total score {user_score}")
            print(f"Robo's final hand {robo_cards}, with total score {computer_score}")
            print("Sorry! You loose.\nBetter luck next time")
        elif user_score <= 21 and computer_score <= 21 and user_score < computer_score:
            print(f"Your final hand {user_cards},with total score {user_score}")
            print(f"Robo's final hand {robo_cards}, with total score {computer_score}")
            print("Sorry! You loose.\nBetter luck next time")
        elif user_score <= 21 and computer_score <= 21 and user_score > computer_score:
            print(f"Your final hand {user_cards},with total score {user_score}")
            print(f"Robo's final hand {robo_cards}, with total score {computer_score}")
            print("You win")
        elif user_score <= 21 and computer_score > 21:
            print(f"Your final hand {user_cards},with total score {user_score}")
            print(f"Robo's final hand {robo_cards}, with total score {computer_score}")
            print("You Win.")
        elif user_score == computer_score:
            print(f"Your final hand {user_cards},with total score {user_score}")
            print(f"Robo's final hand {robo_cards}, with total score {computer_score}")
            print("Match Drawn!")
        print("\n")
        play_again = input("Do you want to play again? Type 'y' or 'n':")
        if play_again =='n' or play_again == 'N':
            break
    time.sleep(5)
elif continuous == 'n' or continuous == 'N':
    exit()
