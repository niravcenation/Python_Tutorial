from data import menu, resources


def resources_calculation(resource_type):
    if resources['water'] < menu[resource_type]['ingredients']['water'] and resources['milk'] < \
            menu[resource_type]['ingredients'][
                'milk'] and resources['coffee'] < menu[resource_type]['ingredients']['coffee']:
        return "Sorry, all the ingredients are less"
    elif resources['water'] < menu[resource_type]['ingredients']['water'] and resources['milk'] < menu[resource_type]['ingredients']['milk']:
        return "Sorry, there is not enough water and milk"
    elif resources['water'] < menu[resource_type]['ingredients']['water'] and resources['coffee'] < menu[resource_type]['ingredients']['coffee']:
        return "Sorry, there is not enough water and coffee"
    elif resources['coffee'] < menu[resource_type]['ingredients']['coffee'] and resources['milk'] < menu[resource_type]['ingredients']['milk']:
        return "Sorry, there is not enough milk and coffee"
    elif resources['water'] < menu[resource_type]['ingredients']['water']:
        return "Sorry, there is not enough water"
    elif resources['milk'] < menu[resource_type]['ingredients']['milk']:
        return "Sorry, there is not enough milk"
    elif resources['coffee'] < menu[resource_type]['ingredients']['coffee']:
        return "Sorry, there is not enough coffee"


coin_1 = 0
coin_2 = 0
coin_5 = 0
coin_10 = 0
coin_20 = 0


def coffee_option(type):
    global coin_1, coin_2, coin_5, coin_10, coin_20

    if resources['water'] >= menu[type]['ingredients']['water'] and resources['milk'] >= menu[type]['ingredients'][
        'milk'] and resources['coffee'] >= menu[type]['ingredients']['coffee']:
        print("Please insert coins.")
        coin_1 = int(input("How many 1 rupee coin? : "))
        coin_2 = int(input("How many 2 rupee coin? : "))
        coin_5 = int(input("How many 5 rupee coin? : "))
        coin_10 = int(input("How many 10 rupee coin? : "))
        coin_20 = int(input("How many 20 rupee coin? : "))
        money = cost_calculation(type)
        if money == "You provided less money.":
            print(money)
        else:
            if type == 'espresso':
                resources['water'] = resources['water'] - menu[type]['ingredients']['water']
                resources['milk'] = resources['milk'] - menu[type]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - menu[type]['ingredients']['coffee']
            elif type == 'latte':
                resources['water'] = resources['water'] - menu[type]['ingredients']['water']
                resources['milk'] = resources['milk'] - menu[type]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - menu[type]['ingredients']['coffee']
            elif type == 'cappuccino':
                resources['water'] = resources['water'] - menu[type]['ingredients']['water']
                resources['milk'] = resources['milk'] - menu[type]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - menu[type]['ingredients']['coffee']
            print(money)
    else:
        current_resource = resources_calculation(type)
        print(current_resource)

def cost_calculation(coffee_type):
    global coin_1,coin_2,coin_5,coin_10,coin_20
    total_money = (1 * coin_1) + (2 * coin_2) + (5 * coin_5) + (10 * coin_10) + (20 * coin_20)
    if coffee_type == 'espresso':
        if total_money == menu[coffee_type]['cost']:
            return f"Here is your {coffee_type} coffee,\nEnjoy!!!."
        elif total_money > menu[coffee_type]['cost']:
            money_difference = total_money - menu[coffee_type]['cost']
            return f"Here is rs. {money_difference} in change.\nHere is your {coffee_type} coffee.\nEnjoy!!!"
        elif total_money < menu[coffee_type]['cost']:
            return "You provided less money."
    elif coffee_type == 'latte':
        if total_money == menu[coffee_type]['cost']:
            return f"Here is your {coffee_type} coffee,\nEnjoy!!!."
        elif total_money > menu[coffee_type]['cost']:
            money_difference = total_money - menu[coffee_type]['cost']
            return f"Here is rs. {money_difference} in change.\nHere is your {coffee_type} coffee.\nEnjoy!!!"
        elif total_money < menu[coffee_type]['cost']:
            return "You provided less money."
    elif coffee_type == 'cappuccino':
        if total_money == menu[coffee_type]['cost']:
            return f"Here is your {coffee_type} coffee,\nEnjoy!!!."
        elif total_money > menu[coffee_type]['cost']:
            money_difference = total_money - menu[coffee_type]['cost']
            return  f"Here is rs. {money_difference} in change.\nHere is your {coffee_type} coffee.\nEnjoy!!!"
        elif total_money < menu[coffee_type]['cost']:
            return "You provided less money."

while True:
    user_choice = input("What would you like? (espresso, latte, cappuccino) : ").lower()

    if user_choice == 'report':
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} g")
    elif user_choice == 'latte':
        coffee_option('latte')
    elif user_choice == 'espresso':
        coffee_option('espresso')
    elif user_choice == 'cappuccino':
        coffee_option('cappuccino')
    elif user_choice == 'fill':
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
    elif user_choice == 'off':
        exit(0)
    else:
        print("Sorry, it's not valid option, please choose again.")
        continue
