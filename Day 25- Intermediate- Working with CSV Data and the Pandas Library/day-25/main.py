import pandas

# Create dataframe from csv
# data = pandas.read_csv("weather_data.csv")

# Convert data frame to dictionary
# data_dict = data.to_dict()


# Series from data frame
# temp_data = data.temp

# Convert series to list
# temp_data_list = temp_data.to_list()

# Get Data in Row
# print(data[data.day == "Monday"])


# Get row data when temp was maximum
# print(data[data.temp == temp_data.max()])

# monday = data[data.temp == 14]
# temp = monday.condition

# Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = df["Primary Fur Color"]
gray_fur_color_count = str(len(df[df["Primary Fur Color"] == "Gray"]))
cinnamon_fur_color_count = str(len(df[df["Primary Fur Color"] == "Cinnamon"]))
black_fur_color_count = str(len(df[df["Primary Fur Color"] == "Black"]))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur_color_count, cinnamon_fur_color_count, black_fur_color_count]
}
data_df = pandas.DataFrame(data_dict)
data_df.to_csv("Squirrel Counts.csv")
