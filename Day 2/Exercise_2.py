# Tip Calculator

print("Welcome to the Tip Calculator.")
amount = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10,12, or 15? "))
no_of_people = float(input("How many people to split the bill? "))

total_amt = amount + round((amount * tip) / 100,2)
amt_per_person = total_amt / no_of_people

print(f'Each person should pay: ${round(amt_per_person,2)}')