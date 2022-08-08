import os
from art import logo
import time

print(logo)


def addition(a, b):
    return (a + b)


def substraction(a, b):
    return (a - b)


def multiplication(a, b):
    return (a * b)


def division(a, b):
    return (a / b)


def calculator(first_number, operator, second_number):
    if operator == '+':
        return addition(first_number, second_number)
    elif operator == '-':
        return substraction(first_number, second_number)
    elif operator == '*':
        return multiplication(first_number, second_number)
    elif operator == '/':
        return division(first_number, second_number)

no_1 = float(input("What's the First number?\n"))
while True:
    print("+\n-\n*\n/\n")
    sign = input("Pick an operation: ")
    no_2 = float(input("What's the Next number?\n"))
    result = calculator(no_1, sign, no_2)
    print(f'{no_1} {sign} {no_2} = {result}')
    user_option = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation:")
    if user_option == 'y' or user_option == 'Y':
        no_1 = result
        continue
    elif user_option == 'n' or user_option == 'N':
        os.system('cls')
        no_1 = float(input("What's the First number?\n"))
        continue

time.sleep(5)