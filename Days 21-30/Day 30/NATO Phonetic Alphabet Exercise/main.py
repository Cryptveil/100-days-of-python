import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
is_running = True
while is_running:
    user_word = input("Enter a word: ").upper()
    try:
        result = [new_dictionary[letter] for letter in user_word]
    except KeyError:
        print("Please provide only letters.")
    else:
        is_running = False
        print(result)
