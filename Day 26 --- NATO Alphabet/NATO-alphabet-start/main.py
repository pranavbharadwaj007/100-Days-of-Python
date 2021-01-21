import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}

word = input()
print([nato_dict[letter.upper()] for letter in word])
