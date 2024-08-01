import pandas as pd

squirrelsdatas = pd.read_csv("Squirrel_data.csv")
gray_squirrels_count = len(squirrelsdatas[squirrelsdatas["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels_count = len(squirrelsdatas[squirrelsdatas["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrelsdatas[squirrelsdatas["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(Cinnamon_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, Cinnamon_squirrels_count, black_squirrels_count]
}

data = pd.DataFrame(data_dict)
data.to_csv("Squirrels.csv")