MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources['money'] = 0


def play_machine():
    is_on = True
    continue_order = True
    while continue_order:
        choice = input("What would you like? (espresso/latte/cappuccino) or type 'report'").lower()
        if choice != 'off':
            if choice == 'report':
                display_report()
            elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
                check_resources(choice)
                answer = input("Do you want to continue and order something else? Y/N").upper()
                if answer == 'N':
                    continue_order = False
                    resources['water'] = 300
                    resources['milk'] = 200
                    resources['coffee'] = 100
                    resources['money'] = 0
                    print(f"Thank you!")
                    print('\n' * 20)
            else:
                print("This is not a option, please do it again!")
        else:
            continue_order = False
            is_on = False
    if is_on:
        play_machine()


def display_report():
    """Show the default values of resources"""
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}mL")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice):
    """Check if the machine has the amount of necessary resources"""
    ingredients = MENU[choice]['ingredients']
    has_resources = True
    for ingredient, amount in ingredients.items():
        if ingredient in resources:
            if amount > resources[ingredient]:
                has_resources = False
                print(f"Sorry there is not enough {ingredient}")

    if has_resources and calculate_money(choice):
        for ingredient, amount in ingredients.items():
            if ingredient in resources:
                resources[ingredient] = resources[ingredient] - amount
    print(f"Here is your {choice} ☕ Enjoy!")


def calculate_money(choice):
    """Count money"""
    QUARTER = 0.25
    DIME = 0.1
    NICKEL = 0.05
    PENNY = 0.01
    print("Please inert coins:")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    inserted_money = (quarters * QUARTER) + (dimes * DIME) + (nickels * NICKEL) + (pennies * PENNY)

    cost = MENU[choice]['cost']

    if cost > inserted_money:
        print("There is no enough money! Money refunded")
        play_machine()
        return False
    else:
        change = inserted_money - cost
        resources['money'] += cost
        print(f"Here is ${change:.2f} in change.")
        return True


play_machine()
