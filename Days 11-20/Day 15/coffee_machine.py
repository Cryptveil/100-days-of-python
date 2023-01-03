from data import MENU, resources
import os

money = 0.0


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
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def check_resources():



machine_is_off = False
while not machine_is_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_is_off = True
    elif choice == "report": 
        print (format_report())
    elif choice == "latte":
        money = calculate_money()
        print(money)


 

