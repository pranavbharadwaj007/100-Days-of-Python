import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}

def generate_phonetic():
    word = input()
    try:

        print([nato_dict[letter.upper()] for letter in word])

    except KeyError:

        print("Sorry, only letters from the alphabet please.")
        generate_phonetic()


generate_phonetic()
