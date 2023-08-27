import pandas

data = pandas.read_csv("./NATO/nato_phonetic_alphabet.csv")
    
# #TODO 1. Create a dictionary in this format:
# pd_dict = {new_key:new_val for (index, val) in df.iterrows()}

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

phonetic_list = [phonetic_dict[letter] for letter in user_input]
print(phonetic_list)