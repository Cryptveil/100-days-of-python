from data import MENU, resources
import os

machine_money = 0.0


def format_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global money
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def calculate_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    machine_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return machine_money


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money, drink):
    if drink["cost"] > money:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        global machine_money
        machine_money += drink["cost"]
        change = money - drink["cost"]
        print(f"Here is your change: ${change}")


machine_is_off = False
while not machine_is_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_is_off = True
    elif choice == "report": 
        print (format_report())
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            money = calculate_money()
            is_transaction_successful(money, drink)
