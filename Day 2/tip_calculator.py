print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
print(bill)
split = input("How many people to split the bill? ")
print(split)
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
print(percentage)
value_per_person = (bill + (bill * percentage/100)) / split
print(f"Each person should pay: ${value_per_person}")