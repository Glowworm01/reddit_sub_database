from fuzzywuzzy import process
import re
import json


class Database:
    def __init__(self, file):
        with open(file) as fl:
            self.db = json.load(fl)
            self.db_inverse = {v: k for k, v in self.db.items()}

    def lev_search_by_key(self, query, limit=200, threshold=80):
        return filter(
            lambda x: x[1] > threshold,
            process.extract(query, self.db.keys(), limit=limit),
        )

    def lev_search_by_value(self, query, limit=200, threshold=80):
        return filter(
            lambda x: x[1] > threshold,
            process.extract(query, self.db.values(), limit=limit),
        )

    def regex_search_by_key(self, query):
        return list(
            map(
                lambda x: x.string,
                filter(
                    lambda x: x != None,
                    [re.search(query, key) for key in self.db.keys()],
                ),
            )
        )

    def regex_search_by_value(self, query):
        return list(
            map(
                lambda x: x.string,
                filter(
                    lambda x: x != None,
                    [re.search(query, value) for value in self.db.values()],
                ),
            )
        )
