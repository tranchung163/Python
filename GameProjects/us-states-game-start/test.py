# with open(file='file1.txt') as file1:
#     file1_list = file1.readlines()

# with open(file='file2.txt') as file2:
#     file2_list = file2.readlines()

# result = [int(nums.strip('\n')) for nums in file1_list[1:] if nums in file2_list]
# print(result)





# names = ['Alex','Caroline','Fash','Dave',"Jack",'Josh']

# import random

# dict_names = {student: random.randint(1,100) for student in names}

# passed_student = {student: score for (student, score) in dict_names.items() if score > 50}

# print(passed_student)





# sentence = "What is the air speed velocity of an unladen swallow"
# sentence_list = sentence.split()

# results = {words: len(words) for words in sentence_list}
# print(results)





# temperture = {
#     'monday': 12,
#     'tuesday': 24,
#     'wednesday': 16,
#     'thursday': 22
# }

# temperture_F = {day: (temperture_c * 9/5) + 32 for day, temperture_c in temperture.items()}

# print(temperture_F)





import pandas

student_scores = {
    'Name': ['Angela', 'James', 'Lily'],
    'Score': [36,76,49]
}

convert_dataframe = pandas.DataFrame(student_scores)

for index, row in convert_dataframe.iterrows():
    if row.Name == 'Lily':
        print(row.Score)
