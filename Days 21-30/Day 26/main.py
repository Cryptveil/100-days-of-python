import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: ").upper()
input_letters = [letter for letter in user_word]
result = [new_dictionary[letter] for letter in input_letters if letter.isalpha()]
print(result)
