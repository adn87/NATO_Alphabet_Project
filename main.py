import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}


def generate_phonetic():
    word = input("What is your name? ").upper()
    try:
        new_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()
