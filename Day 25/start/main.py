import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list)/len(temp_list)

#print(avg)
#
# data_dict = {
#     "students": ["Amy", "James", "Mandy"],
#     "scores": [73, 85, 9]
# }

data = pandas.read_csv("squirrel_data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_fur_data.csv")


