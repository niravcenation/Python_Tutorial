# Strong password Generator project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
mix = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many number of letters do you want in your password ?\n"))
no_numbers = int(input("How many numbers do you want in your password ?\n"))
no_symbols = int(input("How many symbols do you want in your password ?\n"))

# n_of_letters = random.randint(0, len(letters) - 1)
# n_of_numbers = random.randint(0, len(numbers) - 1)
# n_of_symbols = random.randint(0, len(symbols) - 1)

# easy level
# sum = ''
# for n in range(1, no_letters + 1):
#     sum = sum + random.choice(letters)
# for n in range(1, no_numbers + 1):
#     sum = sum + random.choice(numbers)
# for n in range(1, no_symbols + 1):
#     sum = sum + random.choice(symbols)
# print(sum)

# hard level
password_list = []
for n in range(1, no_letters + 1):
    password_list.append(random.choice(letters))
for n in range(1, no_numbers + 1):
    password_list.append(random.choice(numbers))
for n in range(1, no_symbols + 1):
    password_list.append(random.choice(symbols))
password = ""
for n in range(1, no_symbols + no_numbers + no_letters + 1):
    rand_choice = random.choice(password_list)
    password = password + rand_choice
    password_list.remove(rand_choice)
print(password)