import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

color_list = data["Primary Fur Color"].to_list()
#print(color_list)
#print(len(color_list))

# Counting the amount of Nan data in the column
count_nan = data["Primary Fur Color"].isnull().sum()
print(f"Number of NaN values is {count_nan}.")

# Counting the amount of squirrels with different fur color
sum_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
sum_of_cin = len(data[data["Primary Fur Color"] == "Cinnamon"])
sum_of_black = len(data[data["Primary Fur Color"] == "Black"])

# Create a dataframe about the amount of squirrels with different color from scratch
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [sum_of_gray, sum_of_cin, sum_of_black]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_data.csv")
print(new_data)