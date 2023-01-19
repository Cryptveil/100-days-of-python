import random
import pandas as pd
import datetime as dt
import smtplib

EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

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

if today in birthday_dict:
    person = birthday_dict[today]
    recipient = person["email"]
    chosen_letter = "".join(random_letter_template)
    chosen_letter = chosen_letter.replace("[NAME]", person["name"])

with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=recipient, msg=chosen_letter)
