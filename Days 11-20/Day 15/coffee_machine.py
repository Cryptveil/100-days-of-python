from data import MENU, resources

machine_money = 0.0


def format_report():
    """Gives a more formatted output for the input 'report'"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${machine_money}")


def calculate_money():
    """Calculates the money put into the machine"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def check_resources(drink_ingredients):
    """Checks if the resources of the machine are enough to make the coffee"""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money, drink):
    """Checks if the money is enough to pay for the coffee"""
    if drink["cost"] > money:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = money - drink["cost"]
        print(f"Here is your change: ${change:.2f}")
        return True


def deduct_ingredients(drink_ingredients):
    """Deducts ingredients from the machine"""
    if drink_ingredients["water"] == 50: 
        resources["water"] -= drink_ingredients["water"]
        resources["coffee"] -= drink_ingredients["coffee"]
    else:
        resources["water"] -= drink_ingredients["water"]
        resources["coffee"] -= drink_ingredients["coffee"]
        resources["milk"] -= drink_ingredients["milk"]
    

machine_is_off = False
while not machine_is_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_is_off = True
    elif choice == "report": 
        format_report()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            money = calculate_money()
            if is_transaction_successful(money, drink):
                machine_money += drink["cost"]
                deduct_ingredients(drink["ingredients"])
                print(f"Here is your {choice} ☕️. Enjoy!")
