from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        }
def calculator():
    continue_calculating = True
    print(logo)
    first_number = float(input("What's the first number?: "))

    for keys in operations:
        print(keys)

    operation = input("Pick an operation from the line above: ")
    second_number = float(input("What's the next number?: "))
    calculation_function = operations[operation]
    first_answer = calculation_function(first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {first_answer}")

    while continue_calculating:

        print("Type 'y' to continue calculating with {first_answer}", end="")
        print(" or type 'n' to start a calculation with a new number.")
        choice = input(f"If you want to stop the program, simply type 'stop': ")

        if choice == 'n':
            continue_calculating = False
            calculator()

        elif choice == 'y':
            operation = input("Pick another operation: ")
            next_number = int(input("What's the next number?: "))
            calculation_function = operations[operation]
            second_answer = calculation_function(first_answer, next_number)
            print(f"{first_answer} {operation} {next_number} = {second_answer}")
            first_answer = second_answer
        elif choice == 'stop':
            continue_calculating = False

calculator()
