# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_str = name1 + name2
lower_case_str = combined_str.lower()

t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e1 = lower_case_str.count("e")

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e2 = lower_case_str.count("e")

sum_true = str(t + r + u + e1)
sum_love = str(l + o + v + e2)

love_score = int(sum_true + sum_love)

if 90 < love_score or love_score < 10:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 < love_score < 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
