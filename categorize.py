from database import Database
import json

with open('cats.json', 'w') as fl:
    json.dump({"tech", ['computer', 'tech', 'code']})

with open('cats.json', 'r') as fl:
    categories = json.load(fl)
