import os
from art import logo
import time

# HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the bid")

bid_dict = {}

def max_bid(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while True:
    name = input("What's your name?\n")
    amount = int(input("What's your bid?\n$ "))
    users = input("Are there any other bidders? Type 'yes' or 'no'\n")

    bid_dict[name] = amount

    if users == 'yes':
        os.system('cls')
        continue
    elif users == 'no':
        os.system('cls')
        max_bid(bid_dict)
        break
    else:
        print("please enter a valid input")

time.sleep(5)