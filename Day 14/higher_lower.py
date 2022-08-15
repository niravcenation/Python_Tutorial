from art import logo, vs
from data import data
from os import system
import random
import time

comparision_list = []
account_list = data
def select_any(number_of_comparision):
    global comparision_list, account_list
    i = 0
    while i < number_of_comparision:
        random_account = account_list[random.randint(0, len(account_list) - 1)]
        account_list.remove(random_account)
        comparision_list.append(random_account)
        i = i + 1

def account_a_or_b(account_value):
    global comparision_list
    select_any(2)
    if account_value == 'A':
        user_1 = comparision_list[0]["follower_count"]
        return user_1
    elif account_value == 'B':
        user_2 = comparision_list[1]["follower_count"]
        return user_2


def comparision():
    global comparision_list
    print(
        f"Compare A: {comparision_list[0]['name']}, a {comparision_list[0]['description']}, from {comparision_list[0]['country']}\n{vs}\nCompare B: {comparision_list[1]['name']}, a {comparision_list[1]['description']}, from {comparision_list[1]['country']}")


no_of_comparision = 0
score = 0
while True:
    if no_of_comparision > 0:
        if ask_user == 'A' and A > B:
            system("cls")
            print(logo)
            score = score + 1
            print(f"You are right. Current Score: {score}")
            comparision_list = []
        elif ask_user == 'B' and B > A:
            system("cls")
            print(logo)
            score = score + 1
            print(f"You are right. Current Score: {score}")
            comparision_list = []
        elif ask_user == 'A' and A < B:
            system("cls")
            print(logo)
            print(f"Sorry, that's wrong.\nYour final score: {score}")
            break
        elif ask_user == 'B' and B < A:
            system("cls")
            print(logo)
            print(f"Sorry, that's wrong.\nYour final score: {score}")
            break
    else:
        print(logo)

    A = account_a_or_b('A')
    # print(A)
    B = account_a_or_b('B')
    # print(B)

    comparision()
    ask_user = input("Who has more followers? 'A' or 'B': ").upper()

    no_of_comparision = no_of_comparision + 1
    continue

time.sleep(5)
