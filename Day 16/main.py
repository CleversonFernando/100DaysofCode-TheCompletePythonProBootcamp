from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

newMenu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()

run_machine = True

while run_machine:
    choice = input(f"What would you like? {newMenu.get_items()}").lower()
    if choice == 'report':
        coffeeMachine.report()
        moneyMachine.report()
    elif choice == 'off':
        run_machine = False
    else:
        drink = newMenu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMachine.make_coffee(drink)
