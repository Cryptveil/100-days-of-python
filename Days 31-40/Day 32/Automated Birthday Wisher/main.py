import random
import pandas as pd
import datetime as dt


letter_list = []

with open("letter_templates/letter_1.txt") as letter_1_file:
    letter_1 = letter_1_file.readlines()
    letter_list.append(letter_1)

with open("letter_templates/letter_2.txt") as letter_2_file:
    letter_2 = letter_2_file.readlines()
    letter_list.append(letter_2)

with open("letter_templates/letter_3.txt") as letter_3_file:
    letter_3 = letter_3_file.readlines()
    letter_list.append(letter_3)

random_letter_template = random.choice(letter_list)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)

print(birthday_dict[today])
