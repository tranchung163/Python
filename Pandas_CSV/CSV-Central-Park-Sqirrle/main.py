import pandas 

import_data = pandas.read_csv('2018_Central_Park_Squirrel_Data.csv')
# gray_squirrles = import_data[import_data['Primary Fur Color'] == 'Gray']
# print(gray_squirrles)

gray_squirrles_count = len(import_data[import_data['Primary Fur Color'] == 'Gray'])
print(gray_squirrles_count)

red_squirrles_count = len(import_data[import_data['Primary Fur Color'] == 'Cinnamon'])
print(red_squirrles_count)

black_squirrles_count = len(import_data[import_data['Primary Fur Color'] == 'Black'])
print(black_squirrles_count)

data_dict = {
    "Fur Color": ['Gray', 'Red','Black'],
    "Count": [gray_squirrles_count, red_squirrles_count, black_squirrles_count]
}

dtaframe =  pandas.DataFrame(data_dict)
dtaframe.to_csv('squirrel-colors')
