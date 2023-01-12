import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(average)
