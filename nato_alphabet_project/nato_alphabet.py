# implementation for day 26 from 100 days of code by Dr. Angela

import pandas

read_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for index, row in read_csv.iterrows()}

invalid_input = True

while invalid_input:
    word = input("Type your name: ").upper()
    try:
        code_words = [alphabet_dict[item] for item in word]
        print(code_words)
        invalid_input = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        invalid_input = True



