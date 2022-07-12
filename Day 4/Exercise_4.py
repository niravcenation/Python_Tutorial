import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the rock, paper and scissor game!")

list1 = [rock, paper, scissors]
x = len(list1)
y = random.randint(0, x - 1)
y = list1[y]

name = input("Please enter your name: ")
user_input = input(f"{name} please enter r for rock, p for paper and s for scissor: ")

if user_input == 'r':
    user_input = rock
elif user_input == 's':
    user_input = scissors
elif user_input == 'p':
    user_input = paper

print(f"Robo's choice:\n{y}")
print(f"{name}'s choice:\n{user_input}")

if user_input == paper and y == rock:
    print(f"{name} you win the the game")
elif user_input == rock and y == scissors:
    print(f"{name} you win the the game")
elif user_input == scissors and y == paper:
    print(f"{name} you win the the game")
elif y == paper and user_input == rock:
    print(f"{name} you loose the the game")
elif y == rock and user_input == scissors:
    print(f"{name} you loose the the game")
elif y == scissors and user_input == paper:
    print(f"{name} you loose the the game")
else:
    print(f"{name} your game tied with the Robo")