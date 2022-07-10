#Console game of Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road = input("You are at cross-road. Where do you want to go ?\nType 'left' or 'right':\n")
if cross_road == 'left':
    lake = input("You have reached lake.There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across:\n")
    if lake == 'wait':
        door = input("You arrived to the island. There is a house with three door:one red, one blue and one yellow.\nWhihch door do you choose?\n")
        if door == 'red' :
            print("You have entered room full of snakes\nGame Over.")
        elif door == 'blue':
            print("You Win")
        elif door == 'yellow':
            print("You have entered room full of beast.\nGame Over.")
        else:
            print("Please enter valid input")
    elif lake == 'swim':
        print("Game Over")
    else:
        print("Please enter valid input")
elif cross_road == 'right':
    print("Game Over")
else:
    print("Please enter valid input")
