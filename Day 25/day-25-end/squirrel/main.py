import pandas

# with open("./weather_data.csv") as data:
#     content = data.readlines()
#     print(content)

# import csv
#
# with open("./weather_data.csv") as data:
#     content = csv.reader(data)
#     temperature = []
#     row = next(content)
#     for row in content:
#         temperature_str = row[1]
#         temperature_int = int(temperature_str)
#         temperature.append(temperature_int)
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

#data_dic = data.to_dict()
# print(data_dic)
# print(data_dic["temp"])

#temp_list = data["temp"].to_list()
# print(temp_list)
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
# total = temp_sum / len(temp_list)
# print(total)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
#
# print(data[data.day == "Monday"])

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# celsius = int(monday.temp[0])
#
# F = (celsius * 9/5) + 32
# print(F)

# data_dic = {
#     "students": ["Any", "James", "Angela"],
#     "acores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_data.csv")

#Problem
# raw_csv = pandas.read_csv("./day-25-end/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# result = raw_csv["Primary Fur Color"].value_counts()
#
# result.to_csv("./day-25-end/squirrel_count.csv")

#Problem
raw_csv = pandas.read_csv("day-25-end/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(raw_csv[raw_csv["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(raw_csv[raw_csv["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(raw_csv[raw_csv["Primary Fur Color"] == "Black"])

new_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_df = pandas.DataFrame(new_dict)

new_df.to_csv("./day-25-end/squirrel_count.csv")

