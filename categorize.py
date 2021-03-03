from database import Database
import json

with open('cats.json', 'r') as fl:
    categories = json.load(fl)

for i in categories:
    print(categories[i])