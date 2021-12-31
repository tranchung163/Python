student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# letter_code = {}
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for index, row in alphabet_data.iterrows():
#     # print(row.letter)
#     # print(row.code)
#     # print(index)

letter_code = {row.letter: row.code for index, row in alphabet_data.iterrows()}
    # print(letter_code)



    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("What is your name ?: ").upper()
        # for letter in user_input:
        #     if letter in letter_code.keys():
        #         print(f"{letter}: {letter_code[letter.upper()]}")
    try:
        ouput = {letter_code[letter] for letter in user_input}
    except KeyError:
        print("KEYERROR enter your name again: ")
        generate_phonetic()
    else:
        print(ouput)
generate_phonetic()