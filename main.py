import pandas


#TODO 1. Create a dictionary in this format:
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("What is your name? ").upper()
new_list = [nato_dict[letter] for letter in word]

print(new_list)


