from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_is_running = True


def enough_resources(drink):
    """Created these functions to keep the code cleaner"""
    return coffee_maker.is_resource_sufficient(drink)


def payment_made(cost):
    return money_machine.make_payment(drink.cost)


while machine_is_running:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        machine_is_running = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if enough_resources(drink) and payment_made(drink.cost):
            coffee_maker.make_coffee(drink)
