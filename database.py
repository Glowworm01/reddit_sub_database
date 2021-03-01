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

test = db.search_by_key('test')
for i in test:
    print(i)

test = db.search_by_value('test')
for i in test:
    print(i)


