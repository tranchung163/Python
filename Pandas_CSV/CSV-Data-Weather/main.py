# with open(file='weather_data.csv') as data:
#     weather_data = data.readlines()
#     print(weather_data)



# import csv 

# with open(file='weather_data.csv') as data:
#     weather_data = csv.reader(data)
#     temperature_list = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperature_list.append(int(row[1]))
#     print(temperature_list)


import pandas 

data = pandas.read_csv('weather_data.csv')
# print(data['condition'])


# data_dict = data.to_dict()
# print(data_dict)


# temper_data = data['temp']
# print(temper_data.max())

# print(data.condition)

data_monday = data[data.day == 'Monday']
print(data_monday)

# monday_temp = int(data_monday.temp)
# F_temp = monday_temp * 9/5 +32
# print(F_temp)




