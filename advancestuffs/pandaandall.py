import pandas

data_files = pandas.read_csv("weather_data.csv")
# temprature = data["temp"].to_list()
# print(temprature)
#
# print(data["temp"].max())


#Getting data from conditions
# print(data.condition)
# print(data.temp)
# print(data.day)

# print(data[data.day == "Monday"])

temps = data_files["temp"].max()

print(data_files[data_files.temp == temps])

#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# celcius= monday.temp[0]
# farhanite = (celcius * 9/5) + 32
#
# print(farhanite)


#Create a dataframe from stratch

# data_dict = {
#     "students": ["Spongebob", "Squarepants", "Patrik"],
#     "Scores": [92, 77, 64]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")