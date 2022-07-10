# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")

# Below prices are in $
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small = 2
pepperoni_for_medium = 3
pepperoni_for_large = 3
extra_cheese_for_any = 1

if size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f'Your final bill is: ${small_pizza + pepperoni_for_small + extra_cheese_for_any}.')
elif size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f'Your final bill is: ${small_pizza + pepperoni_for_small}.')
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f'Your final bill is: ${small_pizza + extra_cheese_for_any}.')
elif size == 'S' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f'Your final bill is: ${small_pizza}.')
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f'Your final bill is: ${medium_pizza + pepperoni_for_medium + extra_cheese_for_any}.')
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f'Your final bill is: ${medium_pizza + pepperoni_for_medium}.')
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f'Your final bill is: ${medium_pizza + extra_cheese_for_any}.')
elif size == 'M' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f'Your final bill is: ${medium_pizza}.')
elif size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f'Your final bill is: ${large_pizza + pepperoni_for_large + extra_cheese_for_any}.')
elif size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f'Your final bill is: ${large_pizza + pepperoni_for_large}.')
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f'Your final bill is: ${large_pizza + extra_cheese_for_any}.')
elif size == 'L' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f'Your final bill is: ${large_pizza}.')