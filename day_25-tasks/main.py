# import csv
import pandas

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# avg = sum(temp_list) / len(temp_list)
# print(round(avg))

print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_f = int(monday.temp) * 9/5 + 32
print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Fill", "Lora"],
    "scores": [74, 85, 98]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
print(new_data)
