from data import menu, resources

money_collected = 0


def sufficient_resources(coffee_type):
    for items in resources:
        if resources[items] < menu[coffee_type]['ingredients'][items]:
            print(f"{resources[items]} is insufficient.")
            return False
        else:
            return True


def process_coins():
    print("Please insert coins.")
    total_coins = int(input("How many 1 rupee coin? : ")) * 1
    total_coins += int(input("How many 2 rupee coin? : ")) * 2
    total_coins += int(input("How many 5 rupee coin? : ")) * 5
    total_coins += int(input("How many 10 rupee coin? : ")) * 10
    total_coins += int(input("How many 20 rupee coin? : ")) * 20
    return total_coins


def transaction_successful(received_payment, original_cost):
    global money_collected
    if received_payment > original_cost:
        change = received_payment - original_cost
        print(f"Here is rs {change} in change")
        money_collected = money_collected + original_cost
        return True
    elif received_payment == original_cost:
        money_collected = money_collected + original_cost
        return True
    else:
        print("Money provided by you is insufficient")
        return False


def make_coffee(drink_name, drink_ingredients):
    for things in drink_ingredients:
        resources[things] = resources[things] - drink_ingredients[things]
    print(f"Here is your {drink_name} ☕.\nEnjoy!")


while True:
    user_choice = input("What would you like? (espresso, latte, cappuccino) : ").lower()

    if user_choice == 'report':
        for item in resources:
            if item == 'coffee':
                print(f"{item} : {resources[item]} g")
            else:
                print(f"{item} : {resources[item]} ml")
        print(f"Money : rs {money_collected}")
    elif user_choice == 'off':
        break
    elif user_choice == 'fill':
        resources['water'] = 600
        resources['milk'] = 300
        resources['coffee'] = 100
    else:
        if sufficient_resources(user_choice):
            print(f"The of {user_choice} coffee is rs{menu[user_choice]['cost']}")
            payment = process_coins()
            if transaction_successful(payment, menu[user_choice]['cost']):
                make_coffee(user_choice, menu[user_choice]['ingredients'])
