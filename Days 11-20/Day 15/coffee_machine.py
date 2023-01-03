from data import MENU, resources

machine_money = 0.0


def format_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${machine_money}"


def calculate_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money, drink):
    if drink["cost"] > money:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = money - drink["cost"]
        print(f"Here is your change: ${change:.2f}")
        return True


def deduct_ingredients(drink_ingredients):
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
        print (format_report())
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            money = calculate_money()
            if is_transaction_successful(money, drink):
                machine_money += drink["cost"]
                deduct_ingredients(drink["ingredients"])
                print(f"Here is your {choice}, enjoy!")
