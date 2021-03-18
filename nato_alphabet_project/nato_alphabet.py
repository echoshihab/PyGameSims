# implementation for day 26 from 100 days of code by Dr. Angela

import pandas

read_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for index, row in read_csv.iterrows()}

word = input("Type your name: ").upper()
code_words = [alphabet_dict[item] for item in word]
print(code_words)

