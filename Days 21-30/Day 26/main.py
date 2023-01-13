import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in data.iterrows():
    print(row.code)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

