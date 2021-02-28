from fuzzywuzzy import process
import json

class Database:
    def __init__(self, file):
        with open(file) as fl:
            self.db = json.load(fl)

    def search_by_key(self, query, limit=200, threshold=80):
        return filter(lambda x: x[1] > threshold, process.extract(query, self.db.keys(), limit=limit))

    def search_by_value(self, query, limit=200, threshold=80):
        return filter(lambda x: x[1] > threshold, process.extract(query, self.db.values(), limit=limit))


db = Database('sub_db.json')

balls = db.search_by_key('petite')
for i in balls:
    print(i)

balls = db.search_by_value('petite')
for i in balls:
    print(i)


