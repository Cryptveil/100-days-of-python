import pandas

data = pandas.read_csv("squirrel_data.csv")
fur_color = data["Primary Fur Color"]
gray_count = fur_color.value_counts()["Gray"]
black_count = fur_color.value_counts()["Black"]
cinnamon_count = fur_color.value_counts()["Cinnamon"]
dictionary = {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray_count, cinnamon_count, black_count]
        }
new_data = pandas.DataFrame(dictionary)
new_data.to_csv("new_data.csv")
